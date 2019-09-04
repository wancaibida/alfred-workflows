import xml.etree.ElementTree as ET

import xmltodict

data = '''
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.9</version>
</dependency>

'''

data = xmltodict.parse(data)
dependency = data['dependency']
print("{}:{}:{}".format(dependency['groupId'], dependency['artifactId'], dependency['version']).strip())
