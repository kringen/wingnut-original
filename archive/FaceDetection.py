import cv2
import base64

encodedImages = []

def getImage(outputFileName):
    #Get the picture
    video_capture = cv2.VideoCapture(0)
    #video_capture.set(3,320)
    #video_capture.set(4,240)

    # Capture a frame
    ret_val, img = video_capture.read()
    #  Scale size to 320 X 240
    (h, w) = img.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center,-90,1)
    img = cv2.warpAffine(img, M, (w, h))

    #Load a cascade file for detecting faces
    face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')

    #Convert to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #Look for faces in the image using the loaded cascade file
    faces = face_cascade.detectMultiScale(
             gray,
            scaleFactor=1.05,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )

    print "Found "+str(len(faces))+" face(s)"

    for idx,(x,y,w,h) in enumerate(faces):
        #cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
        tmpImg = img[y:y + h, x:x + w]
        pngImg = cv2.imencode(".png",tmpImg)[1]
        encodedImages.append(encodeImage(pngImg))
        encodedFile = open("encoded.txt", "w")
        encodedFile.write(encodeImage(pngImg))
        #cv2.imwrite("cropped" + str(idx) + ".jpg",tmpImg)
    print encodedImages
    #Save the result image
    #cv2.imwrite(outputFileName,gray)
    #encodedFile = open("encoded.txt", "w")
    #cnt = cv2.imencode(".png",gray)[1]
    #encodedFile.write(encodeImage(cnt))
    #print(encodeImage(gray))

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

def encodeImage(image):
    encoded = base64.b64encode(image)
    return encoded

if __name__ == "__main__":
    getImage('result.jpg')
