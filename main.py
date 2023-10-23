from io import BytesIO

import PIL
from PIL import Image
import numpy as np
import requests
import cv2

def convertToGrayAPI(img):
    API_ENDPOINT = 'https://h6s7d6jvv5.execute-api.ap-southeast-2.amazonaws.com/dev'

    is_success, im_buf_arr = cv2.imencode(".png", img)
    byte_im = im_buf_arr.tobytes()

    r = requests.post(url=API_ENDPOINT, data=byte_im)

    try:
        img_ = Image.open(BytesIO(r.content))
        return np.asarray(img_)
    except PIL.UnidentifiedImageError as e:
        print(f"Error opening image: {e}")
        return None  # Handle the error, e.g., return None or an error message

def convertToGray(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray

if __name__ == "__main":
    img_path = './test_img_bgr.png'
    img = cv2.imread(img_path)

    img_gray = convertToGrayAPI(img)

    if img_gray is not None:
        cv2.imwrite('./test_img_gray.png', img_gray)
    else:
        print("Conversion to gray failed. Check the image format received from the API.")
