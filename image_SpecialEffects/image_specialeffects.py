#author: hanshiqiang365 （微信公众号：韩思工作室）

import cv2
import numpy as np
from PIL import Image,ImageFilter

class pic_imshow:
    def __init__(self,file,temp='',params=12):
        self.file=file
        self.temp=temp
        self.params=params      

    def filter_PIL(self):
        src=Image.open(self.file)
        img = src.filter(ImageFilter.BLUR)              # 模糊滤镜
        img.save(f'{self.file}_blur.jpg')

        img = src.filter(ImageFilter.EMBOSS)            # 浮雕效果滤镜
        img.save(f'{self.file}_emboss.jpg')

        img = src.filter(ImageFilter.EDGE_ENHANCE)      # 凸显边界
        img.save(f'{self.file}_edgeenhance.jpg')

        img = src.filter(ImageFilter.EDGE_ENHANCE_MORE) # 加倍凸显边界
        img.save(f'{self.file}_edgeenhancemore.jpg')

        img = src.filter(ImageFilter.FIND_EDGES)        # 只保留边界
        img.save(f'{self.file}_findedges.jpg')

        img = src.filter(ImageFilter.CONTOUR)           # 铅笔画效果
        img.save(f'{self.file}_contour.jpg')

        img = src.filter(ImageFilter.SMOOTH_MORE)       # 平滑滤镜(阀值更大)
        img.save(f'{self.file}_smoothmore.jpg')
 
    def fleeting(self): #"流年"效果
        src=Image.open(self.file)
        img=np.asarray(Image.open(self.file).convert('RGB'))
        img1=np.sqrt(img*[1.0,0.0,0.0])*self.params
        img2=img*[0.0,1.0,1.0]
        img=img1+img2
        img=Image.fromarray(np.array(img).astype('uint8'))
        #img.show()
        img.save(f'{self.file}_fleeting.jpg')

    def oldFilm(self): #"旧电影"效果
        src=Image.open(self.file)
        img=np.asarray(Image.open(self.file).convert('RGB'))
        trans = np.array([[0.393,0.769,0.189],[0.349,0.686,0.168],[0.272,0.534,0.131]]).transpose()
        img = np.dot(img,trans).clip(max=255)               
        img=Image.fromarray(np.array(img).astype('uint8')) 
        #img.show()
        img.save(f'{self.file}_oldFilm.jpg')

    def filter_opencv(self):
        src=cv2.imread(self.file)
        cv2.namedWindow('input',cv2.WINDOW_AUTOSIZE)
        cv2.imshow('input',src)
        dst=cv2.applyColorMap(src,self.temp)
        cv2.imshow('output',dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows() 
 
if __name__=='__main__':

    image_file='hengshan_temple.jpg'
    image=pic_imshow(image_file,cv2.COLORMAP_COOL)
    image.filter_PIL()
    image.fleeting()
    image.oldFilm()


