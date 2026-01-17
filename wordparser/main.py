import json

# Opening JSON file
f = open('data.json')
g = open("demofile2.txt", "a")

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['words']:
    g.write(i['word'])
    g.write('\n')

# Closing file
f.close()