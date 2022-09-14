import requests

def main():
    status_code = requests.get('http://www.google.com')
    print(status_code)
    return requests.__version__


print(main())
