import zipfile
import sys
import StringIO
data = StringIO.StringIO(sys.stdin.read())
z = zipfile.ZipFile(data)
dest = sys.argv[1] if len(sys.argv) == 2 else '.'
z.extractall(dest)
