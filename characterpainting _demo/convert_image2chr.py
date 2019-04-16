#author: hanshiqiang365 （微信公众号：韩思工作室）

import cv2 as cv

ascii_char = list(r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
char_len = len(ascii_char)

frame = cv.imread("resources/fu.png")

img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

img_resize = cv.resize(img_gray, (int(img_gray.shape[0] / 5), int(img_gray.shape[1] / 20)))

text = ''
for row in img_resize:
    for pixel in row:
        text += ascii_char[int(pixel / 256 * char_len)]
    text += '\n'

print(text)


