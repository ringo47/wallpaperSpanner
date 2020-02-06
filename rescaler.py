#!/usr/bin/env python3
import cv2
import numpy as np
import gi

gi.require_version("Gdk", "3.0")
from gi.repository import Gdk
allmonitors = []
gdkdsp = Gdk.Display.get_default()
for i in range(gdkdsp.get_n_monitors()):
    monitor = gdkdsp.get_monitor(i)
    scale = monitor.get_scale_factor()
    geo = monitor.get_geometry()
    allmonitors.append([
        monitor.get_model()] + [n * scale for n in [
            geo.x, geo.y, geo.width, geo.height
        ]
    ])
#print(allmonitors)

def spanned(monitorStatus):
    #wp=cv2.imread('/home/ringo/Pictures/Wallpapers/cyberpunk-black-widow-4k-y0-2160x3840.jpg')
    wp=cv2.imread('/home/ringo/Pictures/Wallpapers/cyberpunk-2077-black-widow-ve-2160x3840.jpg')
    pscale=0.9 #downscaling to 1920 from 2160
    bezel_offset=150
    topLeft=[500,0] #corner for cropping to a 1920x2160 window
    scaling=1.51 #(24inch/15.6inch) upscale higher ppi monitor

    wp=cv2.resize(wp,(0,0),fx=pscale,fy=pscale,interpolation=cv2.INTER_AREA)
    wp=wp[topLeft[0]:topLeft[0]+2160, topLeft[1]:topLeft[1]+1920]
    wp_top=wp[:1080,:1920]
    wp_bot=wp[1080:2160,:1920]
    wp_bot=cv2.resize(wp_bot,(0,0),fx=scaling,fy=scaling,interpolation=cv2.INTER_AREA)
    newTL=[bezel_offset,(wp_bot.shape[1]-1920)//2]
    wp_bot=wp_bot[newTL[0]:newTL[0]+1080,newTL[1]:newTL[1]+1920]
    nwp=np.vstack([wp_top,wp_bot])

    #cv2.imshow('wp',wp[topLeft[0]:topLeft[0]+2160, topLeft[1]:topLeft[1]+1920])
    ##cv2.imshow('wpb',wp_bot)
    ##cv2.waitKey()
    ##cv2.imshow('wpt',wp_top)
    ##cv2.waitKey()

    ##cv2.imshow('wpt',nwp)
    ##cv2.waitKey()
    ##cv2.destroyAllWindows()
    
    if monitorStatus==2:
        cv2.imwrite('/home/ringo/Pictures/Wallpapers/CyberWidow.jpg',nwp)
    else:
        cv2.imwrite('/home/ringo/Pictures/Wallpapers/CyberWidow.jpg',wp_top)
    

if __name__=="__main__":
    spanned(len(allmonitors))
    
