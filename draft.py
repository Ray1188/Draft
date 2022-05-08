# s = input().split()
# print(s)
import random
import string
import numpy
import os.path
import shutil
from os import path

# x = print(newPath)
src_r = r'D:\Testing\Excel_worker\Txt_file1234'
src_o = r'D:\Testing\Excel_worker\Txt_file123'
# src_o = r'D:\Testing\Excel_worker\Excel_file\Txt_file'
v = 'temp.txt'
v1 = 'temp1.txt'
# s = ' '.join(random.choices(string.digits, k=9))
# print(type(s))
# def teat(n):
#     res = numpy.array([random.randrange(1, 50) for i in range(n)])
#     return res
#
#
# def qw(arr):
#     for num in arr:
#         print(num % 10)
#
# arr = teat(10)
# print(arr)
# qw(arr)
def rename_folder(src_o, src_r):
    os.rename(src_o, src_r)
    print('finish')

# rename_folder(src_o, src_r)
# if path.exists("guru99.txt"):
# 	src = path.realpath("guru99.txt")

# print(src)

# shutil.copy(src_r, src_o)
# base_name, ext = os.path.splitext(src_o)
# base_m = os.path.splitext(src_o)
# print(base_m[0])

def generate_files(path):
    for i in range(1, 10):
        strPath = os.path.split(path)
        base_name, ext = os.path.splitext(strPath[1])
        new_file_name = base_name+'_'+str(i)+ext
        newPath = os.path.join(strPath[0], new_file_name)


# generate_files(src_r)
# rename_folder(src_o, src_r)
shutil.copytree(src_o, src_r)
# compare perfomance between copytree and replace
# how install venv with python 2.7