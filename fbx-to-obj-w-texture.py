# run from command line : blender --background --python fbx-to-obj-w-texture.py
import bpy 
import sys
import os

def my_function(directory):
    print("Listing: " + directory)
    for file in os.listdir("."):
    	if file.endswith(".fbx"):
    		# output_obj_name = file
        	curr_fbx = os.path.join(directory, file)
        	print(curr_fbx)
    for file in os.listdir("."):
    	if file.endswith(".jpg") or file.endswith(".JPG") or file.endswith(".JPEG") or file.endswith(".jpeg"):
        	curr_img = os.path.join(directory, file)
        	print(curr_img)
    convert(curr_fbx, curr_img, directory)

def convert(fbx_path,texture_path,output_dir):
	
	bpy.ops.scene.new(type='EMPTY')
	bpy.ops.import_scene.fbx(filepath=fbx_path, axis_forward='-Z', axis_up='Y')

	try:
	    img = bpy.data.images.load(texture_path)
	except:
	    raise NameError("Cannot load image %s" % texture_path)

	mat = bpy.data.materials['Toon']
	tex = bpy.data.textures.new("Youtube-tex", 'IMAGE')
	tex.image = img
	slot = mat.texture_slots.add()
	slot.texture = tex

	
	outputpath = output_dir + "/test.obj"
	bpy.ops.export_scene.obj(filepath=outputpath, axis_forward='-Z', axis_up='Y')
	return

if __name__ == "__main__":
	path_to_fbx_file_folders = "/Users/alyssadavis/Documents/code/AC-Institute/input_fbx_files/"
	# path_to_obj_output_folder = "/Users/alyssadavis/Documents/code/AC-Institute/output_obj_files/"

	files = folders = 0

	# Get all the subdirectories of directory_to_check recursively and store them in a list:
	directories = [os.path.abspath(x[0]) for x in os.walk(path_to_fbx_file_folders)]
	directories.remove(os.path.abspath(path_to_fbx_file_folders)) # If you don't want your main directory included

	for i in directories:
		os.chdir(i)         # Change working Directory
		my_function(i)      # Run your function
