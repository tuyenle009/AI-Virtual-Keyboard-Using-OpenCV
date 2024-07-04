import cv2
from HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Set the width of the webcam feed
cap.set(3, 1280)  # 1280

# Set the height of the webcam feed
cap.set(4, 720)  # 720

# Initialize hand detector with a confidence threshold and max number of hands
detector = HandDetector(detectionCon=0.8, maxHands=2)


# Function to draw all buttons on the image
def drawAllButton(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        # Draw button rectangle
        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
        # Put button text
        cv2.putText(img, button.text, (x + 15, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 4)
    return img


# Function to draw a filled rectangle with text on the image
def drawRectangle(img, x, y, w, h, text, color=(0, 255, 0)):
    # Draw rectangle
    cv2.rectangle(img, (x, y), (x + w, y + h), color, cv2.FILLED)
    # Put text
    cv2.putText(img, text, (x + 15, y + 65),
                cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 4)


# Class to define a Button with position, size, and text
class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text


# List to hold all buttons
buttonList = []
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]
# String to write results
finalText = ""

# Initialize keyboard controller
keyboard = Controller()

# Create and position buttons based on the keys layout
for i in range(len(keys)):
    for x, key in enumerate(keys[i]):
        buttonList.append(Button([100 * x + 50, 100 * i], key))

# Main loop
while True:
    # Read image from webcam
    success, img = cap.read()
    # Flip image horizontally
    img = cv2.flip(img, 1)

    # Detect hands in the image
    hands, img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)

    # Draw all buttons on the image
    img = drawAllButton(img, buttonList)

    # If landmarks are detected
    if lmList:
        for button in buttonList:
            x, y = button.pos
            w, h = button.size
            # Check if the index finger tip is within the button area
            if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                # Highlight button on hover
                drawRectangle(img, x, y, w, h, button.text, (175, 0, 175))
                # Calculate distance between index finger tip and thumb tip
                l, _, _ = detector.findDistance(lmList[8], lmList[4], img)
                # If distance is less than 40, consider it as a click
                if l < 40:
                    keyboard.press(button.text)
                    drawRectangle(img, x, y, w, h, button.text, (0, 255, 0))
                    # Add the button text to the final text
                    finalText += button.text
                    sleep(0.5)

    # Draw the final text area
    cv2.rectangle(img, (50, 350), (600, 450), (175, 0, 175), cv2.FILLED)
    cv2.putText(img, finalText, (60, 430),
                cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 4)

    cv2.imshow("Image", img)
    if cv2.waitKey(25) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()