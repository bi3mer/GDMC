from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from pymclevel.box import Vector
from mcplatform import *
from tqdm import tqdm

inputs = (
    ("Selection Material Counter", "label"),
    ("Creator: Colan Biemer", "label")
)

DATA_DIRECTORY = "/home/colanbiemer/work/projects/mcedit_data/extracted_data/"
RESULT_FILE = DATA_DIRECTORY + "results.csv"
DATA_FILE = "data_"
EXTENSION = ".csv"

def calculate_box_size(index):
    if index <= 1:
        return 8

    return calculate_box_size(index - 1) + (4 * 2 * index)

def calculate_width(index):
    if index <= 1:
        return 3

    return calculate_width(index - 1) + 2

#  __ ____ ____ __ _  _ __ ____ ____    ____ _  _ __ ____     __  ____  __  ____ 
#  /  (  _ (_  _(  ( \/ (  (__  (  __)  (_  _/ )( (  / ___)   / _\/ ___)/ _\(  _ \
# (  O ) __/ )(  )(/ \/ \)( / _/ ) _)     )( ) __ ()(\___ \  /    \___ /    \) __/
#  \__(__)  (__)(__\_)(_(__(____(____)   (__)\_)(_(__(____/  \_/\_(____\_/\_(__)  
def build_data(level, point, size_index):
    min_x = point.x - size_index
    min_y = point.y - size_index
    min_z = point.z - size_index

    max_x = point.x + size_index
    max_y = point.y + size_index
    max_z = point.z + size_index

    data = []

    for x in xrange(min_x, max_x + 1):
        for y in xrange(min_y, max_y + 1):
            for z in xrange(min_z, max_z + 1):
                if x == point.x and y == point.y and z == point.z:
                    continue

                data.append(level.blockAt(x,y,z))

    return data

# @todo: handle distance from the ground and add that to each set for a toal
#        of 12 datasets
def perform(level, box, options):
    data_set_size = 6

    final_x = box.origin.x + box.size.x
    final_y = box.origin.y + box.size.y
    final_z = box.origin.z + box.size.z

    min_x = min(box.origin.x, final_x)
    max_x = max(box.origin.x, final_x)
    min_y = min(box.origin.y, final_y)
    max_y = max(box.origin.y, final_y)
    min_z = min(box.origin.z, final_z)
    max_z = max(box.origin.z, final_z)

    point = None

    level_data = [[] for i in xrange(data_set_size)]
    results = []

    print "analyzing data"
    for x in tqdm(xrange(min_x, max_x)):
        for y in xrange(min_y, max_y):
            for z in xrange(min_z, max_z):
                point = Vector(x, y, z)
                results.append(level.blockAt(x, y, z))

                for size_index in xrange(data_set_size):
                    level_data[size_index].append(build_data(level, point, size_index + 1))

    print "writing data to file"
    for i in tqdm(xrange(data_set_size)):
        data_file = DATA_DIRECTORY + DATA_FILE + str(i) + EXTENSION
        result_file = DATA_DIRECTORY + RESULT_FILE + str(i) + EXTENSION

        data = level_data[i]

        with open(data_file, "a") as myfile:
            for line in data:
                myfile.write(','.join(str(x) for x in line) + "\n")

    with open(RESULT_FILE, "a") as myfile:
        for result in results:
            myfile.write(str(result) + "\n")

    print "completed"

