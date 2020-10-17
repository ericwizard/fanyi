import requests
import json


def get_str(word):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
    data = {
        "i": word,
        "from": "AUTO",
        "to": "Auto",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION",
        "typoResult": "false",
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.text
    else:
        return "404 Not Found"


def get_dict(word):
    str = get_str(word)
    if str != "404 Not Found":
        dict = json.loads(str)
        return dict
    else:
        return "404 Not Found"


def get_word(word):
    dict = get_dict(word)
    if dict != "404 Not Found":
        return_word = dict["translateResult"][0][0]["tgt"]
        return return_word
    else:
        return "404 Not Found"
