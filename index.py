import os
num_session=input('enter session :')
def list_files(directory):
  files = []
  for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
      files.append(filename)
  return files

current_dir = os.path.dirname(__file__)
files = list_files(current_dir)
print(files)
files.remove('index.py')
j=1
for i in files:
    i=str(i)
    format=i.split('.')[1]
    os.system(f'ren "{i}" "{num_session} {j}.{format}"')
    j+=1






















