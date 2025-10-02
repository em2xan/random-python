from PIL import Image
from random import randint

img = Image.open("/Users/em2xan/Desktop/Pics/CS Vault.jpeg")
img = img.convert("RGB")
w, h = img.size

def coding():
    password = input("whats the password: ")
    counter = 0
    for x in range(0,w,100):
        for y in range(0,h,100):
            if counter < len(password):
                val = ord(password[counter])
                if counter %2 == 0:
                    img.putpixel((x,y), (val, randint(0,255), val))
                    counter += 1
                else:
                    img.putpixel((x,y), (randint(0,255), val, randint(0,255)))
                    counter += 1
            else:
                break
    img.save("/Users/em2xan/Desktop/Pics/CS Vault--OUT.jpeg")
    print("Saved!")

coding()
