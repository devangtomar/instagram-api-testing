file_read = open("more-celebs", 'r+')
celeb_list = []
for lines in file_read.readlines():
    length = len(lines)
    celeb_list.append(lines[1:length - 1])
print(celeb_list)
