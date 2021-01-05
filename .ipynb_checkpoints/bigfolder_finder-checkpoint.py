import os
import pickle

"""module for traversing a directory structure and finding the largest directories"""

def size(directory, size_dict, max_size=1e500):
    try:
        dirs = [name for name in os.listdir(directory)
                if os.path.isdir(os.path.join(directory, name)) 
                and not name[0] =='.' 
                and not os.path.islink(os.path.join(directory, name))]
    except (PermissionError, FileNotFoundError, OSError) as e:
        print(e)
        return 0, size_dict
    if len(dirs) == 0:
        try:
            files_size = sum([os.path.getsize(os.path.join(directory, f)) for f in os.listdir(directory)])>>20
        except (FileNotFoundError, PermissionError, OSError) as e:
            print(e)
            files_size = 0
        if files_size > max_size:
            size_dict[directory] = files_size
            return 0, size_dict
        return files_size, size_dict
    else:
        for root, dirs, files in os.walk(directory):
            files = [f for f in files if not f[0] == '.']
            subdirs = [d for d in dirs if not d[0] == '.']
            if len(subdirs) ==0:
                return 
            dirs[:] = subdirs

            try:
                fsize = sum([os.path.getsize(os.path.join(root,f)) for f in files])>>20
            except (FileNotFoundError, PermissionError, OSError) as e:
                print(e)
                fsize = 0
            sizes, _ = zip(*[size(os.path.join(root,d), size_dict, max_size) for d in subdirs])
            dirsize = sum(sizes)
            all_size = fsize+dirsize
            if all_size > max_size:
                size_dict[directory] = all_size
                return 0, size_dict
            return all_size, size_dict

if __name__ == "__main__":
    size_dict = {}
    folder_to_scour = '/home/disk/eos4'
    _ = size(folder_to_scour, size_dict, max_size=10<<10) # 10 GB
    with open('/home/disk/p/jkcm/dump/testfile.pickle', 'wb') as f:
        pickle.dump(size_dict, f)
