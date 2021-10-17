file_open = open("./celebs", 'r+')
celebs_list = []
for lines in file_open.readlines():
    if str(lines) != "\n":
        length = len(lines)
        celebs_list.append(lines[0:length - 1])

print(celebs_list)
