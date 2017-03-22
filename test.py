import os

path = "/Users/alyssadavis/Documents/code/AC-Institute/input_fbx_files"
files = folders = 0

for _, dirnames, filenames in os.walk(path):
  # ^ this idiom means "we won't be using this value"
    files += len(filenames)
    folders += len(dirnames)

print "{:,} files, {:,} folders".format(files, folders)