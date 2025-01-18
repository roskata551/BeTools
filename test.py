from PIL import Image  # To handle and process image files
import pytesseract  # For Optical Character Recognition
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust path as needed

image1 = Image.open("ScreenShots/TrueShot1.png")
image2 = Image.open("ScreenShots/TrueShot2.png")

true_odd1 = pytesseract.image_to_string(image1)
true_odd2 = pytesseract.image_to_string(image2)

print(true_odd1)
print(true_odd2)

# from PIL import Image, ImageFilter, ImageOps  # To handle and process image files
# import pytesseract  # For Optical Character Recognition
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust path as needed
# def raed_image:
#     image = Image.open(f"ScreenShots/{image_name}.png")
#     image = image.convert("L")  # Convert to grayscale
#     image = ImageOps.invert(image)  # Invert colors (if text is blue on white)
#     image = image.filter(ImageFilter.SHARPEN)  # Sharpen the image
#     image = image.resize((image.width * 3, image.height * 3), Image.Resampling.LANCZOS)  # Resize for better OCR
#     PSM 7 for single-line text; whitelist numbers and period.
#     custom_config = r'--psm 6 -c tessedit_char_whitelist=0123456789.'
#     text = pytesseract.image_to_string(image, config=custom_config)
#     return text
