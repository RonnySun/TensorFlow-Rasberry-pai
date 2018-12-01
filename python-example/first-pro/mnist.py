# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 14:24:10 2018

@author: Administrator
"""

from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
import tensorflow as tf

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
print('-------------------\n');
'''1)获得数据集的个数'''
train_nums = mnist.train.num_examples
validation_nums = mnist.validation.num_examples
test_nums = mnist.test.num_examples
print('MNIST数据集的个数')
print(' >>>train_nums=%d' % train_nums,'\n',
      '>>>validation_nums=%d'% validation_nums,'\n',
      '>>>test_nums=%d' % test_nums,'\n')