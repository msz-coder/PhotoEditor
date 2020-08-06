import os
import sys

# from PIL import Image, ImageFilter

FILTERS = '''

1) BLUR
2) CONTOUR
3) DETAIL
4) EDGE_ENHANCE
5) EDGE_ENHANCE_MORE
6) EMBOSS
7) FIND_EDGES
8) SHARPEN

'''
IMG_FOLDER = input('Give a folder name with Images: ')
OUTPUT_FOLDER = input('Give a destination folder: ')
FILTERS_DICT = {'1': 'BLUR', '2': 'CONTOUR', '3': 'DETAIL', '4': 'EDGE_ENHANCE', '5': 'EDGE_ENHANCE_MORE',
                '6': 'EMBOSS', '7': 'FIND_EDGES', '8': 'SHARPEN'}
print(FILTERS)
SELECT_FILTER = input('Choose a filter: ')


