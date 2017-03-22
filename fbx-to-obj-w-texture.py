import bpy 
import sys
import os

path_to_fbx_files = "/Users/alyssadavis/Documents/code/AC-Institute/"

def convert():
	argv = sys.argv 
	argv = argv[argv.index("--") + 1:] # get all args after "--"

	fbx_in = argv[0] 
	obj_out = argv[1]

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

	# bpy.ops.object.select_all(action='DESELECT')
	# bpy.context.space_data.context = 'TEXTURE' 
	# bpy.ops.texture.new()
	# bpy.ops.image.open(filepath="/Users/alyssadavis/Documents/code/AC-Institute/texture.jpg", directory="/Users/alyssadavis/Documents/code/AC-Institute/", files=[{"name":"texture.jpg","name":"texture.jpg"}], relative_path=True, show_multiview=False)

	bpy.ops.export_scene.obj(filepath=obj_out, axis_forward='-Z', axis_up='Y')

	# to call in command line: blender --background --python fbx-to-obj-w-texture.py
	# -- test.fbx test.obj

	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
	# bpy.ops.import_scene.fbx() 
	# bpy.ops.texture.new() 
	# bpy.ops.image.open() 
	# bpy.ops.export_scene.obj()
	return


if __name__ == "__main__":
    convert()