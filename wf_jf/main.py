import json
import sys
from json import JSONDecodeError

if __name__ == '__main__':
    if len(sys.argv) > 1 and len(sys.argv[1].strip()):
        query = sys.argv[1]
    else:
        query = sys.stdin.read()

    try:
        parsed = json.loads(query)
    except JSONDecodeError:
        json.dump({'items': [{'title': 'Invalid JSON'}]}, sys.stdout)
        sys.stdout.flush()
        exit(-1)

    formatted = json.dumps(parsed, indent=4)
    lines = formatted.split('\n')
    items = []
    for line in lines:
        items.append({'title': line, 'arg': formatted})

    result = {'items': items}
    json.dump(result, sys.stdout)
    sys.stdout.flush()
