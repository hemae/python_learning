import argparse
import json


try:
    with open('storage.data', 'r') as f:
        my_dict = json.load(f)
except Exception:
    _dict = {}
    with open('storage.data', 'w') as f:
        json.dump(_dict, f)

with open('storage.data', 'r') as f:
    my_dict = json.load(f)

parser = argparse.ArgumentParser()
parser.add_argument('--key', help='key argument')
parser.add_argument('--value', help='value argument')
args = parser.parse_args()

if args.value == None:
    if args.key not in my_dict.keys():
        print('None')
    else:
        for i in range(len(my_dict[args.key])):
            if i == (len(my_dict[args.key]) - 1):
                print(my_dict[args.key][i])
            else:
                print(my_dict[args.key][i], end=', ')
else:
    if args.key not in my_dict.keys():
        my_dict[args.key] = []
   # if args.value not in my_dict[args.key]:
    my_dict[args.key].append(args.value)

with open('storage.data', 'w') as f:
    json.dump(my_dict, f)
