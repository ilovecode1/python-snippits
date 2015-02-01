#Found at http://stackoverflow.com/questions/691946/short-and-useful-python-snippets by John Feminella

import zipfile

z = zipfile.ZipFile('my-archive.zip', 'w', zipfile.ZIP_DEFLATED)
startdir = "/home/johnf"
for dirpath, dirnames, filenames in os.walk(startdir):
  for filename in filenames:
    z.write(os.path.join(dirpath, filename))
z.close()
