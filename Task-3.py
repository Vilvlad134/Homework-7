import os

def create_total_dict():
    files_dir = 'Files'
    work_dir = os.path.join(os.getcwd(), files_dir)
    file_list = ['1.txt', '2.txt', '3.txt']
    total_dict = {}
    for file in file_list:
        with open(os.path.join(work_dir, file), 'r', encoding='utf-8') as cur_file:
            total_dict[file] = cur_file.readlines()
    return total_dict

def sort_dict():
    var_dict = create_total_dict()
    sorted_list = sorted(var_dict, key=lambda key: len(var_dict[key]))
    sort_total_dict = {}
    for key in sorted_list:
        sort_total_dict[key] = var_dict[key]
    return sort_total_dict

def save_file():
    files_dir = 'Files'
    work_dir = os.path.join(os.getcwd(), files_dir)
    file = os.path.join(work_dir, 'TotalFile.txt')
    var_dict = sort_dict()
    with open(file, 'w', encoding='utf-8') as cur_file:
        for key in var_dict.keys():
            cur_file.write(f'{key}\n')
            cur_file.write(f'{(len(var_dict[key]))}\n')
            for elem in var_dict[key]:
                cur_file.write(elem)
            cur_file.write('\n')

if __name__ == "__main__":
    save_file()