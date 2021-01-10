import numpy as np
from cv2 import bitwise_and
from cv2 import transform
from cv2 import addWeighted
from cv2 import convertScaleAbs
from cv2 import cvtColor
from cv2 import COLOR_BGR2HSV
from cv2 import COLOR_HSV2BGR
from cv2 import filter2D
from cv2 import split
from cv2 import LUT
from cv2 import equalizeHist
from cv2 import merge
from cv2 import COLOR_BGR2GRAY
from cv2 import bilateralFilter
from cv2 import medianBlur
from cv2 import adaptiveThreshold
from cv2 import ADAPTIVE_THRESH_GAUSSIAN_C
from cv2 import THRESH_BINARY
from cv2 import COLOR_GRAY2BGR
from cv2 import imread
from cv2 import imwrite
from scipy.interpolate import UnivariateSpline
""" import sys """
import os

def sepia(image,amount,mask=None):
    img2=0
    if type(mask)!=type(None):
        t=255-mask
        img2=bitwise_and(image,image,mask=mask)
        image=bitwise_and(image,image,mask=t)
        
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    sepia=transform(image,kernel)
    amount=amount/100
    if type(mask)!=type(None):
        res=addWeighted(image,1-amount,sepia,amount,0)
        return res+img2
    return addWeighted(image,1-amount,sepia,amount,0)

def brightness(image, amount):
    return convertScaleAbs(image,beta=amount)

def saturation(image, amount):
    hsv=cvtColor(image, COLOR_BGR2HSV)
    hsv[:,:,2]=convertScaleAbs(hsv[:,:,2],beta=amount)
    return cvtColor(hsv, COLOR_HSV2BGR)

def sharpness(image, amount):
    kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    amount=amount/100
    res=filter2D(image,-1,kernel)
    return addWeighted(image, 1-amount, res, amount, 0)

def warm(image, amount):
    x,y1=[0, 64, 128, 256], [0, 80, 160, 256]
    spline=UnivariateSpline(x,y1)
    np.set_printoptions(suppress=True)
    inc_lut=spline(range(256))
    x,y2=[0, 64, 128, 256], [0, 50, 100, 256]
    spline=UnivariateSpline(x,y2)
    dec_lut=spline(range(256))
    image2=image.copy()
    b, g, r = split(image)#image[:,:,0],image[:,:,1],image[:,:,2]
    b=np.uint8(LUT(b,dec_lut))
    r=np.uint8(LUT(r, inc_lut))
    image2=merge((b,g,r))
    amount=amount/100
    #print(image.shape)
    #print(b.shape)
    return addWeighted(image, 1-amount, image2, amount, 0)
    
def cold(image, amount):
    x,y1=[0, 64, 128, 256], [0, 80, 160, 256]
    spline=UnivariateSpline(x,y1)
    np.set_printoptions(suppress=True)
    inc_lut=spline(range(256))
    x,y2=[0, 64, 128, 256], [0, 50, 100, 256]
    spline=UnivariateSpline(x,y2)
    dec_lut=spline(range(256))
    image2=image.copy()
    b, g, r = split(image)#image[:,:,0],image[:,:,1],image[:,:,2]
    r=np.uint8(LUT(r,dec_lut))
    b=np.uint8(LUT(b, inc_lut))
    image2=merge((b,g,r))
    amount=amount/100
    #print(image.shape)
    #print(b.shape)
    return addWeighted(image, 1-amount, image2, amount, 0)

def equalise(image, amount):
    b , g, r = split(image)
    b_eql = equalizeHist(b)
    g_eql = equalizeHist(g)
    r_eql = equalizeHist(r)
    image2=merge((b_eql, g_eql, r_eql))
    amount=amount/100
    return addWeighted(image, 1-amount , image2, amount, 0)

def cartoon(image, amount):
    grey=cvtColor(image, COLOR_BGR2GRAY)
    blf=bilateralFilter(image, 5, 250, 250)
    medblur=medianBlur(grey, 5)
    """lap=cv2.Laplacian(medblur, -1, ksize=3)
    lap=255-lap
    lap=cv2.cvtColor(lap, cv2.COLOR_GRAY2BGR)"""
    amount=int(amount/10)
    if amount<=1:
        amount=3
    amount=amount if amount%2==1 else amount+1
    adap=adaptiveThreshold(medblur, 255, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY, amount, 2)
    adap=cvtColor(adap, COLOR_GRAY2BGR)
    image2=bitwise_and(blf,adap)
    return image2

#filename input_folder_path output_folder_path sepia brightness saturation sharpness warm cold equalise cartoon
effects=[sepia,brightness,saturation,sharpness,warm,cold,equalise,cartoon]
effect_suffix=['_sep_','_brgt_','_stur_','_srp_','_wrm_','_cld_','_eq_','_toon_']
""" input_folder_path=sys.argv[1]
output_folder_path=sys.argv[2]
effects_input=sys.argv[3:] """
def applyEffects(input_folder_path,output_folder_path,effects_input):
    effects_input=[i.split('-') for i in effects_input]
    imgs_path=os.listdir(input_folder_path)

    imgs_path=[i for i in imgs_path if i.find('.jpg')!=-1 or i.find('.bmp')!=-1 or i.find('.dib')!=-1 or i.find('.jpeg')!=-1 or i.find('.jpe')!=-1 or i.find('.jp2')!=-1 or i.find('.png')!=-1 or i.find('.webp')!=-1 or i.find('.pbm')!=-1 or i.find('.pgm')!=-1 or i.find('.ppm')!=-1 or i.find('.pxm')!=-1 or i.find('.pnm')!=-1 or i.find('.pfm')!=-1 or i.find('.sr')!=-1 or i.find('.ras')!=-1 or i.find('.tiff')!=-1 or i.find('.tif')!=-1 or i.find('.exr')!=-1 or i.find('.hdr')!=-1 or i.find('.pic')!=-1]
    #print(imgs_path)
    for imgpath in imgs_path:
        img=imread(input_folder_path+'/'+imgpath)
        for eff,amount in effects_input:
            amount=int(amount)
            suffix=''
            for eff_type in range(len(eff)):
                if eff[eff_type]=='1':
                    suffix=suffix+effect_suffix[eff_type]
                    img=effects[eff_type](img,amount)
            filename=imgpath.split('.')[0]+suffix+'.jpg'
            imwrite(output_folder_path+'/'+filename,img)
"complete"