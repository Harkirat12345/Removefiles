import os
import shutil
import time
path = '/Applications/Harkirat white hat jr/Python/class 99/tempFolder'
days=30
seconds=time.time()-(days*24*60*60)
if os.path.exists(path):
    for root_folder,folder,files in os.walk(path):
        if seconds>=get_file_or_folder_age(root_folder):
            remove_folder(root_folder)
            delted_folder_count+=1
            break
        else:
            for folder in folders:
                folder_path=os.path.join(root_folder,folder)
                if seconds>= get_file_or_folder_age(folder_path):
                    remove_folder(folder_path)
                     delted_folder_count+=1
            for file in files:
                folder_path=os.path.join(root_folder,folder)
                 if seconds>= get_file_or_folder_age(folder_path):
                     remove_folder(folder_path)
                      delted_folder_count+=1
        else:
            if seconds >= get_file_or_folder_age(path):
                	remove_file(path)
				deleted_files_count += 1 
else:
    print("path")
print("total folders delted:delted_folder_count")
print("total files delted: delted_files_count")

def remove_file(path):
    def remove_file(path):
	if not os.remove(path):
        print(path:"Removed successfully")

	else:
		print("Unable to delete the "+path)
              



                
        
# This will create a properly organized
# list with all the filename that is
# there in the directory
list_of_files = os.listdir(path)
# This will go through each and every file
print(list_of_files)
for file in list_of_files:
    name, ext = os.path.splitext(file)
    print(name+'--'+ext)
     # This is going to store the extension type
    ext = ext[1:]
    print(ext)
    # This forces the next iteration,
     # if it is the directory
    if ext == '':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)