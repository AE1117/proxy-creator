# proxy-creator
You can take proxy with send ping to websites.
first download the file. Then add the "proxy_creator" to the project file. Then import it. E.g:

from proxy_creator import take_proxy

proxy = take_proxy(site_name="https://www.google.com.tr/",print_info=False,delay=7000)
print(proxy)

outputs : 
  118.99.87.79:8080


- site_name : site name to send request 
- print_info : print sucseefuly or fail 
- delay : proxy delay 
