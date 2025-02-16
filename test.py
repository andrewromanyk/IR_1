import xml.etree.ElementTree as ET

fb2 = ET.parse('test.xml').getroot()

for text in fb2.itertext():
    print("'" + text + "'")

# print("a1'".isalnum())