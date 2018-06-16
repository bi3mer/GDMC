from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *

inputs = (
    ("Selection Material Counter", "label"),
    ("Creator: Colan Biemer", "label")
)

def perform(level, box, options):
    final_x = box.origin.x + box.size.x
    final_y = box.origin.y + box.size.y
    final_z = box.origin.z + box.size.z

    materials = {}

    for x in range(min(box.origin.x, final_x), max(box.origin.x, final_x)):
        for y in range(min(box.origin.y, final_y), max(box.origin.y, final_y)):
            for z in range(min(box.origin.z, final_z), max(box.origin.z, final_z)):
                material = level.blockAt(x,y,z)

                if material not in materials:
                    materials[material] = 0

                materials[material] += 1

    print "Material Counts"
    for key in materials:
        print "\t" + str(key) + ": " + str(materials[key])