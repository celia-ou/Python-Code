# Load JSON file
# Load into dictionary
# Set dictionary key to: userId
# Print dictionary using a for loop, not a while loop
# Then save the dictionary to a XML file without the userId

import json
import xml.etree.ElementTree as ET

filename = "Sample-JSON-file-with-multiple-records-download.json"
handle = open(filename,'r')

data = json.load(handle)

user_dict = dict()
for p in data["users"]:
    key = p.pop("userId")
    user_dict[key] = p
    print(key, ":", p)

root = ET.Element("Contacts")
tree = ET.ElementTree(root)
for i in user_dict:
    child = ET.Element("User")
    for k, v in user_dict[i].items():
        #child.set(k, v)
        grandchild = ET.Element(k)
        grandchild.text = v
        child.append(grandchild)
    root.append(child)

#output_file = open("converted_file.xml","w")
tree.write("converted_file.xml", encoding = 'utf8')
