import cv2
import numpy
import sys
import os

def find_inconsistencies(image_name):
    img = cv2.imread(image_name)
    height, width = img.shape[0:2]
    for i in range(height):
        for j in range(width):
            if img[i,j,0] % 255 != 0 or img[i,j,1] % 255 != 0 or img[i,j,2] % 255 != 0:
                # print(img[i,j])
                return False
            else: 
                # print("OK:" + str(img[i,j]))
                pass

    return True

def encrypt(img):
    height, width = img.shape[0:2]
    ret = numpy.ndarray(img.shape)
    # print(img.shape, ret.shape)
    for i in range(height):
        for j in range(width):
            if img[i,j,0] == 0:
                # print(str((i, j)) + "is 0")
                if i%2 == 0:
                    if j%2 == 0: pixel = 0
                    else: pixel = 255
                else:
                    if j%2 == 1: pixel = 0
                    else: pixel = 255
            else:
                # print(str((i, j)) + "is 255")
                if i%2 == 1:
                    if j%2 == 0: pixel = 0
                    else: pixel = 255
                else:
                    if j%2 == 1: pixel = 0
                    else: pixel = 255

            ret[i,j,0] = pixel
            ret[i,j,1] = pixel
            ret[i,j,2] = pixel
            # print(i, j, pixel)

    return ret

def write_text(text):
    img = numpy.zeros((512,512,3), numpy.uint8)

    # Write some Text

    font                   = cv2.FONT_HERSHEY_PLAIN
    bottomLeftCornerOfText = (10,512//2)
    fontScale              = 1
    fontColor              = (255,255,255)
    lineType               = 1

    cv2.putText(img, text, 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)

    return img


if __name__ == "__main__":
    # TEXT_MODE = False
    # # print(find_inconsistencies("cannyLena.png"))
    # # print(find_inconsistencies("cannyLena.bmp"))

    # if TEXT_MODE:
    #     print("Write some text to output:")
    #     text = input()
    #     msg = write_text(text)
    #     img = encrypt(msg)
    #     cv2.imwrite('message.png', img)
    # else:
    #     img = cv2.imread("Porsche.bmp")
    #     ret = encrypt(img)
    #     cv2.imwrite("Porsche_ret.bmp", ret)

    if len(sys.argv) == 1 or len(sys.argv) > 3:
        print("usage: " + str(sys.argv[0]) + " input-name [output-name]")
        exit()
    if len(sys.argv) == 2:
        output_name = os.path.splitext(sys.argv[1])[0] +"_output.png"
    else:
        output_name = sys.argv[2]

    input_name = sys.argv[1]
    img = cv2.imread(input_name)
    ret = encrypt(img)    
    cv2.imwrite(output_name, ret)

