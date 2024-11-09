import os

file = "PMC000xxxxxx/PMC176545.txt"

def open_file_from_folder(folder):
    
    files = []
    for root, dirs, files in os.walk(folder):
        i = 0
        for file in files:
            i += 1
            if i == 100:
                break
            else:
                files.append(f"{file}")
    print(len(files))
    return files

def sanitize_data_from_txt(file):
    with open(file, 'r', encoding='latin-1') as f:
        lines = f.readlines()
    data = ""
    for line in lines:
        if line.startswith("====") or line == "\n" or line =="":
            continue
        else:
            data += line
    return data.strip().replace("\n", " ")

def sort_data_into_list():
    data_list = []
    file_list = open_file_from_folder("PMC000xxxxxx")
    print(file_list[3])
    for file in file_list:
        data = sanitize_data_from_txt(f"PMC000xxxxxx/{file}")
        data_list.append(data)
    print(len(data_list))
    return data_list
        
with open("datalist.txt", 'w', encoding='latin-1') as f:
    data = sort_data_into_list()
    for d in data:
        f.write(d + "\n")