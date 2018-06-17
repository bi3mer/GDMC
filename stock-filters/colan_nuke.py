from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from pymclevel.box import Vector
from mcplatform import *

inputs = (
	("Nuke", "label"),
	("Creator: Colan Biemer", "label")
)

def draw_block(level, x, y, z, material):
	level.setBlockAt(x, y, z, material.ID)
	level.setBlockDataAt(x, y, z, 0)

# We do this last, so we can assume leaves have been destroyed and
# wood has been changed to coal
def fill_top_layer_with_obsidian(level, origin, size):
	for x in range(min(origin.x, size.x), max(origin.x, size.x)):
		for z in range(min(origin.z, size.z), max(origin.z, size.z)):
			# loop from the top until we reach a material that is not empty
			for y in reversed(range(min(origin.y, size.y), max(origin.y, size.y))):
				block = level.blockAt(x,y,z)
				if block != alphaMaterials.Air.ID and \
				   block != alphaMaterials.CoalBlock.ID and \
				   block != alphaMaterials.Lava.ID:
					draw_block(level, x, y, z, alphaMaterials.Obsidian)
					break

def replace_all_water_with_lava(level, origin, size):
	for x in range(min(origin.x, size.x), max(origin.x, size.x)):
		for y in range(min(origin.y, size.y), max(origin.y, size.y)):
			for z in range(min(origin.z, size.z), max(origin.z, size.z)):
				block = level.blockAt(x,y,z)

				if block == alphaMaterials.Water.ID or block == alphaMaterials.WaterActive.ID:
					draw_block(level, x, y, z, alphaMaterials.Lava)

def replace_all_trees_with_coal(level, origin, size):
	for x in range(min(origin.x, size.x), max(origin.x, size.x)):
		for y in range(min(origin.y, size.y), max(origin.y, size.y)):
			for z in range(min(origin.z, size.z), max(origin.z, size.z)):
				block = level.blockAt(x,y,z)

				if block == alphaMaterials.Wood.ID:
					draw_block(level, x, y, z, alphaMaterials.CoalBlock)
				elif block == alphaMaterials.Leaves.ID:
					draw_block(level, x, y, z, alphaMaterials.Air)

def perform(level, box, options):
	size = Vector(box.origin.x + box.size.x, box.origin.y + box.size.y, box.origin.z + box.size.z)

	replace_all_water_with_lava(level, box.origin, size)
	replace_all_trees_with_coal(level, box.origin, size)
	fill_top_layer_with_obsidian(level, box.origin, size)