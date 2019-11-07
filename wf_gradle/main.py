import json
import sys
import xml
import xmltodict


def main(xml_input):
    try:
        data = xmltodict.parse(xml_input)
    except xml.parsers.expat.ExpatError:
        return "Invalid Input"
    dependency = data['dependency']
    return "{}:{}:{}".format(dependency['groupId'], dependency['artifactId'], dependency['version']).strip()


if __name__ == '__main__':
    if len(sys.argv) > 1 and len(sys.argv[1].strip()):
        query = sys.argv[1]
    else:
        query = sys.stdin.read()

    output = main(query)

    result = {'items': [{'title': output, 'arg': output}]}
    json.dump(result, sys.stdout)
    sys.stdout.flush()
