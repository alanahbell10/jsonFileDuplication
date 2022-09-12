import os
import shutil
import json

firstName = 0

newName = firstName
prevName = newName
count = int(input("How many times would you like to duplicate " + str(firstName) + ".json? "))
name = str(input("Enter name: "))
symbol = str(input("Enter symbol: "))
traitType = str(input("Enter trait type: "))
value = str(input("Enter value: "))
desc = str(input("Enter description: "))


src = os.path.join('/Users/lana/desktop/generator', str(firstName) + '.json')
dest = os.path.join('/Users/lana/desktop/generator/assets', str(newName) + '.json')

try:
    path = shutil.copyfile(src,dest)
except shutil.SameFileError:
    pass
        

for i in range(0, count):
    prevName = newName
    newName = newName + 1
    src = os.path.join('/Users/lana/desktop/generator/assets', str(prevName) + '.json')
    dest = os.path.join('/Users/lana/desktop/generator/assets', str(newName) + '.json')

    with open(os.path.join('/Users/lana/desktop/generator/assets', str(prevName) + '.json'), 'r+') as file:
        data = json.load(file)
        data['name'] = name + " #" + str(newName + 1)
        data['image'] = str(newName) + ".png"
        data['properties']['files'][0]['uri'] = str(newName) + ".png"
        data['attributes'][0]['trait_type'] = traitType
        data['attributes'][0]['value'] = value
        data['symbol'] = symbol
        data['description'] = desc
        file.seek(0)
        json.dump(data, file, indent=2)
        file.truncate()
        try:
            path = shutil.copyfile(src,dest)
        except shutil.SameFileError:
            pass
        
    
    
    
    
    
    
    
print(str(count) + ' files duplicated')
