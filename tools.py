import re

#finds the appropriate context in order to check correctly the request body
class Tools():
    def __init__(self):
        self._username = re.compile('^username=')
        self._password = re.compile('^password=')
        self._confirm_password = re.compile('^confirm_password=')
        self._my_signature = re.compile('^my_signature=')
        self._background_color = re.compile('^background_color=')
        self._blog_entry = re.compile('^blog_entry=')

    def find_context(self, str):
        list = str.split('&')
        if len(list) == 5:
            if self._username.match(list[0]) \
                and self._password.match(list[1]) \
                    and self._confirm_password.match(list[2]) \
                    and self._my_signature.match(list[3]) \
                    and list[4] == 'register-php-submit-button=Create+Account':
                return 'register'
        elif len(list) == 4:
            if list[0] == 'user-info.php' \
                and self._username.match(list[1]) \
                    and self._password.match(list[2]) \
                    and list[4] == 'register-php-submit-button=View+Account+Details':
                return 'user-info'
        elif len(list) == 3:
            if self._username.match(list[0]) \
                    and self._password.match(list[1]) \
                    and list[2] == 'login-php-submit-button=Login':
                return 'login'
            if self._blog_entry.match(list[1]) \
                    and list[2] == "add-to-your-blog-php-submit-button=Save+Blog+Entry":
                return 'blog_entry'
        elif len(list) == 2:
            if self._background_color.match(list[0])\
                    and list[1] == 'set-background-color-php-submit-button=Set+Background+Color':
                return 'set-color'

