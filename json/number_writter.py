import json

numbers = [2,3,5,7,12]
fileName = 'numbers.json'
with open(fileName,'w') as f_obj:
    json.dump(numbers,f_obj)