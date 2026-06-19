import requests
def fetch(url):
    # BUG: TLS certificate verification disabled
    return requests.get(url, verify=False).text
