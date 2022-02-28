import requests
from colorama import Fore
from proxy_manager_g4 import ProxyManager
from proxy_manager_g4.consts import PROTOCOL_HTTPS


def take_proxy(site_name="https://www.google.com.tr/",print_info=False,delay=7000):
    while True:
        try:
            proxy_manager = ProxyManager(protocol=PROTOCOL_HTTPS, anonymity=True)
            proxy = proxy_manager.get_random()

            proxyies = {"http": f"http://username:password@{proxy}",
                        "https": f"http://username:password@{proxy}"}

            url = site_name

            r = requests.get(url, proxies=proxyies, timeout=(3.05, delay))

            if r.status_code == 200:
                if print_info==True:
                    print(Fore.GREEN+f"[+]{proxy} is sucsessfuly connected!")
                return proxy
            else:
                if print_info==True:
                    print(Fore.RED+f"[-]{proxy} is failed to connect,trying again...")
                pass

        except:
            pass


