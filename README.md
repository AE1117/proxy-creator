# proxy-creator
You can take proxy with send ping to websites.
first download the file. Then add the "proxy_creator" to the project file. Then import it. E.g:

from proxy_creator import take_proxy

proxy = take_proxy("https://www.facebook.com/")
print(proxy)

outputs : 
  118.99.87.79:8080
