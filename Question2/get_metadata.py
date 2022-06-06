import requests
import json

url = 'http://169.254.169.254/latest/'

def expand_response(url, url_to_add):
    result = {}
    for str in url_to_add:
        new_url = url + str
        resp = requests.get(new_url)
        resp_text = resp.text
        if str[-1] == "/":
            list_of_values = resp_text.splitlines()
            result[str[:-1]] = expand_response(new_url, list_of_values)
        elif check_json(resp_text):
            result[str] = json.loads(resp_text)
        else:
            result[str] = resp_text
    return result
    
def extract_metadata():
    first_expand = ["meta-data/"]
    result = expand_response(url, first_expand)
    return result

def convert_to_json():
    result=extract_metadata()
    json_metadata = json.dumps(result, indent=4, sort_keys=True)
    return json_metadata

def check_json(json_to_check):
    try:
        json.loads(json_to_check)
    except ValueError:
        return False
    return True

if __name__ == '__main__':    
    print(convert_to_json())

