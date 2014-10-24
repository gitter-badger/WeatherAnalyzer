#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.2'
__author__ = 'Matthew (matthewgao@gmail.com)'

from src.ImageGetter import *
from src.ImageAnalyzer import *
from src.WeiboPoster import *
import time

if __name__ == "__main__":

    status = "Clear"
    imgGet = ImageGetter()
    imgAnalyzer = ImageAnalyzer()
    
    
    while True:
        try:
            imgData = imgGet.getRadarImg("http://www.nmc.gov.cn/publish/radar/qingpu.htm")

            imgAnalyzer.setRegion((235,185,330,274))
            croppedImg = imgAnalyzer.cropImage(imgData)

            imgAnalyzer.setRegion((37,32,46,37))
            croppedImg2 = imgAnalyzer.cropImage(croppedImg)

            result = imgAnalyzer.analysisImage(croppedImg2)
            print "Check result: " + result

            if status != result:
                string = "#AutoWeatherPoster# "
                string = string + "The weather at Jiangqiao is " + status
                string = string + ", Right Now"
                weibo = WeiboPoster()
                weibo.postWeibo(string)
                status = result
                
            time.sleep(600)
    
        except Exception , e:
            print Exception,":",e
            continue
   
