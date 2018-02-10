import os
import tempfile
import argparse
import json
from collections import defaultdict


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--key',
        type=str,
        default=None,
    )
    parser.add_argument(
        '--val',
        type=str,
        default=None,
        nargs='?'
    )
    parser.add_argument(
        '--clear', action='store_true'
    )
    return parser.parse_args()


def main():
    storage = defaultdict(list)

    args = get_args()


    storage_path= os.path.join(tempfile.gettempdir(), 'storage.data')
    if args.clear:
        os.remove(storage_path)
        exit()


    with open(storage_path, 'a') as write_object, open(storage_path, 'r') as read_object:
        key = args.key
        data = [line.strip() for line in read_object]

        if data:
            json_object = json.loads(''.join(data))
            [[storage[k].append(i) for i in v] for k, v in json_object.items()]

        if args.val:
            val = args.val
            [storage[key].append(val) ]
            write_object.seek(0)
            write_object.truncate()
            write_object.write(json.dumps(storage, ensure_ascii=False))
        else:
            if storage.get(key, None):
                [str(i) for i in storage.get(key)]
                k = ', '.join(storage.get(key))
                print(k)
            else:
                print('')

if __name__ == '__main__':
     main()
