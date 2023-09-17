#argv[1] foldername of existing images
#argv[2] new folder to put the converted images

import os, sys
from PIL import Image

def JPG_to_PNG_converter(src_im_folder,dest_folder):

    """converts x.jpg images in src_im_folder to x.png and stores new images in dest_folder"""

    # create the new directory if it does not exist
    try:
        os.makedirs(dest_folder)
    except FileExistsError:
        pass

    new_ext = 'png'

    # get image file names
    for im_file_name in os.listdir(src_im_folder):

        # create image obj
        image = Image.open(src_im_folder + im_file_name)

        # update the name of the image file with new extension
        im_file_name = im_file_name[:-3] + new_ext

        image.save(dest_folder + im_file_name,new_ext)


if __name__ == "__main__":
    # get path of image data
    source_folder = sys.argv[1]

    # get path of new directory to store the images
    dest_folder = sys.argv[2]

    JPG_to_PNG_converter(source_folder,dest_folder)
