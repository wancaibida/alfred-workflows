import requests
import json
import sys
import os


def build_items(iterable, fun):
    items = []
    for it in iterable:
        items.append(fun(it))
    return items


def print_items(items):
    result = {'items': items}
    json.dump(result, sys.stdout)
    sys.stdout.flush()
    return


def send_request(method, url, data=None):
    try:
        request_method = getattr(requests, method)
        if request_method is None:
            return

        response = request_method(
            url="https://api.pushbullet.com/v2" + url,
            headers={
                "Access-Token": get_token(),
                "Content-Type": 'application/json'
            },
            data=data
        )

        return response.json()
    except requests.exceptions.RequestException:
        result = {'items': {'title': 'HTTP Request failed', 'arg': 'HTTP Request failed'}}
        json.dump(result, sys.stdout)
        sys.stdout.flush()
        exit(-1)


def list_devices(query):
    result = send_request('get', '/devices')
    items = build_items(result['devices'], lambda it: {'title': it['model'], 'arg': query + ' ' + it['iden']})
    items.insert(0, {'title': 'All Devices', 'arg': query})
    print_items(items)


def push(content, device=None):
    body = {
        "type": "file",
        "body": content
    }

    if device is not None:
        body['device_iden'] = device

    resp = send_request('post', '/pushes', json.dumps(body))

    items = [{'title': content, 'arg': json.dumps(resp)}]
    result = {'items': items}
    json.dump(result, sys.stdout)
    sys.stdout.flush()


def get_token():
    with open(os.environ['alfred_workflow_data'], 'r') as f:
        token = f.readline()
    return token


def set_token(token):
    with open(os.environ['alfred_workflow_data'], 'w+') as f:
        f.writelines(token)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        first_arg = sys.argv[1].strip()
        if first_arg == 'list':
            if len(sys.argv) > 2 and len(sys.argv[2].strip()):
                query = sys.argv[2].strip()
            else:
                query = sys.stdin.read()
            list_devices(query)
        elif first_arg == 'push':
            if len(sys.argv) > 2 and len(sys.argv[2].strip()):
                content = sys.argv[2].strip()
            else:
                content = sys.stdin.read()

            if len(sys.argv) > 3 and len(sys.argv[3].strip()):
                device = sys.argv[3].strip()
            else:
                device = None
            push(content, None)
        elif first_arg == 'set':
            if len(sys.argv) > 2 and len(sys.argv[2].strip()):
                token = sys.argv[2].strip()
                set_token(token)
