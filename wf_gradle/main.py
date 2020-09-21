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
    args = []

    for k in ['groupId', 'artifactId', 'version']:
        if k in dependency:
            args.append(dependency[k])

    return ':'.join([str(ele) for ele in args])


if __name__ == '__main__':
    if len(sys.argv) > 1 and len(sys.argv[1].strip()):
        query = sys.argv[1]
    else:
        query = sys.stdin.read()

    output = main(query)

    result = {
        'items': [
            {'title': output, 'arg': output},
            {'title': 'implementation("{}")'.format(output), 'arg': 'implementation({})'.format(output)}
        ]
    }
    json.dump(result, sys.stdout)
    sys.stdout.flush()
