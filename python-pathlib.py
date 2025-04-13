from pathlib import Path

p1 =  Path('files/abc.txt')
#p1 =  './files/abc.txt'
p2 =  Path('files/ghi.txt')
p3 =  Path('files')
print(type(p1))

if p1.exists():
    with open(p1, 'r') as file_p1:
        print(file_p1.read())

if not p2.exists():
    with open(p2, 'w') as file_p2:
        file_p2.write('content 3')
else:
    with open(p2, 'r') as file_p2:
        print(file_p2.read())

print(p1.name)
print(p1.stem)
print(p1.suffix)

print(p3.iterdir())
for item in p3.iterdir():
    print(type(item))
    print(item)

print(list(p3.iterdir()))