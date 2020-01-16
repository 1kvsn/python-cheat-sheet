from PIL import Image, ImageFilter

# img = Image.open('./Pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR )
# filtered_img.save('blurred.png', 'png')  # name of new file and the new format

# -------------

filtered_img = img.convert('L') # convert to different formats
# filtered_img.save('greyscaled.png', 'png')
# filtered_img.show() # shows the image

# crooked = filtered_img.rotate(180)
# crooked.save("rotated.png", 'png')

# resize = filtered_img.resize((300, 300)) # notice double parenthesis inside
# resize.save('resized.png', 'png')

# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save("cropped.png", 'png')

# img = Image.open('./astro.jpg')
# img.thumbnail((400, 400)) # doesn't return new image. Modifies existing one. Hence not saved in a new variable
# thumbnail maintains the aspect ratio. Output will be within 400 x 400 and will never go beyond what is specified.
# print(img.size)
# img.save('thumbnail.jpg')

# print(dir(img)) # all available commands
# print(img) # image object
# print(img.format) # image format #jpg
# print(img.size) # image size #(640,640)
# print(img.mode) # image mode #RGB

# -----------------------------------------------------------

