import json


f = open('./Dataset/Data_Subset/subset.json')

data = json.load(f)

print('\n')
k = 0
for item in data:
    print(data[k])
    k+=1
print('\n')

f.close()