# run `python3 jpg_to_png_convertor.py Pokedex/ new/`

import sys
import os
from PIL import Image # importing Image from Pillow installed from pip3

# grab first and second argument
image_folder, output_folder = sys.argv[1], sys.argv[2]

# check if new/ exists, if not create it
if not os.path.exists(output_folder):
	os.makedirs(output_folder)

for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}{filename}')
	clean_name = os.path.splitext(filename)[0]
	img.save(f'{output_folder}{clean_name}.png', 'png')
	print('all done!')














# reads all files in a folder and gets all their names
# for file in [f for f in os.listdir('./Pokedex') if f.endswith('.jpg')]:
# 	print(file)