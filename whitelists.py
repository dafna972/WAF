import re

#defines appropriate white lists for each web page
class Whitelists():
    def __init__(self):
        pass

    # Activate relevant checks

    def register(self, str):
        list = str.split('&')
        if self._username(list[0])\
        and self._password(list[1])\
        and self._confirm_password(list[2])\
        and self._my_signature(list[3]):
            return str
        else:
            return 'Blocked by WAF'

    def user_info(self, str):
        list = str.split('&')
        if self._username(list[1])\
        and self._password(list[2]):
            return str
        else:
            return 'Blocked by WAF'

    def login(self, str):
        list = str.split('&')
        if self._username(list[0])\
        and self._password(list[1]):
            return str
        else:
            return 'Blocked by WAF'

    def set_color(self, str):
        list = str.split('&')
        if self._color(list[0]):
            return str
        else:
            return 'Blocked by WAF'

    # whitelists:

    def _username(self, current):
        content = current[9:]
        allowed = re.compile('^[A-z0-9]+$')
        matches = allowed.search(content)
        return matches


    def _password(self, current):
        content = current[9:]
        allowed = re.compile('^[A-z0-9]+$')
        matches = allowed.search(content)
        return matches


    def _confirm_password(self, current):
        content = current[17:]
        allowed = re.compile('^[A-z0-9]+$')
        matches = allowed.search(content)
        return matches


    def _my_signature(self, current):
        content = current[13:]
        allowed = re.compile('^[A-z0-9]+$')
        matches = allowed.search(content)
        return matches


    def _color(self, current):
        content =  current[17:]
        allowed = re.compile('^(?:[0-9a-fA-F]{3}){1,2}$')
        matches = allowed.search(content)
        return matches