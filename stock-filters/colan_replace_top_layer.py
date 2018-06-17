from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *

inputs = (
	("Replace Top Layer", "label"),
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
		for z in range(min(origin.z, final_z), max(origin.z, final_z)):
			# loop from the top until we reach a material that is not empty
			for y in reversed(range(min(origin.y, final_y), max(origin.y, final_y))):
				if level.blockAt(x,y,z) != alphaMaterials.Air.ID:
					draw_block(level, x, y, z, material)
					break

def perform(level, box, options):
	fill_box(level, box.origin, box.size, options["Material"])