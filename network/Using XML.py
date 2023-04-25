import xml.etree.ElementTree as ET

data = '''<person>
    <name>Sorin</name>
    <phone type="intl">
    +17343034564
    </phone>
    <email hide="yes"/>
    </person>'''
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
