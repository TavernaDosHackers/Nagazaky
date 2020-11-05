#!/usr/bin/env python3

"""
MIT License

Copyright (c) 2020 Taverna dos Hackers

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

try:
    import sys
    import socket
    from requests import get

    # Core
    from nagazaky.core.color import Color
    from nagazaky.core.settings import Settings
    from nagazaky.core.banner import Banner
    from nagazaky.core.update import Update
    from nagazaky.core.request import Request
    from nagazaky.core.args import Arguments

    # Discovery
    from nagazaky.discovery.checkcms import CheckCMS
    from nagazaky.discovery.searchdns import SearchDNS
except (ValueError, ImportError) as e:
    Color.exception("Import Error", e)
except Exception as e:
    Color.exception("Error", e)


class Nagazaky:
    def __init__(self):
        """ Constructor and Attributes. """

        # Core
        # Configure Arguments.
        self.args = Arguments().args
        self.args.url = Settings.target(self.args.url)
        self.args.user_agent = Settings.get_user_agent(self.args.user_agent)
        self.args.proxy = Settings.get_proxy(self.args.proxy)

        # Configure Request.
        self.request = Request(self.args.user_agent, self.args.proxy)

        # Configure Update.
        self.update = Update(self.request)

        # Configure Banner.
        self.banner = Banner()

        # Discovery.
        # Configure CheckCMS
        self.check_cms = CheckCMS(self.args.url, self.request)

        # Configure SearchDNS.
        self.search_dns = SearchDNS(self.args.url, self.request)

    def run(self) -> None:
        """ Method that starts Nagazaky. """

        # Check --no-banner.
        if self.args.no_banner is False:
            self.banner.print_logo()

        # Check --update.
        update_verify = self.update.verify(self.args.update)
        if self.args.update and update_verify:
            self.update.upgrade()
            sys.exit()

        # Check --url.
        # Print help message.
        if self.args.url is None:
            self.banner.print_helper()
            sys.exit()

        # Target URL.
        target_ip = self.args.url + " [{P}" + str(socket.gethostbyname(Settings.target_simple(self.args.url))) + "{W}]"
        Color.println("\n{+} %s" % target_ip)

        # Prints the selected proxy on the screen.
        if self.args.proxy != "":
            for key, value in self.args.proxy.items():
                key_value = key + "://" + str(value)
                Color.println("{+} Proxy: %s" % key_value)

        # Prints the selected User-Agent on the screen.
        for key, value in self.args.user_agent.items():
            key_value = str(value)
            Color.println("{+} User-Agent: %s\n" % key_value)

        print("Interesting Finding(s):\n")

        # Discovery CMS.
        Color.println("{+} Discovery:")

        # Check robots.txt.
        robots_txt = self.request.get(self.args.url + "robots.txt").text
        if "User-agent: *" in robots_txt or "User-Agent: *" in robots_txt:
            Color.println(" ├─{+} Robots.txt: %s" % self.args.url + "robots.txt")

        # Check CMS.
        Color.println(" ├─{+} CMS:")

        check_cms_wordpress = self.check_cms.wordpress()
        check_cms_joomla = self.check_cms.joomla()
        check_cms_drupal = self.check_cms.drupal()

        if check_cms_wordpress:
            Color.println(" │  ├ WordPress: {G}running{W} (/wp-content/)")
        elif check_cms_joomla:
            Color.println(" │  ├ Joomla: {G}running{W} (/com_content/)")
        elif check_cms_drupal:
            Color.println(" │  ├ Drupal: {G}running{W} (/sites/default/files/)")
        else:
            Color.println(" │  │ 'No valid CMS was found.'")


def entry_point() -> None:
    try:
        nagazaky = Nagazaky()
        nagazaky.run()
    except KeyboardInterrupt as ex:
        Color.exception("KeyboardInterrupt", ex)
    except Exception as ex:
        Color.exception("Error", ex)


if __name__ == "__main__":
    entry_point()
