from logicalConjunctions import *
from inputController import *
from operators import *

inc = inputController('P', 'S', 'A', 'E')
inc.inputStream()

'''
rain = symbol("rain")
sun = symbol("sun")

moon = symbol("moon")
cloud = symbol("cloud")

earth = symbol("earth")
sky = symbol("sky")

air = symbol("air")

ocean = symbol("ocean")
lake = symbol("lake")

kb = knowledgeBase()
kb.appendAdd(rain, sun)
kb.appendOr(moon, cloud)
kb.appendImplication(sky, earth)
kb.appendNot(air)
kb.appendbiDirectionalImplication(lake, ocean)
kb.printFunction()

s = kb.modelCheckAlgorithm(cloud)
print(s)
'''
