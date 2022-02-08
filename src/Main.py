from PIL import Image
# Rearranges a very particular type of scrambled page
# Original image
image = Image.open('puzzle.jpg')

# records and edits the width and height of the original image
width = image.width
height = image.height - 2

# Removes white space at bottom of page
box = (0, 0, width, height)
image = image.crop(box)
solved_image = image.copy()

# width and height of 1/16 of the image
fourth_width = int(width / 4)
fourth_height = int(height / 4)

# list of images
image_list = []

# Crops the page into 16 parts and stores them into a list
for y in range(4):
    for x in range(4):
        box = (fourth_width * x, y * fourth_height, fourth_width * (x + 1), fourth_height * (y + 1))

        cropped_image = image.crop(box)

        image_list.append(cropped_image)

# Rearranges the page into the current format
for y in range(4):
    for x in range(4):
        position = (x * fourth_width, y * fourth_height)

        solved_image.paste(image_list[y + (x * 4)], position)

# Saves the edited image
solved_image.save('solved_puzzle.jpg')
solved_image.show()
