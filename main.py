
import os
import urllib
import traceback
import time
import sys
import numpy as np
import cv2

import numpy as np
import platform
from PIL import Image, ImageDraw

from rknnlite.api import RKNNLite

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



if __name__ == '__main__':
    RK3588_RKNN_MODEL = './RKNNModel/PFLD_GhostNet_112_1_opt_sim.rknn'
    rknn_lite = RKNNLite()

    # Load RKNN model
    print('--> Load RKNN model')
    ret = rknn_lite.load_rknn(RK3588_RKNN_MODEL)


    ori_img = cv2.imread('./testImg/4.png')
    #imgTemp = cv2.cvtColor(ori_img, cv2.COLOR_BGR2RGB)
    img=cv2.resize(ori_img, (112, 112), interpolation=cv2.INTER_CUBIC)
    img1 = np.expand_dims(img, 0)

    ret = rknn_lite.init_runtime(core_mask=RKNNLite.NPU_CORE_0)
    # Inference
    print('--> Running model')
    outputs = rknn_lite.inference(inputs=[img1])

    preds=outputs[0]
    print(preds)
    for i in range(98):
       center_x = 112* preds[0,i * 2]
       center_y =  112*preds[0,i * 2 + 1]

       radius = 1
       cv2.circle(img,(int(center_x),int(center_y)),radius,(21,123,0))


    cv2.imwrite("./picture.jpg",img)
    #cv2.imshow("df",img)
    #cv2.waitKey(0)
