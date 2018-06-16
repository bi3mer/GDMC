from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from pprint import pprint


inputs = (
	("Replace Eight Corners", "label"),
	("Material", alphaMaterials.CoalBlock),
	("Creator: Colan Biemer", "label")
)


def draw_block(level, x, y, z, material):
	level.setBlockAt(x, y, z, material.ID)
	level.setBlockDataAt(x, y, z, 0)

def perform(level, box, options):
	material = options["Material"]

	draw_block(level, box.origin.x, box.origin.y, box.origin.z, material)
	draw_block(level, box.origin.x + box.size.x, box.origin.y, box.origin.z, material)
	draw_block(level, box.origin.x, box.origin.y + box.size.y, box.origin.z, material)
	draw_block(level, box.origin.x, box.origin.y, box.origin.z + box.size.z, material)
	draw_block(level, box.origin.x + box.size.x, box.origin.y + box.size.y, box.origin.z, material)
	draw_block(level, box.origin.x + box.size.x, box.origin.y, box.origin.z + box.size.z, material)
	draw_block(level, box.origin.x, box.origin.y + box.size.y, box.origin.z + box.size.z, material)
	draw_block(level, box.origin.x + box.size.x, box.origin.y + box.size.y, box.origin.z + box.size.z, material)