import xml.etree.ElementTree as ET

tree = ET.parse('macbeth.xml')
values = {}

def speeches(act):
    speech = act.findall('SCENE/SPEECH')
    for x in speech:
        speaker = x.findall('SPEAKER')
        line = x.findall('LINE')
        speakers(speaker, line)


def speakers(speaker, line):
    for s in speaker:
        if s.text == 'ALL':
            pass
        elif s.text.title() in values:
            values[s.text.title()] += len(line)
        else:
            values[s.text.title()] = len(line)

def acts(root):
    for child in root:
        if child.tag == "ACT":
            speeches(child)

acts(tree.getroot())
print(values)





