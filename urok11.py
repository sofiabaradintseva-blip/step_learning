import cv2
from PIL import Image

image_path = "tmp/cbbd205bf39e9e3a887799e024b70d66.jpg"
#cascade_path = cv2.data.haarcascades + "haarcascade_frontalcatface_extended.xml"
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
cat_face_cascade = cv2.CascadeClassifier(cascade_path)
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)
cat = Image.open(image_path)
glasses = Image.open("tmp/pngimg.com - glasses_PNG54356.png")
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")
for (x, y, w, h) in cat_face:
    glasses = glasses.resize((w, int(h/3)))
    cat.paste(glasses, (x, int(y+h/4)), glasses)
    cat.save("tmp/cat_with_glasses1.png")
    cat_with_glasses = cv2.imread("tmp/cat_with_glasses1.png")
    cv2.imshow("cat_with_glasses", cat_with_glasses)
    cv2.waitKey()
