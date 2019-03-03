from pathlib import Path
import namelist as nl
import re
import os
import shutil

# Directory with files to sort
file_directory = 'CW2MS/'

# Method to find out the numbers and names of files in  file_directory


def existing_files(directory_of_file):
    entries = Path(directory_of_file)
    file_list = []
    for i in entries.iterdir():
        file_list.append(i.name)
    return file_list


directoryList = existing_files(file_directory)  # creates a list of filenames in file directory


# print(directoryList)
sections = nl.classes  # references 2D List which contains student names

section_count = 0
match_count = 0  # file matches found in directory
total_count = 0  # total names in the classes list
check_dict = {}  # stores names and their corresponding files names
for section in sections:
    section_count += 1
    for each in section:
        pattern = re.compile(r'(?i).*{name}.*\.pdf'.format(name=each))
        found = list(filter(pattern.search, directoryList))
        if len(found) == 1:
            item = found[0]
            # print(match_count, "Match Found", "C{s_count} ----"
            # .format(s_count=section_count), each, "----File Name:", item)
            match_count += 1
            check_dict[each] = [item, 'C{s_count}'.format(s_count=section_count)]
        else:
            check_dict[each] = ['', 'C{s_count}'.format(s_count=section_count)]
        total_count += 1

print("Total names in the list", total_count)
print("Files found", match_count)
        

# to copy files to another directory

file = open("notfound.txt", "a")
nf = 1
for name, s_file in check_dict.items():
    if s_file[0] == '':
        file.write(str(nf)+" "+name+"\n")
        nf += 1
    else:
        if not os.path.exists(s_file[1]):
            os.makedirs(s_file[1])
        try:
            shutil.copy("{fdr}{file_name}".format(fdr=file_directory, file_name=s_file[0]), s_file[1])
        except FileNotFoundError as e:
            print(e)
file.close()
print("----------Program now terminating----------------")
