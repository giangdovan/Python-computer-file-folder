from pathlib import Path

root_dir = Path('files')
#root_dir = Path('D:\\Documents\\Learning\\Python\Automate Everything with Python\\Python - Computer File Folder\\files')


file_paths = root_dir.iterdir()
print(file_paths)
#print(list(file_paths)) #can not rename if un momment this line
print(Path.cwd())

for path in file_paths:
    new_filename = "new-" + path.stem + path.suffix
    print(new_filename)
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)