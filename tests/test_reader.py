"""Check the outputs of all functions in the reader module"""

#pylint: disable=import-error
#pylint: disable=wrong-import-position

#------------------------------Imports---------------------------------

import os
import sys
ROOT = os.path.dirname(__file__).replace("\\tests","\\")
sys.path.append("".join([ROOT, r"chatbots\components"]))
from reader import read_scenes, read_patterns

#------------------------------Unit test-------------------------------

tempA = read_scenes("locked_room", "question")
tempB = read_patterns("question")

print(tempA)
print(tempB)
