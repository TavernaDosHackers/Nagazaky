#!/usr/bin/env python3

class Color:
    """ Helper object for easily printing colored text to the terminal. """

    # Basic console colors
    colors = {
        "W": "\033[0m",  # white (normal)
        "PK": "\033[95m",  # pink
        "R": "\033[31m",  # red
        "G": "\033[32m",  # green
        "O": "\033[33m",  # orange
        "B": "\033[34m",  # blue
        "P": "\033[35m",  # purple
        "C": "\033[36m",  # cyan
        "GR": "\033[37m",  # gray
        "D": "\033[2m"  # dims current color. {W} resets.
    }

    # Helper string replacements
    replacements = {
        "{+}": " {W}{D}[{W}{G}+{W}{D}]{W}",
        "{-}": " {W}{D}[{W}{GR}-{W}{D}]{W}",
        "{!}": " {O}[{R}!{O}]{W}",
        "{?}": " {W}[{C}?{W}]"
    }

    @staticmethod
    def return_message(message):
        """ Returns colored string """
        output = message
        for (key, value) in Color.replacements.items():
            output = output.replace(key, value)
        for (key, value) in Color.colors.items():
            output = output.replace("{%s}" % key, value)
        return output

    @staticmethod
    def print(message):
        """
        Prints text using colored format on same line.
        Example:
            Color.p("R}This text is red. {W} This text is white")
        """
        import sys
        sys.stdout.write(Color.return_message(message))
        sys.stdout.flush()

    @staticmethod
    def println(message):
        """Prints text using colored format with trailing new line."""
        Color.print("%s\n" % message)

    @staticmethod
    def exception(message, ex):
        """ Prints message exception """
        Color.println(Color.return_message("{!} {R}%s{W}: " % message) + str(ex))


if __name__ == "__main__":
    Color.println("{R}Testing {G}One {C}Two {P}Three {W}Done")
    print(Color.return_message("{C}Testing {P}String {W}"))
    Color.println("{+} Good line")
    Color.println("{!} Danger")
