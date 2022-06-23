import requests

def scan(url):
    return requests.get(url).headers

def print_test():
    print("print_test")