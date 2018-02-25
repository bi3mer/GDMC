from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from pprint import pprint


inputs = (
	("Replace All", "label"),
	("Material", alphaMaterials.CoalBlock),
	("Creator: Colan Biemer", "label")
)

def draw_block(level, x, y, z, material):
	level.setBlockAt(x, y, z, material.ID)
	level.setBlockDataAt(x, y, z, 0)

def fill_box(level, origin, size, material):
	final_x = origin.x + size.x
	final_y = origin.y + size.y
	final_z = origin.z + size.z

	for x in range(min(origin.x, final_x), max(origin.x, final_x)):
		for y in range(min(origin.y, final_y), max(origin.y, final_y)):
			for z in range(min(origin.z, final_z), max(origin.z, final_z)):
				draw_block(level, x, y, z, material)

def perform(level, box, options):
	fill_box(level, box.origin, box.size, options["Material"])