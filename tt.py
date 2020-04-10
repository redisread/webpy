import os


img_path = "./static/images/"
r = [os.path.join(img_path,each) for each in os.listdir(img_path)]
print(r)