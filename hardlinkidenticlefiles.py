#Found at http://stackoverflow.com/questions/691946/short-and-useful-python-snippets by rmmh

import os
import hashlib

dupes = {}

for path, dirs, files in os.walk(os.getcwd()):
    for file in files:
        filename = os.path.join(path, file)
        hash = hashlib.sha1(open(filename).read()).hexdigest()
        if hash in dupes:
            print 'linking "%s" -> "%s"' % (dupes[hash], filename)
            os.rename(filename, filename + '.bak')
            try:
                os.link(dupes[hash], filename)
                os.unlink(filename + '.bak')
            except:
                os.rename(filename + '.bak', filename)
            finally:
        else:
            dupes[hash] = filename
