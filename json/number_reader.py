import json
fileName = 'numbers.json'
with open(fileName) as obj:
    numbers = json.load(obj)
print(numbers)