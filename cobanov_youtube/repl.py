from PIL import Image
import glob
import os
import timm
import torch



def read_images_from_directory(image_directory: str) -> list :
    """
    > It takes a directory as input and returns a list of all the images in that directory
    :param image_directory: The directory where the images are stored
    :return: Alist of images
    """

    list_of_images = list()
    for ext in ("*.gif", "*.png", "*.jpg", "*.jpeg"):
        list_of_images.extend(
            glob.glob(os.path.join(image_directory, ext))
        )
    print(f"images found : {len(list_of_images)}")
    return list_of_images

def read_with_pil(list_of_images: list, resize = False) -> list :
    pil_images = list()
    for img_path in list_of_images:
        img = Image.open(img_path).convert("RGB")
        if resize:
            img.thumbnail((512,512))
        pil_images.append(img)
    return pil_images

def main():
    list_of_images = read_images_from_directory('./images/')
    pil_images = read_with_pil(list_of_images, resize = False)
    #model = timm.create_model('resnet_34', pretrained=True)

   # with torch.no_grad():
     #   for image


if __name__ == '__main__' :
    main()


