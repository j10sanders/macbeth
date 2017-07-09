import requests
import xml.etree.ElementTree as ET
import sys

response = requests.get('http://www.ibiblio.org/xml/examples/shakespeare/macbeth.xml')
tree = ET.fromstring(response.content)

def speeches(act, result):
    speech = act.findall('SCENE/SPEECH')
    for x in speech:
        speakers = x.findall('SPEAKER')
        lines = x.findall('LINE')
        for speaker in speakers:
            if speaker.text == 'ALL':
                pass
            elif speaker.text.title() in result:
                result[speaker.text.title()] += len(lines)
            else:
                result[speaker.text.title()] = len(lines)
    return result


def acts(tree):
    result = {}
    for child in tree:
        if child.tag == "ACT": 
            speeches(child, result)
    return sorted(result.items(), key=lambda character: character[1], reverse=True)


def choose():
    url = input("Enter the play's url (leave blank for Macbeth): ")
    if len(url) > 0:
        pass
    else:
        url = 'http://www.ibiblio.org/xml/examples/shakespeare/macbeth.xml'

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)
    try:
        tree = ET.fromstring(response.content)
    except ET.ParseError:
        print("That doc isn't the right xml format :(")
        sys.exit(1)
    for key, value in acts(tree):
        print("%s has %s" % (key, value))


if __name__ == '__main__':
    choose()