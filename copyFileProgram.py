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


srcFile = os.path.join('/Users/lana/desktop/generator', str(firstName) + '.json')
destFile = os.path.join('/Users/lana/desktop/generator/assets', str(newName) + '.json')

srcPng = os.path.join('/Users/lana/desktop/generator', str(firstName) + '.png')
destPng = os.path.join('/Users/lana/desktop/generator/assets', str(newName) + '.png')

try:
    path = shutil.copyfile(srcFile,destFile)
except shutil.SameFileError:
    path = shutil.copyfile(srcFile,destFile)
    
try:
    path = shutil.copyfile(srcPng, destPng)
except shutil.SameFileError:
    path = shutil.copyfile(srcPng, destPng)
        

for i in range(0, count+1):
    prevName = newName
    newName = newName + 1
    srcFile = os.path.join('/Users/lana/desktop/generator/assets', str(prevName) + '.json')
    destFile = os.path.join('/Users/lana/desktop/generator/assets', str(newName) + '.json')
    
    srcPng = os.path.join('/Users/lana/desktop/generator/assets', str(prevName) + '.png')
    destPng = os.path.join('/Users/lana/desktop/generator/assets', str(newName) + '.png')
    
    try:
        path = shutil.copyfile(srcPng, destPng)
    except shutil.SameFileError:
        path = shutil.copyfile(srcPng, destPng)

    with open(os.path.join('/Users/lana/desktop/generator/assets', str(prevName) + '.json'), 'r+') as file:
        data = json.load(file)
        data['name'] = name + " #" + str(newName)
        data['image'] = str(prevName) + ".png"
        data['properties']['files'][0]['uri'] = str(prevName) + ".png"
        data['attributes'][0]['trait_type'] = traitType
        data['attributes'][0]['value'] = value
        data['symbol'] = symbol
        data['description'] = desc
        file.seek(0)
        json.dump(data, file, indent=2)
        file.truncate()
        try:
            path = shutil.copyfile(srcFile,destFile)
        except shutil.SameFileError:
            path = shutil.copyfile(srcFile,destFile)
        
    
    
    
    
    
    
    
print(str(count) + ' files duplicated')
