# Pan_card_information_extractor
Extracts PAN card number and date of birth from image of PAN card. Google's Tesseract OCR engine, pytesseract, OpenCV, and regular expressions were used.

Few notes :- 
1. Gave the user capability to rotate the image if the pan card in the image is not straight.
2. For better OCR, adaptive thresholding is used so that better results can be achieved using pytesseract (When card is sufficiently big in image). Tweaking the threshhold values can better or worsen results. Turning adaptive threshholding off can better or worsen results. 
3. Higher the resolution and clarity of the input image, better the results.
4. Resizing the image in case the pan card in the image is far and not very clear can provide better results. The line which resizes the image is in the code but commented out.

Alternate method and complications :- 
1. Using multi scale template matching, we could find where "Permanent Account Number Card" and "Date of Birth" is written. 
2. Using the 4 points we get after template matching, we can shift the points (bottom left and right point) downward to get the actual PAN card number and date of birth.
3. After getting the updated points, we can pass only that area of the image for OCR. This way we won't get redundant information and gibberish.
4. Problem 1 - Apparently there are a lot of different types of PAN cards which have differently written "Permanent Account Number" and "Date of Birth". So a singular template cannot be used for all of them.
5. Problem 2 - After getting the 4 points during template matching, the amount by which we have to shift the points downward is hard to determine because we don't know how big the PAN card is in the image. We could try edge detection using canny algorithm and 4 point transform to get a birds eye view so that all cards are the same size but edge detection is very unreliable and won't work a lot of the times.
