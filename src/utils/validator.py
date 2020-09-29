import re

class Validator:
    def __init__(self):
        ...

    def url(self, url):
        url_list = []

        regex = re.compile(r'^(?:http|ftp)s?://') # http:// or https://
        regex = re.match(regex, url) is not None

        if regex is True and not url in url_list:
            url_list.append(url)
        
        return url_list