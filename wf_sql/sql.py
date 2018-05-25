import sqlparse
import json
import sys
import re


def create_item(title, arg):
    return {'title': title, 'arg': arg}


if __name__ == '__main__':
    if len(sys.argv) > 1 and len(sys.argv[1].strip()):
        query = sys.argv[1]
    else:
        query = sys.stdin.read()
    formatted_sql = sqlparse.format(query.strip(), reindent=True, keyword_case='upper')

    long_sql = re.sub(r"\n", ' ', formatted_sql)
    long_sql = re.sub(r" +", ' ', long_sql)

    items = [create_item(formatted_sql, formatted_sql), create_item(long_sql, long_sql)]

    json.dump({'items': items}, sys.stdout)
    sys.stdout.flush()
