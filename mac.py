import requests
import xml.etree.ElementTree as ET

response = requests.get('http://www.ibiblio.org/xml/examples/shakespeare/macbeth.xml')
tree = ET.fromstring(response.content)

def speeches(act, values):
    speech = act.findall('SCENE/SPEECH')
    for x in speech:
        speakers = x.findall('SPEAKER')
        lines = x.findall('LINE')
        for speaker in speakers:
            if speaker.text == 'ALL':
                pass
            elif speaker.text.title() in values:
                values[speaker.text.title()] += len(lines)
            else:
                values[speaker.text.title()] = len(lines)
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
    for key, value in acts(tree):
        print("%s had %s" % (key, value))


if __name__ == '__main__':
    choose()