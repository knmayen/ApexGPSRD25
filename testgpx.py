file = open(r'C:\Users\knmay\OneDrive\Desktop\gps\data.txt', 'r')

lines = file.readlines()

for line in lines:
    print(line)

file.close()
