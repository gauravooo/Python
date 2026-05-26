# Program that takes an image as input and outputs the same image with a shirt on it. The program should be executed from the command line, taking two arguments: the name of the input file and the name of the output file. The program should check that the correct number of command-line arguments are provided, that the input file exists, and that both files have the same extension (either .jpg or .png). If any of these checks fail, the program should exit with an error message. If all checks pass, the program should open the input image, resize it to fit a shirt template, paste the shirt onto the image, and save the result as the output file.
import sys
from PIL import Image, ImageOps

if len(sys.argv) == 3:
    file1 = sys.argv[1]
    file2 = sys.argv[2]

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
else:
    sys.exit("Too many command-line arguments")

if file1.endswith((".png",".jpg",".jpeg")):
    if file1.split(".")[-1] == file2.split(".")[-1] :
        try:
            with Image.open(file1) as im1 , Image.open("shirt.png") as im2 :
                target_size = im2.size
                new_im1 = ImageOps.fit(im1, target_size)
                new_im1.paste(im2 , im2)
                new_im1.save(file2)

        except FileNotFoundError:
            sys.exit("Input does not exist")
    else:
        sys.exit("Input and output have different extensions")
else:
    sys.exit("Invalid output")
