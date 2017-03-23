# run from command line : blender --background --python fbx-to-obj-w-texture.py
import bpy 
import sys
import os

def find_fbx(directory):
    print("Listing: " + directory)
    for file in os.listdir("."):
    	if file.endswith(".fbx"):
        	curr_fbx_file = file
        	print(curr_fbx_file)
    for file in os.listdir("."):
    	if file.endswith(".jpg") or file.endswith(".JPG") or file.endswith(".JPEG") or file.endswith(".jpeg"):
        	curr_img = os.path.join(directory, file)
        	print(curr_img)
    # print("BEFORE CONVERTING")
    # print(curr_fbx_file)	
    # print(curr_img)
    convert(curr_fbx_file, curr_img, directory)

def convert(fbx_p,texture_path,output_dir):
	fbx_path = os.path.join(output_dir, fbx_p)
	base, ext = os.path.splitext(fbx_p)

	bpy.ops.scene.delete()
	bpy.ops.scene.new(type='EMPTY')
	bpy.ops.import_scene.fbx(filepath=fbx_path, axis_forward='-Z', axis_up='Y')

	try:
	    img = bpy.data.images.load(texture_path)
	except:
	    raise NameError("Cannot load image %s" % texture_path)

	mat = bpy.data.materials['Toon']
	print("TEX INFO")
	print(bpy.data.textures)
	tex = bpy.data.textures.new(base, 'IMAGE')
	tex.image = img
	slot = mat.texture_slots.add()
	slot.texture = tex
	print(slot.texture)
	
	outputpath = path_to_fbx_output_folder + base + ".fbx"
	bpy.ops.export_scene.fbx(filepath=outputpath, axis_forward='-Z', axis_up='Y')
	return

if __name__ == "__main__":
	path_to_fbx_file_folders = "/Users/alyssadavis/Documents/code/AC-Institute/input_fbx_files/"
	path_to_fbx_output_folder = "/Users/alyssadavis/Documents/code/AC-Institute/output_fbx_files/"

	files = folders = 0

	# Get all the subdirectories of directory_to_check recursively and store them in a list:
	directories = [os.path.abspath(x[0]) for x in os.walk(path_to_fbx_file_folders)]
	directories.remove(os.path.abspath(path_to_fbx_file_folders)) # If you don't want your main directory included

	for i in directories:
		os.chdir(i)         # Change working Directory
		find_fbx(i)      
