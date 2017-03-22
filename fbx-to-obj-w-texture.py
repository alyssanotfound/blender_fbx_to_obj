import bpy 
import sys
import os

path_to_fbx_file_folders = "/Users/alyssadavis/Documents/code/AC-Institute/input_fbx_files"

files = folders = 0

argv = sys.argv 
argv = argv[argv.index("--") + 1:] # get all args after "--"

fbx_in = argv[0] 
obj_out = argv[1]

# for _, dirnames, filenames in os.walk(path_to_fbx_file_folders):
#   # ^ this idiom means "we won't be using this value"
#   	# print(filenames)
  	
#     files += len(filenames)
#     folders += len(dirnames)
#     print(dirnames)
#     print(filenames)

# print(folders)

def my_function(directory):
    print("Listing: " + directory)
    for file in os.listdir("."):
    	if file.endswith(".fbx"):
        	curr_fbx = file
        	print(curr_fbx)
    for file in os.listdir("."):
    	if file.endswith(".jpg") or file.endswith(".JPG") or file.endswith(".JPEG") or file.endswith(".jpeg"):
        	curr_img = file
        	print(curr_img)
        # elif file.endswith(".jpg"):
        # 	print(file)
        # else:
    # print("\t-" + "\n\t-".join(os.listdir("."))) # List current working directory

def convert(i,o):
	
	bpy.ops.import_scene.fbx(filepath=fbx_in, axis_forward='-Z', axis_up='Y')

	realpath = os.path.expanduser(path_to_fbx_files + 'texture.jpg')
	try:
	    img = bpy.data.images.load(realpath)
	except:
	    raise NameError("Cannot load image %s" % realpath)

	mat = bpy.data.materials['Toon']
	tex = bpy.data.textures.new("Youtube-tex", 'IMAGE')
	tex.image = img
	slot = mat.texture_slots.add()
	slot.texture = tex

	bpy.ops.export_scene.obj(filepath=obj_out, axis_forward='-Z', axis_up='Y')

	# to call in command line: blender --background --python fbx-to-obj-w-texture.py
	# -- test.fbx test.obj

	return

# Get all the subdirectories of directory_to_check recursively and store them in a list:
directories = [os.path.abspath(x[0]) for x in os.walk(path_to_fbx_file_folders)]
directories.remove(os.path.abspath(path_to_fbx_file_folders)) # If you don't want your main directory included

for i in directories:
	os.chdir(i)         # Change working Directory
	my_function(i)      # Run your function

# if __name__ == "__main__":
# 	for x in range(0, folders):
# 		print("folder number")

	# print(folders)
    # convert(fbx_in, obj_out)