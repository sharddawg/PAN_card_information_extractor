import cv2
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Anish\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def rotate_image(image, angle):
    height, width = image.shape[:2]
    image_center = (width / 2, height / 2)
    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1)
    abs_cos = abs(rotation_mat[0, 0])
    abs_sin = abs(rotation_mat[0, 1])
    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)
    rotation_mat[0, 2] += bound_w / 2 - image_center[0]
    rotation_mat[1, 2] += bound_h / 2 - image_center[1]
    rotated_mat = cv2.warpAffine(image, rotation_mat, (bound_w, bound_h))

    return rotated_mat


def rotated_image(image):
    angle = int(
        input("If PAN card in the image is straight, input 0 degrees \n"
              "If PAN card in image is not straight, what angle should you rotate it anti clockwise so that it is? - "))
    rotated_image = rotate_image(image, angle)
    rotated_image = cv2.cvtColor(rotated_image, cv2.COLOR_RGB2GRAY)
    # rotated_image = cv2.resize(rotated_image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    th = cv2.adaptiveThreshold(rotated_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 23, 15)

    return th


def extract_information(image):
    text = pytesseract.image_to_string(image)
    pan_card_number = re.findall('([A-Z]{5}[0-9]{4}[A-Z])', text)
    dob = re.findall('([0-9]{2}/[0-9]{2}/[0-9]{4})', text)

    return [pan_card_number, dob]


if __name__ == "__main__":
    img = cv2.imread("Image path")
    image = rotated_image(img)
    pan_card_number, dob = extract_information(image)
    print(f"PAN card number is {pan_card_number} and Date Of Birth is {dob}")
