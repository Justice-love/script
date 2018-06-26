import os
import sys

if len(sys.argv) < 2:
	print "args error:", sys.argv
	sys.exit(1)

fileName = sys.argv[1]
path = '/Users/xuyi/Desktop/'
fileType = ('jpg', 'JPG', 'jpeg', 'mp4', 'MOV')
delimiter = '.'


def findFile():
    filterFiles = filter(lambda name: name.endswith(fileType), os.listdir(path))
    for index, name in enumerate(filterFiles):
        newName = '%s%s%s' % (sys.argv[1] , index + 1 , name[name.index(delimiter):])
        print '%s rename to %s' % (name, newName)
        os.rename(path + name, path + newName)

findFile()
