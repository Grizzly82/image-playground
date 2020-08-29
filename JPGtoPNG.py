import sys
import os
from pathlib import Path
from PIL import Image


#grab first and second argument 

img_folder = sys.argv[1]
output_folder = sys.argv[2]

#Created a new folder to save new images 
#check if new folder exist if not created it
newpath = (f'.\{output_folder}')
if not os.path.exists(newpath):
    os.makedirs(newpath)

#Get the current directory
cwd = os.getcwd()    
currentPath = cwd + str(f'\{img_folder}')

#loop through Pokedex and 
# convert images to png 
# Save them to the folder 
paths = Path(currentPath).glob('**/*.jpg')
for path in paths:
    # because path is object not string
    path_in_str = str(path)
    filename = os.path.basename(path_in_str)
    (fn , ext) = os.path.splitext(filename)
    img = Image.open(path_in_str)
    img.save(newpath + "\\" + fn + ".png","png")
    
