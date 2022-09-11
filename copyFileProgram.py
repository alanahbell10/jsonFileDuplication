import os
import shutil
import json

firstName = int(input("Enter number of starting JSON file name: "))
numFiles = int(input("How many times would you like to duplicate " + str(firstName) + ".json? "))


prevName = firstName
newName = firstName + 1
count = numFiles

for i in range(0, count):

	src = os.path.join('/Users/lana/Desktop/', str(prevName) + '.json')
	dest = os.path.join('/Users/lana/Desktop/', str(newName) + '.json')	
	path = shutil.copyfile(src, dest)

	with open(os.path.join('/Users/lana/Desktop/', str(newName) + '.json'), 'r+') as file:
    		data = json.load(file)
    		data['number'] = data['number'] + 1
    		file.seek(0)
    		json.dump(data, file, indent=4)
    		file.truncate()


	prevName += 1
	newName += 1
  
print(str(count) + ' files duplicated')
