#!/usr/bin/env python3

try:
    from nagazaky.core.color import Color
    from nagazaky.core.banner import Banner
    from nagazaky.core.update import Update
    from nagazaky.core.args import Arguments

    import sys
    from requests import get
except (ValueError, ImportError) as e:
    Color.exception("Error", e)
except Exception as e:
    Color.exception("Unknown exception error", e)


class Nagazaky:
    def __init__(self):
        """ Constructor and Attributes. """
        self.args = Arguments().args
        self.banner = Banner()
        self.update = Update()

    def run(self) -> None:
        """ Method that starts Nagazaky. """
        if self.args.no_banner is False:
            self.banner.print_logo()

        if self.args.url is None:
            self.banner.print_helper()
            sys.exit()

        self.update.verify()
        if self.args.update is True:
            self.update.upgrade()
            sys.exit()


def entry_point() -> None:
    try:
        nagazaky = Nagazaky()
        nagazaky.run()
    except KeyboardInterrupt as ex:
        Color.exception("KeyboardInterrupt", ex)
    except Exception as ex:
        Color.exception("Unknown exception error", ex)


if __name__ == "__main__":
    entry_point()
