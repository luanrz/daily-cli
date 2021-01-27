import requests

from daily.config import CustomConfig
from daily.model import User


class Api:
    def __init__(self):
        self.server_url = CustomConfig().get('server_url')
        self.login_server_url = self.server_url + '/user/login'
        self.sync_server_url = self.server_url + '/task/sync'

    def login(self, username, password):
        data = {'username': username, 'password': password}
        try:
            response = requests.post(self.login_server_url, data)
        except requests.RequestException:
            return 'Can\'t connect to server, Please check your server_url config or your network'

        response_json = response.json()
        response_headers = response.headers

        error_code = None
        error_msg = None
        user_id = None
        username = None
        jwt = None
        if 'errorCode' in response_json:
            error_code = response_json['errorCode']
        if 'errorMsg' in response_json:
            error_msg = response_json['errorMsg']
        if 'userId' in response_json:
            user_id = response_json['userId']
        if 'username' in response_json:
            username = response_json['username']
        if 'jwt' in response_headers:
            jwt = response_headers['jwt']

        if (error_code is not None) and (error_msg is not None):
            return '%s(%s)' % (error_msg, error_code)
        if (user_id is not None) and (username is not None) and (jwt is not None):
            user = User()
            user.user_id = user_id
            user.username = username
            user.jwt = jwt
            return user
        return None

    def sync(self):
        pass
