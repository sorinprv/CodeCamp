import json

data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
info = json.loads(data)
print(info[1]['name'])

input = '''[
    { "id" : "001",
        "x" : "2",
        "name" : "Quincy"
    } ,
    { "id" : "009",
        "x" : "7",
        "name" : "Mrugesh"
    }
]'''
info = json.loads(input)
print('User:', len(info))
for item in info:
    print('Name', item['name'])
    print('ID', item['id'])
    print('Attribute', item['x'])
