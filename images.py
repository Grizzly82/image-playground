from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
#filtered_img = img.filter(ImageFilter.EMBOSS)
#convert image to grey scale
filtered_img = img.convert('L')
#saved modiefied image
resize = filtered_img.resize((300 , 300))
resize.save("bigPika.png", "png")
filtered_img.save("blurPika.png", 'png')
filtered_img.show()