class colors:
    # Define as variáveis de cores
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    CYAN = '\033[36m'
    YELLOW = '\033[33m'
    BLACK = '\033[30m'
    WHITE = '\033[37m'
    RESET = '\033[0;0m'
    BOLD = '\033[1m'

class settings:
    banner = f"""
    _________________________________________________________________________{colors.GREEN}{colors.BOLD}
            _   _                            _
            | \ | |                          | |           Mass Exploit
            |  \| | __ _  __ _  __ _ ______ _| | ___   _      Finder Priv8
            | . ` |/ _` |/ _` |/ _` |_  / _` | |/ / | | |
            | |\  | (_| | (_| | (_| |/ / (_| |   <| |_| |
            |_| \_|\__,_|\__, |\__,_/___\__,_|_|\_\\__, |
                        __/ |                     __/ |
                        |___/                     |___/{colors.RESET}
    _________________________________________________________________________
    """

    user_agent_default = "Nagazaky Browser"