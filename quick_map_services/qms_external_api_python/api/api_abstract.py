try:
    from ..requests import get
except:
    from requests import get

from .default import DEFAULT_URL


class ApiClient(object):
    VERSION = 0

    def __init__(self, endpoint_url=DEFAULT_URL):
        self.endpoint_url = endpoint_url
        self.__proxy = {}
        
    def set_proxy(self, proxy_host, proxy_port, proxy_user, proxy_password):
        if proxy_host != "":
            proxy_url = proxy_host
            if proxy_port != "":
                proxy_url = "%s:%s" % (proxy_url, proxy_port)
            if proxy_user != "":
                proxy_url = "%s:%s@%s" % (
                    proxy_user,
                    proxy_password,
                    proxy_url
                )

            self.__proxy = {
                "http": proxy_url
            }

    @property
    def base_url(self):
        return '%s/api/v%s/' % (self.endpoint_url, self.VERSION)

    def full_url(self, sub_url):
        return self.base_url + sub_url

    def _get_json(self, url, params=None):
        _params = {}
        if params is not None:
            _params.update(params)
            _params.update(self.__proxy)

        response = get(url, params=_params, verify=False)
        return response.json()

    def _get_content(self, url, params=None):
        response = get(url, params=params, stream=True, verify=False)
        return response.content
