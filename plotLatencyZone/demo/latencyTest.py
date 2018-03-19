#!/usr/bin/env python
# coding: utf-8

# In[1]:

from __future__ import division, print_function

import matplotlib.pyplot as plt
import matplotlib

import numpy as np
plt.rcParams['image.cmap'] = 'gist_earth'


# In[4]:

import sys
print(sys.version)

if __name__ == "__main__":
    NUM_ITE = int(sys.argv[1])


# In[4]:

from tf_unet import image_gen
from tf_unet import unet
from tf_unet import util


# In[3]:

nx = 572
ny = 572


# In[4]:
for i in range(1, NUM_ITE):
	generator = image_gen.GrayScaleDataProvider(nx, ny, cnt=20)
	net = unet.Unet(channels=generator.channels, n_class=generator.n_class, layers=3, features_root=16)



x_test, y_test = generator(1)
prediction = net.predict("./unet_trained/model.cpkt", x_test)

