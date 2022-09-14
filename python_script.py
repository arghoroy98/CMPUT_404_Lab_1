import requests

def main():
    print ("Getting Google homepage")
    status_code = requests.get('http://www.google.com')
    print(status_code)
    
    python_script_src_code = requests.get('https://raw.githubusercontent.com/arghoroy98/CMPUT_404_Lab_1/main/python_script.py')
    
    print("#" * 60)
    print(python_script_src_code.text)
    print("#" * 60)

    print("Version of requests module is ")
    return requests.__version__


print(main())
