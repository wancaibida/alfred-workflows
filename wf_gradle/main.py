import json
import sys
import xmltodict


def main(xml_input):
    data = xmltodict.parse(xml_input)
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
