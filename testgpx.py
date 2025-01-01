# import pickle

# file = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\data.txt", 'r')

# lines = file.readlines()

# for line in lines:
#     print(line)

# var = 'hello'
# pickle.dump(var, file)


# file.close()
# print('here')

# nfile = open(r"C:\Users\knmay\OneDrive\Documents\GitHub\ApexGPSRD25\data.txt", 'rb')
# db = pickle.load(nfile)
# for line in nfile.readlines():
#     print(lines)

# nfile.close()

# allRolls = dict()
# date = '2024-12-17'
# infoDict = {'driver' : 'Maggie'}
# tag = '2024-12-17-MB-Sol-1'
# # allRolls[date][infoDict['driver']][tag] = 'hello'
# allRolls[date] = dict( )
# allRolls[date][infoDict['driver']] = dict()
# allRolls[date][infoDict['driver']][tag] = 'hello'
# tag = '2024-12-17-MB-Sol-2'
# allRolls[date][infoDict['driver']][tag] = 'bye'
# date = '2024-12-18'
# allRolls[date] = dict( )
# allRolls[date][infoDict['driver']] = dict()
# allRolls[date][infoDict['driver']][tag] = 'hello'
# print(allRolls)
from rollInputUI import allRolls



def getAllTags(dict, tags = []):
    for key in dict:
        if type(dict[key]) != type(dict):
            for tag in dict:
                tags.append(tag)
            return tags
        else:
            tags =  getAllTags(dict[key], tags)
    return tags


def findRoll(dict, tag):
    for key in dict:
        if key == tag:
            return dict[key]
        elif type(dict[key]) == type(dict):
            solution = findRoll(dict[key], tag)
            if solution != None:
                return solution


print(findRoll(allRolls, '2024-12-17-LQ-Fir-4'))