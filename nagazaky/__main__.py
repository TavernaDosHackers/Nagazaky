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
    from nagazaky.discovery.wordpress.scan import Scan
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
        self.args.user_agent = Settings.get_user_agent(self.args.user_agent)
        self.args.proxy = Settings.get_proxy(self.args.proxy)

        # Configure Request.
        self.request = Request(self.args.user_agent, self.args.proxy)

        # Configure Banner.
        self.banner = Banner()

    def run(self) -> None:
        """ Method that starts Nagazaky. """

        # Check --no-banner.
        if self.args.no_banner is False:
            self.banner.print_logo()

        # Configure Update.
        # Check --update.
        update = Update(self.request)
        update_verify = update.verify(self.args.update)
        if self.args.update and update_verify:
            update.upgrade()
            sys.exit()

        # Check --url.
        # Print help message.
        if self.args.url is None:
            self.banner.print_helper()
            sys.exit()

        # Target URL.
        # Format target URL.
        self.args.url = Settings.target(self.args.url)
        # Prints the Target URL and IP.
        try:
            target_ip = self.args.url + " [{P}" + str(
                socket.gethostbyname(Settings.target_simple(self.args.url))) + "{W}]"
            Color.println("\n{+} %s" % target_ip)
        except:
            Color.println("\n{+} %s" % self.args.url)

        # Prints the selected proxy on the screen.
        if self.args.proxy != "":
            for key, value in self.args.proxy.items():
                key_value = str(value)
                Color.println("{+} Proxy: %s" % key_value)

        # Prints the selected User-Agent on the screen.
        for key, value in self.args.user_agent.items():
            key_value = str(value)
            Color.println("{+} User-Agent: %s" % key_value)

        # Start Scan!
        print("\nInteresting Finding(s):\n")

        # Discovery.
        Color.println("{+} {P}Discovery:{W}")

        # Check robots.txt.
        robots_txt = self.request.get(self.args.url + "robots.txt").text
        if "User-agent: *" in robots_txt or "User-Agent: *" in robots_txt:
            Color.println(" ├─{+} {G}Robots.txt:{W}")
            Color.println(" │  ├ %s" % self.args.url + "robots.txt")

        # Check CMS.
        # Configure CheckCMS
        check_cms = CheckCMS(self.args.url, self.request)
        Color.println(" ├─{+} {G}CMS:{W}")
        list_cms = check_cms.run()

        # Finally discovery.
        Color.println(" └──┘")

        if "wordpress" in list_cms:
            Color.println("\n{+} {P}WordPress:{W}")
            wordpress_scan = Scan(self.args.url, self.request)
            wordpress_scan.directories_listing()
            version_readme = wordpress_scan.readme_html()

            # Finally WordPress.
            Color.println(" └──┘")
        elif "joomla" in list_cms:
            pass
        elif "drupal" in list_cms:
            pass


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
