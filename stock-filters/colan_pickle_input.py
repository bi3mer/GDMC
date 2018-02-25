'''
The only purpose of this is to take the input of the perform function
and pickle them so I can run code elsewhere to get a handle of the 
format and what I should be expecting. 

- Colan
'''

from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
import pickle


def pickle_object(obj, path):
	f = open(path, 'w')
	pickle.dump(obj, f)
	f.close()

def perform(level, box, options):
	# I know this is bad practice but it isn't meant to be used by 
	# anyone else, so please let it slide if you see this
	pickle_destination = "/home/colanbiemer/work/projects/GDMC/pkl/"

	# pickle_object(level,   pickle_destination + "/level.pkl")
	pickle_object(box,     pickle_destination + "/box.pkl")
	pickle_object(options, pickle_destination + "/options.pkl")