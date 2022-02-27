import requests
from proxy_manager_g4 import ProxyManager
from proxy_manager_g4.consts import PROTOCOL_HTTPS


def take_proxy(site_name="https://www.google.com.tr/"):
    while True:
        try:
            proxy_manager = ProxyManager(protocol=PROTOCOL_HTTPS, anonymity=True)
            proxy = proxy_manager.get_random()

            proxyies = {"http": f"http://username:password@{proxy}",
                        "https": f"http://username:password@{proxy}"}

            url = site_name

            r = requests.get(url, proxies=proxyies, timeout=(3.05, 7000))

            if r.status_code == 200:
                return proxy
            else:
                pass

        except:
            pass


