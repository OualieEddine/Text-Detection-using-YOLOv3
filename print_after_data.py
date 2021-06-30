from IPython.display import Image
from google.colab.patches import cv2_imshow
import cv2
import os

def get_images(s):
    files = []
    exts = ['jpg', 'png', 'jpeg', 'JPG']
    for parent, dirnames, filenames in os.walk(s):
        for filename in filenames:
            for ext in exts:
                if filename.endswith(ext):
                    files.append(filename)
                    break
    print('Find {} images'.format(len(files)))
    return files

im_fn_list = get_images("imgs/")
to_out = get_images("out/")
for im_fn in im_fn_list:
  for i in to_out:
    if im_fn == i:
      im = cv2.imread("out/"+i)
      cv2_imshow(im)
  