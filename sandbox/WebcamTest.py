import cv2

def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    cam.set(3,320)
    cam.set(4,240)

    while True:
        ret_val, img = cam.read()
        (h, w) = img.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center,-90,1)
        img = cv2.warpAffine(img, M, (w, h))
        
        cv2.imshow('My Webcam', img)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()

def main():
    show_webcam()

if __name__ == "__main__":
    main()
