import requests
import xml.etree.ElementTree as ET
import pprint

response = requests.get('http://www.ibiblio.org/xml/examples/shakespeare/macbeth.xml')
tree = ET.fromstring(response.content)

def speeches(act, values):
    speech = act.findall('SCENE/SPEECH')
    for x in speech:
        speakers = x.findall('SPEAKER')
        lines = x.findall('LINE')
        for s in speakers:
            if s.text == 'ALL':
                pass
            elif s.text.title() in values:
                values[s.text.title()] += len(lines)
            else:
                values[s.text.title()] = len(lines)
    return values

def acts(tree):
    values = {}
    for child in tree:
        if child.tag == "ACT": 
            speeches(child, values)
    return sorted(values.items(), key=lambda character: character[1], reverse=True)


def choose():
    url = input("Enter the play's url (leave blank for Macbeth): ")
    if len(url) > 0:
            pass
    else:
        url = 'http://www.ibiblio.org/xml/examples/shakespeare/macbeth.xml'

    response = requests.get(url)
    tree = ET.fromstring(response.content)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(acts(tree))

if __name__ == '__main__':
    choose()

choose()




