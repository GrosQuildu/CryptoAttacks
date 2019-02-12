from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from builtins import range

import itertools
import os
import re
import sys
from collections import defaultdict

from CryptoAttacks.Math import *
from CryptoAttacks.Utils import *

frequencies = {
    'Swedish': [('e', 10.149), ('a', 9.383), ('n', 8.542), ('r', 8.431), ('t', 7.691), ('s', 6.59), ('i', 5.817),
                ('l', 5.275), ('d', 4.702), ('o', 4.482), ('m', 3.471), ('k', 3.14), ('g', 2.862), ('v', 2.415),
                ('h', 2.09), ('f', 2.027), ('u', 1.919), ('p', 1.839), ('\xc3\xa4', 1.797), ('b', 1.535), ('c', 1.486),
                ('\xc3\xa5', 1.338), ('\xc3\xb6', 1.305), ('y', 0.708), ('j', 0.614), ('x', 0.159), ('w', 0.142),
                ('z', 0.07), ('q', 0.02), ('\xc5\x88', 0.0), ('\xc5\x84', 0.0), ('\xc5\x82', 0.0), ('\xc5\x9d', 0.0),
                ('\xc5\x9f', 0.0), ('\xc3\x9f', 0.0), ('\xc5\x9b', 0.0), ('\xc3\xb8', 0.0), ('\xc5\x93', 0.0),
                ('\xc3\xab', 0.0), ('\xc3\xaa', 0.0), ('\xc3\xa9', 0.0), ('\xc3\xa8', 0.0), ('\xc3\xaf', 0.0),
                ('\xc3\xae', 0.0), ('\xc3\xad', 0.0), ('\xc3\xac', 0.0), ('\xc5\xa5', 0.0), ('\xc3\xa2', 0.0),
                ('\xc3\xa1', 0.0), ('\xc3\xa0', 0.0), ('\xc3\xa7', 0.0), ('\xc3\xa6', 0.0), ('\xc3\xba', 0.0),
                ('\xc3\xb9', 0.0), ('\xc5\xbe', 0.0), ('\xc3\xbe', 0.0), ('\xc3\xbd', 0.0), ('\xc3\xbc', 0.0),
                ('\xc3\xb3', 0.0), ('\xc3\xb2', 0.0), ('\xc3\xb1', 0.0), ('\xc3\xb0', 0.0), ('\xc3\xb4', 0.0),
                ('\xc4\x8f', 0.0), ('\xc4\x8d', 0.0), ('\xc4\x89', 0.0), ('\xc4\x87', 0.0), ('\xc4\x85', 0.0),
                ('\xc5\xaf', 0.0), ('\xc4\x9f', 0.0), ('\xc5\xbc', 0.0), ('\xc4\x9d', 0.0), ('\xc4\x9b', 0.0),
                ('\xc5\xba', 0.0), ('\xc4\x99', 0.0), ('\xc5\xad', 0.0), ('\xc5\xa1', 0.0), ('\xc4\xa5', 0.0),
                ('\xc3\xa3', 0.0), ('\xc5\x99', 0.0), ('\xc4\xb5', 0.0), ('\xc4\xb1', 0.0)],
    'Danish': [('e', 15.453), ('r', 8.956), ('n', 7.24), ('t', 6.862), ('a', 6.025), ('i', 6.0), ('d', 5.858),
               ('s', 5.805), ('l', 5.229), ('o', 4.636), ('g', 4.077), ('k', 3.395), ('m', 3.237), ('f', 2.406),
               ('v', 2.332), ('b', 2.0), ('u', 1.979), ('p', 1.756), ('h', 1.621), ('\xc3\xa5', 1.19),
               ('\xc3\xb8', 0.939), ('\xc3\xa6', 0.872), ('j', 0.73), ('y', 0.698), ('c', 0.565), ('w', 0.069),
               ('z', 0.034), ('x', 0.028), ('q', 0.007), ('\xc5\x88', 0.0), ('\xc5\x84', 0.0), ('\xc5\x82', 0.0),
               ('\xc5\x9d', 0.0), ('\xc5\x9f', 0.0), ('\xc3\x9f', 0.0), ('\xc5\x9b', 0.0), ('\xc5\x93', 0.0),
               ('\xc3\xab', 0.0), ('\xc3\xaa', 0.0), ('\xc3\xa9', 0.0), ('\xc3\xa8', 0.0), ('\xc3\xaf', 0.0),
               ('\xc3\xae', 0.0), ('\xc3\xad', 0.0), ('\xc3\xac', 0.0), ('\xc5\xa5', 0.0), ('\xc3\xa2', 0.0),
               ('\xc3\xa1', 0.0), ('\xc3\xa0', 0.0), ('\xc3\xa7', 0.0), ('\xc3\xa4', 0.0), ('\xc3\xba', 0.0),
               ('\xc3\xb9', 0.0), ('\xc5\xbe', 0.0), ('\xc3\xbe', 0.0), ('\xc3\xbd', 0.0), ('\xc3\xbc', 0.0),
               ('\xc3\xb3', 0.0), ('\xc3\xb2', 0.0), ('\xc3\xb1', 0.0), ('\xc3\xb0', 0.0), ('\xc3\xb6', 0.0),
               ('\xc3\xb4', 0.0), ('\xc4\x8f', 0.0), ('\xc4\x8d', 0.0), ('\xc4\x89', 0.0), ('\xc4\x87', 0.0),
               ('\xc4\x85', 0.0), ('\xc5\xaf', 0.0), ('\xc4\x9f', 0.0), ('\xc5\xbc', 0.0), ('\xc4\x9d', 0.0),
               ('\xc4\x9b', 0.0), ('\xc5\xba', 0.0), ('\xc4\x99', 0.0), ('\xc5\xad', 0.0), ('\xc5\xa1', 0.0),
               ('\xc4\xa5', 0.0), ('\xc3\xa3', 0.0), ('\xc5\x99', 0.0), ('\xc4\xb5', 0.0), ('\xc4\xb1', 0.0)],
    'Icelandic': [('a', 10.11), ('r', 8.581), ('n', 7.711), ('i', 7.578), ('e', 6.418), ('s', 5.63), ('t', 4.953),
                  ('u', 4.562), ('l', 4.532), ('\xc3\xb0', 4.393), ('g', 4.241), ('m', 4.041), ('k', 3.314),
                  ('f', 3.013), ('v', 2.437), ('o', 2.166), ('h', 1.871), ('\xc3\xa1', 1.799), ('d', 1.575),
                  ('\xc3\xad', 1.57), ('\xc3\xbe', 1.455), ('j', 1.144), ('b', 1.043), ('\xc3\xb3', 0.994), ('y', 0.9),
                  ('\xc3\xa6', 0.867), ('p', 0.789), ('\xc3\xb6', 0.777), ('\xc3\xa9', 0.647), ('\xc3\xba', 0.613),
                  ('\xc3\xbd', 0.228), ('x', 0.046), ('\xc5\x88', 0.0), ('\xc5\x84', 0.0), ('\xc5\x82', 0.0),
                  ('\xc5\x9d', 0.0), ('\xc5\x9f', 0.0), ('\xc3\x9f', 0.0), ('\xc5\x9b', 0.0), ('\xc3\xb8', 0.0),
                  ('\xc5\x93', 0.0), ('\xc3\xab', 0.0), ('\xc3\xaa', 0.0), ('\xc3\xa8', 0.0), ('\xc3\xaf', 0.0),
                  ('\xc3\xae', 0.0), ('\xc3\xac', 0.0), ('\xc5\xa5', 0.0), ('\xc3\xa2', 0.0), ('\xc3\xa0', 0.0),
                  ('\xc3\xa7', 0.0), ('\xc3\xa5', 0.0), ('\xc3\xa4', 0.0), ('\xc3\xb9', 0.0), ('\xc5\xbe', 0.0),
                  ('\xc3\xbc', 0.0), ('\xc3\xb2', 0.0), ('\xc3\xb1', 0.0), ('\xc3\xb4', 0.0), ('\xc4\x8f', 0.0),
                  ('\xc4\x8d', 0.0), ('\xc4\x89', 0.0), ('\xc4\x87', 0.0), ('\xc4\x85', 0.0), ('\xc5\xaf', 0.0),
                  ('\xc4\x9f', 0.0), ('\xc5\xbc', 0.0), ('\xc4\x9d', 0.0), ('\xc4\x9b', 0.0), ('\xc5\xba', 0.0),
                  ('\xc4\x99', 0.0), ('\xc5\xad', 0.0), ('z', 0.0), ('c', 0.0), ('\xc5\xa1', 0.0), ('\xc4\xa5', 0.0),
                  ('q', 0.0), ('\xc3\xa3', 0.0), ('w', 0.0), ('\xc5\x99', 0.0), ('\xc4\xb5', 0.0), ('\xc4\xb1', 0.0)],
    'Finnish': [('a', 12.217), ('i', 10.817), ('n', 8.826), ('t', 8.75), ('e', 7.968), ('s', 7.862), ('l', 5.761),
                ('o', 5.614), ('u', 5.008), ('k', 4.973), ('\xc3\xa4', 3.577), ('m', 3.202), ('r', 2.872), ('v', 2.25),
                ('j', 2.042), ('h', 1.851), ('p', 1.842), ('y', 1.745), ('d', 1.043), ('\xc3\xb6', 0.444), ('g', 0.392),
                ('c', 0.281), ('b', 0.281), ('f', 0.194), ('w', 0.094), ('z', 0.051), ('x', 0.031), ('q', 0.013),
                ('\xc3\xa5', 0.003), ('\xc5\x88', 0.0), ('\xc5\x84', 0.0), ('\xc5\x82', 0.0), ('\xc5\x9d', 0.0),
                ('\xc5\x9f', 0.0), ('\xc3\x9f', 0.0), ('\xc5\x9b', 0.0), ('\xc3\xb8', 0.0), ('\xc5\x93', 0.0),
                ('\xc3\xab', 0.0), ('\xc3\xaa', 0.0), ('\xc3\xa9', 0.0), ('\xc3\xa8', 0.0), ('\xc3\xaf', 0.0),
                ('\xc3\xae', 0.0), ('\xc3\xad', 0.0), ('\xc3\xac', 0.0), ('\xc5\xa5', 0.0), ('\xc3\xa2', 0.0),
                ('\xc3\xa1', 0.0), ('\xc3\xa0', 0.0), ('\xc3\xa7', 0.0), ('\xc3\xa6', 0.0), ('\xc3\xba', 0.0),
                ('\xc3\xb9', 0.0), ('\xc5\xbe', 0.0), ('\xc3\xbe', 0.0), ('\xc3\xbd', 0.0), ('\xc3\xbc', 0.0),
                ('\xc3\xb3', 0.0), ('\xc3\xb2', 0.0), ('\xc3\xb1', 0.0), ('\xc3\xb0', 0.0), ('\xc3\xb4', 0.0),
                ('\xc4\x8f', 0.0), ('\xc4\x8d', 0.0), ('\xc4\x89', 0.0), ('\xc4\x87', 0.0), ('\xc4\x85', 0.0),
                ('\xc5\xaf', 0.0), ('\xc4\x9f', 0.0), ('\xc5\xbc', 0.0), ('\xc4\x9d', 0.0), ('\xc4\x9b', 0.0),
                ('\xc5\xba', 0.0), ('\xc4\x99', 0.0), ('\xc5\xad', 0.0), ('\xc5\xa1', 0.0), ('\xc4\xa5', 0.0),
                ('\xc3\xa3', 0.0), ('\xc5\x99', 0.0), ('\xc4\xb5', 0.0), ('\xc4\xb1', 0.0)],
    'Turkish': [('a', 12.92), ('e', 9.912), ('i', 9.6), ('n', 7.987), ('r', 7.722), ('l', 5.922), ('k', 5.683),
                ('d', 5.206), ('\xc4\xb1', 5.114), ('m', 3.752), ('y', 3.336), ('t', 3.314), ('u', 3.235), ('s', 3.014),
                ('o', 2.976), ('b', 2.844), ('\xc3\xbc', 1.854), ('\xc5\x9f', 1.78), ('z', 1.5), ('c', 1.463),
                ('g', 1.253), ('h', 1.212), ('\xc3\xa7', 1.156), ('\xc4\x9f', 1.125), ('v', 0.959), ('p', 0.886),
                ('\xc3\xb6', 0.777), ('f', 0.461), ('j', 0.034), ('\xc5\x88', 0.0), ('\xc5\x84', 0.0),
                ('\xc5\x82', 0.0), ('\xc5\x9d', 0.0), ('\xc3\x9f', 0.0), ('\xc5\x9b', 0.0), ('\xc3\xb8', 0.0),
                ('\xc5\x93', 0.0), ('\xc3\xab', 0.0), ('\xc3\xaa', 0.0), ('\xc3\xa9', 0.0), ('\xc3\xa8', 0.0),
                ('\xc3\xaf', 0.0), ('\xc3\xae', 0.0), ('\xc3\xad', 0.0), ('\xc3\xac', 0.0), ('\xc5\xa5', 0.0),
                ('\xc3\xa2', 0.0), ('\xc3\xa1', 0.0), ('\xc3\xa0', 0.0), ('\xc3\xa6', 0.0), ('\xc3\xa5', 0.0),
                ('\xc3\xa4', 0.0), ('\xc3\xba', 0.0), ('\xc3\xb9', 0.0), ('\xc5\xbe', 0.0), ('\xc3\xbe', 0.0),
                ('\xc3\xbd', 0.0), ('\xc3\xb3', 0.0), ('\xc3\xb2', 0.0), ('\xc3\xb1', 0.0), ('\xc3\xb0', 0.0),
                ('\xc3\xb4', 0.0), ('\xc4\x8f', 0.0), ('x', 0.0), ('\xc4\x8d', 0.0), ('\xc4\x89', 0.0),
                ('\xc4\x87', 0.0), ('\xc4\x85', 0.0), ('\xc5\xaf', 0.0), ('\xc5\xbc', 0.0), ('\xc4\x9d', 0.0),
                ('\xc4\x9b', 0.0), ('\xc5\xba', 0.0), ('\xc4\x99', 0.0), ('\xc5\xad', 0.0), ('\xc5\xa1', 0.0),
                ('\xc4\xa5', 0.0), ('q', 0.0), ('\xc3\xa3', 0.0), ('w', 0.0), ('\xc5\x99', 0.0), ('\xc4\xb5', 0.0)],
    'German': [('e', 16.396), ('n', 9.776), ('s', 7.27), ('r', 7.003), ('i', 6.55), ('a', 6.516), ('t', 6.154),
               ('d', 5.076), ('h', 4.577), ('u', 4.166), ('l', 3.437), ('g', 3.009), ('c', 2.732), ('o', 2.594),
               ('m', 2.534), ('w', 1.921), ('b', 1.886), ('f', 1.656), ('k', 1.417), ('z', 1.134), ('\xc3\xbc', 0.995),
               ('v', 0.846), ('p', 0.67), ('\xc3\xa4', 0.578), ('\xc3\xb6', 0.443), ('\xc3\x9f', 0.307), ('j', 0.268),
               ('y', 0.039), ('x', 0.034), ('q', 0.018), ('\xc5\x88', 0.0), ('\xc5\x84', 0.0), ('\xc5\x82', 0.0),
               ('\xc5\x9d', 0.0), ('\xc5\x9f', 0.0), ('\xc5\x9b', 0.0), ('\xc3\xb8', 0.0), ('\xc5\x93', 0.0),
               ('\xc3\xab', 0.0), ('\xc3\xaa', 0.0), ('\xc3\xa9', 0.0), ('\xc3\xa8', 0.0), ('\xc3\xaf', 0.0),
               ('\xc3\xae', 0.0), ('\xc3\xad', 0.0), ('\xc3\xac', 0.0), ('\xc5\xa5', 0.0), ('\xc3\xa2', 0.0),
               ('\xc3\xa1', 0.0), ('\xc3\xa0', 0.0), ('\xc3\xa7', 0.0), ('\xc3\xa6', 0.0), ('\xc3\xa5', 0.0),
               ('\xc3\xba', 0.0), ('\xc3\xb9', 0.0), ('\xc5\xbe', 0.0), ('\xc3\xbe', 0.0), ('\xc3\xbd', 0.0),
               ('\xc3\xb3', 0.0), ('\xc3\xb2', 0.0), ('\xc3\xb1', 0.0), ('\xc3\xb0', 0.0), ('\xc3\xb4', 0.0),
               ('\xc4\x8f', 0.0), ('\xc4\x8d', 0.0), ('\xc4\x89', 0.0), ('\xc4\x87', 0.0), ('\xc4\x85', 0.0),
               ('\xc5\xaf', 0.0), ('\xc4\x9f', 0.0), ('\xc5\xbc', 0.0), ('\xc4\x9d', 0.0), ('\xc4\x9b', 0.0),
               ('\xc5\xba', 0.0), ('\xc4\x99', 0.0), ('\xc5\xad', 0.0), ('\xc5\xa1', 0.0), ('\xc4\xa5', 0.0),
               ('\xc3\xa3', 0.0), ('\xc5\x99', 0.0), ('\xc4\xb5', 0.0), ('\xc4\xb1', 0.0)],
    'Dutch': [('e', 18.91), ('n', 10.032), ('a', 7.486), ('t', 6.79), ('i', 6.499), ('r', 6.411), ('o', 6.063),
              ('d', 5.933), ('s', 3.73), ('l', 3.568), ('g', 3.403), ('v', 2.85), ('h', 2.38), ('k', 2.248),
              ('m', 2.213), ('u', 1.99), ('b', 1.584), ('p', 1.57), ('w', 1.52), ('j', 1.46), ('z', 1.39), ('c', 1.242),
              ('f', 0.805), ('x', 0.036), ('y', 0.035), ('q', 0.009), ('\xc5\x88', 0.0), ('\xc5\x84', 0.0),
              ('\xc5\x82', 0.0), ('\xc5\x9d', 0.0), ('\xc5\x9f', 0.0), ('\xc3\x9f', 0.0), ('\xc5\x9b', 0.0),
              ('\xc3\xb8', 0.0), ('\xc5\x93', 0.0), ('\xc3\xab', 0.0), ('\xc3\xaa', 0.0), ('\xc3\xa9', 0.0),
              ('\xc3\xa8', 0.0), ('\xc3\xaf', 0.0), ('\xc3\xae', 0.0), ('\xc3\xad', 0.0), ('\xc3\xac', 0.0),
              ('\xc5\xa5', 0.0), ('\xc3\xa2', 0.0), ('\xc3\xa1', 0.0), ('\xc3\xa0', 0.0), ('\xc3\xa7', 0.0),
              ('\xc3\xa6', 0.0), ('\xc3\xa5', 0.0), ('\xc3\xa4', 0.0), ('\xc3\xba', 0.0), ('\xc3\xb9', 0.0),
              ('\xc5\xbe', 0.0), ('\xc3\xbe', 0.0), ('\xc3\xbd', 0.0), ('\xc3\xbc', 0.0), ('\xc3\xb3', 0.0),
              ('\xc3\xb2', 0.0), ('\xc3\xb1', 0.0), ('\xc3\xb0', 0.0), ('\xc3\xb6', 0.0), ('\xc3\xb4', 0.0),
              ('\xc4\x8f', 0.0), ('\xc4\x8d', 0.0), ('\xc4\x89', 0.0), ('\xc4\x87', 0.0), ('\xc4\x85', 0.0),
              ('\xc5\xaf', 0.0), ('\xc4\x9f', 0.0), ('\xc5\xbc', 0.0), ('\xc4\x9d', 0.0), ('\xc4\x9b', 0.0),
              ('\xc5\xba', 0.0), ('\xc4\x99', 0.0), ('\xc5\xad', 0.0), ('\xc5\xa1', 0.0), ('\xc4\xa5', 0.0),
              ('\xc3\xa3', 0.0), ('\xc5\x99', 0.0), ('\xc4\xb5', 0.0), ('\xc4\xb1', 0.0)],
    'French': [('e', 14.715), ('s', 7.948), ('a', 7.636), ('i', 7.529), ('t', 7.244), ('n', 7.095), ('r', 6.693),
               ('u', 6.311), ('o', 5.796), ('l', 5.456), ('d', 3.669), ('c', 3.26), ('m', 2.968), ('p', 2.521),
               ('v', 1.838), ('\xc3\xa9', 1.504), ('q', 1.362), ('f', 1.066), ('b', 0.901), ('g', 0.866), ('h', 0.737),
               ('j', 0.613), ('\xc3\xa0', 0.486), ('x', 0.427), ('z', 0.326), ('\xc3\xa8', 0.271), ('\xc3\xaa', 0.218),
               ('y', 0.128), ('\xc3\xa7', 0.085), ('w', 0.074), ('\xc3\xb9', 0.058), ('\xc3\xa2', 0.051), ('k', 0.049),
               ('\xc3\xae', 0.045), ('\xc3\xb4', 0.023), ('\xc5\x93', 0.018), ('\xc3\xab', 0.008), ('\xc3\xaf', 0.005),
               ('\xc5\x88', 0.0), ('\xc5\x84', 0.0), ('\xc5\x82', 0.0), ('\xc5\x9d', 0.0), ('\xc5\x9f', 0.0),
               ('\xc3\x9f', 0.0), ('\xc5\x9b', 0.0), ('\xc3\xb8', 0.0), ('\xc3\xad', 0.0), ('\xc3\xac', 0.0),
               ('\xc5\xa5', 0.0), ('\xc3\xa1', 0.0), ('\xc3\xa6', 0.0), ('\xc3\xa5', 0.0), ('\xc3\xa4', 0.0),
               ('\xc3\xba', 0.0), ('\xc5\xbe', 0.0), ('\xc3\xbe', 0.0), ('\xc3\xbd', 0.0), ('\xc3\xbc', 0.0),
               ('\xc3\xb3', 0.0), ('\xc3\xb2', 0.0), ('\xc3\xb1', 0.0), ('\xc3\xb0', 0.0), ('\xc3\xb6', 0.0),
               ('\xc4\x8f', 0.0), ('\xc4\x8d', 0.0), ('\xc4\x89', 0.0), ('\xc4\x87', 0.0), ('\xc4\x85', 0.0),
               ('\xc5\xaf', 0.0), ('\xc4\x9f', 0.0), ('\xc5\xbc', 0.0), ('\xc4\x9d', 0.0), ('\xc4\x9b', 0.0),
               ('\xc5\xba', 0.0), ('\xc4\x99', 0.0), ('\xc5\xad', 0.0), ('\xc5\xa1', 0.0), ('\xc4\xa5', 0.0),
               ('\xc3\xa3', 0.0), ('\xc5\x99', 0.0), ('\xc4\xb5', 0.0), ('\xc4\xb1', 0.0)],
    'Czech': [('a', 8.421), ('e', 7.562), ('o', 6.695), ('n', 6.468), ('i', 6.073), ('t', 5.727), ('v', 5.344),
              ('s', 5.212), ('r', 4.799), ('l', 3.802), ('d', 3.475), ('k', 2.894), ('m', 2.446), ('u', 2.16),
              ('p', 1.906), ('\xc3\xad', 1.643), ('z', 1.503), ('j', 1.433), ('h', 1.356), ('\xc4\x9b', 1.222),
              ('y', 1.043), ('\xc3\xbd', 0.995), ('\xc3\xa1', 0.867), ('b', 0.822), ('c', 0.74), ('\xc5\xbe', 0.721),
              ('\xc5\xa1', 0.688), ('\xc3\xa9', 0.633), ('\xc4\x8d', 0.462), ('\xc5\x99', 0.38), ('\xc5\xaf', 0.204),
              ('g', 0.092), ('f', 0.084), ('\xc3\xba', 0.045), ('x', 0.027), ('\xc3\xb3', 0.024), ('w', 0.016),
              ('\xc4\x8f', 0.015), ('\xc5\x88', 0.007), ('\xc5\xa5', 0.006), ('q', 0.001), ('\xc5\x84', 0.0),
              ('\xc5\x82', 0.0), ('\xc5\x9d', 0.0), ('\xc5\x9f', 0.0), ('\xc3\x9f', 0.0), ('\xc5\x9b', 0.0),
              ('\xc3\xb8', 0.0), ('\xc5\x93', 0.0), ('\xc3\xab', 0.0), ('\xc3\xaa', 0.0), ('\xc3\xa8', 0.0),
              ('\xc3\xaf', 0.0), ('\xc3\xae', 0.0), ('\xc3\xac', 0.0), ('\xc3\xa2', 0.0), ('\xc3\xa0', 0.0),
              ('\xc3\xa7', 0.0), ('\xc3\xa6', 0.0), ('\xc3\xa5', 0.0), ('\xc3\xa4', 0.0), ('\xc3\xb9', 0.0),
              ('\xc3\xbe', 0.0), ('\xc3\xbc', 0.0), ('\xc3\xb2', 0.0), ('\xc3\xb1', 0.0), ('\xc3\xb0', 0.0),
              ('\xc3\xb6', 0.0), ('\xc3\xb4', 0.0), ('\xc4\x89', 0.0), ('\xc4\x87', 0.0), ('\xc4\x85', 0.0),
              ('\xc4\x9f', 0.0), ('\xc5\xbc', 0.0), ('\xc4\x9d', 0.0), ('\xc5\xba', 0.0), ('\xc4\x99', 0.0),
              ('\xc5\xad', 0.0), ('\xc4\xa5', 0.0), ('\xc3\xa3', 0.0), ('\xc4\xb5', 0.0), ('\xc4\xb1', 0.0)],
    'Portuguese': [('a', 14.634), ('e', 12.57), ('o', 9.735), ('s', 6.805), ('r', 6.53), ('i', 6.186), ('d', 4.992),
                   ('m', 4.738), ('n', 4.446), ('t', 4.336), ('c', 3.882), ('u', 3.639), ('l', 2.779), ('p', 2.523),
                   ('v', 1.575), ('g', 1.303), ('q', 1.204), ('b', 1.043), ('f', 1.023), ('h', 0.781),
                   ('\xc3\xa3', 0.733), ('\xc3\xb4', 0.635), ('\xc3\xa2', 0.562), ('\xc3\xa7', 0.53), ('z', 0.47),
                   ('\xc3\xaa', 0.45), ('j', 0.397), ('\xc3\xa9', 0.337), ('\xc3\xb3', 0.296), ('x', 0.253),
                   ('\xc3\xba', 0.207), ('\xc3\xad', 0.132), ('\xc3\xa1', 0.118), ('\xc3\xa0', 0.072), ('w', 0.037),
                   ('\xc3\xbc', 0.026), ('k', 0.015), ('y', 0.006), ('\xc5\x88', 0.0), ('\xc5\x84', 0.0),
                   ('\xc5\x82', 0.0), ('\xc5\x9d', 0.0), ('\xc5\x9f', 0.0), ('\xc3\x9f', 0.0), ('\xc5\x9b', 0.0),
                   ('\xc3\xb8', 0.0), ('\xc5\x93', 0.0), ('\xc3\xab', 0.0), ('\xc3\xa8', 0.0), ('\xc3\xaf', 0.0),
                   ('\xc3\xae', 0.0), ('\xc3\xac', 0.0), ('\xc5\xa5', 0.0), ('\xc3\xa6', 0.0), ('\xc3\xa5', 0.0),
                   ('\xc3\xa4', 0.0), ('\xc3\xb9', 0.0), ('\xc5\xbe', 0.0), ('\xc3\xbe', 0.0), ('\xc3\xbd', 0.0),
                   ('\xc3\xb2', 0.0), ('\xc3\xb1', 0.0), ('\xc3\xb0', 0.0), ('\xc3\xb6', 0.0), ('\xc4\x8f', 0.0),
                   ('\xc4\x8d', 0.0), ('\xc4\x89', 0.0), ('\xc4\x87', 0.0), ('\xc4\x85', 0.0), ('\xc5\xaf', 0.0),
                   ('\xc4\x9f', 0.0), ('\xc5\xbc', 0.0), ('\xc4\x9d', 0.0), ('\xc4\x9b', 0.0), ('\xc5\xba', 0.0),
                   ('\xc4\x99', 0.0), ('\xc5\xad', 0.0), ('\xc5\xa1', 0.0), ('\xc4\xa5', 0.0), ('\xc5\x99', 0.0),
                   ('\xc4\xb5', 0.0), ('\xc4\xb1', 0.0)],
    'Spanish': [('e', 12.181), ('a', 11.525), ('o', 8.683), ('s', 7.977), ('r', 6.871), ('n', 6.712), ('i', 6.247),
                ('d', 5.01), ('l', 4.967), ('t', 4.632), ('c', 4.019), ('m', 3.157), ('u', 2.927), ('p', 2.51),
                ('b', 2.215), ('g', 1.768), ('v', 1.138), ('y', 1.008), ('q', 0.877), ('\xc3\xb3', 0.827),
                ('\xc3\xad', 0.725), ('h', 0.703), ('f', 0.692), ('\xc3\xa1', 0.502), ('j', 0.493), ('z', 0.467),
                ('\xc3\xa9', 0.433), ('\xc3\xb1', 0.311), ('x', 0.215), ('\xc3\xba', 0.168), ('w', 0.017),
                ('\xc3\xbc', 0.012), ('k', 0.011), ('\xc5\x88', 0.0), ('\xc5\x84', 0.0), ('\xc5\x82', 0.0),
                ('\xc5\x9d', 0.0), ('\xc5\x9f', 0.0), ('\xc3\x9f', 0.0), ('\xc5\x9b', 0.0), ('\xc3\xb8', 0.0),
                ('\xc5\x93', 0.0), ('\xc3\xab', 0.0), ('\xc3\xaa', 0.0), ('\xc3\xa8', 0.0), ('\xc3\xaf', 0.0),
                ('\xc3\xae', 0.0), ('\xc3\xac', 0.0), ('\xc5\xa5', 0.0), ('\xc3\xa2', 0.0), ('\xc3\xa0', 0.0),
                ('\xc3\xa7', 0.0), ('\xc3\xa6', 0.0), ('\xc3\xa5', 0.0), ('\xc3\xa4', 0.0), ('\xc3\xb9', 0.0),
                ('\xc5\xbe', 0.0), ('\xc3\xbe', 0.0), ('\xc3\xbd', 0.0), ('\xc3\xb2', 0.0), ('\xc3\xb0', 0.0),
                ('\xc3\xb6', 0.0), ('\xc3\xb4', 0.0), ('\xc4\x8f', 0.0), ('\xc4\x8d', 0.0), ('\xc4\x89', 0.0),
                ('\xc4\x87', 0.0), ('\xc4\x85', 0.0), ('\xc5\xaf', 0.0), ('\xc4\x9f', 0.0), ('\xc5\xbc', 0.0),
                ('\xc4\x9d', 0.0), ('\xc4\x9b', 0.0), ('\xc5\xba', 0.0), ('\xc4\x99', 0.0), ('\xc5\xad', 0.0),
                ('\xc5\xa1', 0.0), ('\xc4\xa5', 0.0), ('\xc3\xa3', 0.0), ('\xc5\x99', 0.0), ('\xc4\xb5', 0.0),
                ('\xc4\xb1', 0.0)],
    'English': [('e', 12.702), ('t', 9.056), ('a', 8.167), ('o', 7.507), ('i', 6.966), ('n', 6.749), ('s', 6.327),
                ('h', 6.094), ('r', 5.987), ('d', 4.253), ('l', 4.025), ('c', 2.782), ('u', 2.758), ('m', 2.406),
                ('w', 2.361), ('f', 2.228), ('g', 2.015), ('y', 1.974), ('p', 1.929), ('b', 1.492), ('v', 0.978),
                ('k', 0.772), ('j', 0.153), ('x', 0.15), ('q', 0.095), ('z', 0.074)],
    'Polish': [('a', 10.503), ('i', 8.328), ('e', 7.352), ('o', 6.667), ('n', 6.237), ('w', 5.813), ('r', 5.243),
               ('s', 5.224), ('z', 4.852), ('c', 3.895), ('d', 3.725), ('y', 3.206), ('k', 2.753), ('l', 2.564),
               ('m', 2.515), ('t', 2.475), ('p', 2.445), ('\xc5\x82', 2.109), ('u', 2.062), ('j', 1.836), ('b', 1.74),
               ('g', 1.731), ('\xc3\xb3', 1.141), ('\xc4\x99', 1.035), ('h', 1.015), ('\xc5\x9b', 0.814),
               ('\xc4\x87', 0.743), ('\xc5\xbc', 0.706), ('\xc4\x85', 0.699), ('\xc5\x84', 0.362), ('f', 0.143),
               ('\xc5\xba', 0.078), ('v', 0.012), ('x', 0.004), ('\xc5\x88', 0.0), ('\xc5\x9d', 0.0), ('\xc5\x9f', 0.0),
               ('\xc3\x9f', 0.0), ('\xc3\xb8', 0.0), ('\xc5\x93', 0.0), ('\xc3\xab', 0.0), ('\xc3\xaa', 0.0),
               ('\xc3\xa9', 0.0), ('\xc3\xa8', 0.0), ('\xc3\xaf', 0.0), ('\xc3\xae', 0.0), ('\xc3\xad', 0.0),
               ('\xc3\xac', 0.0), ('\xc5\xa5', 0.0), ('\xc3\xa2', 0.0), ('\xc3\xa1', 0.0), ('\xc3\xa0', 0.0),
               ('\xc3\xa7', 0.0), ('\xc3\xa6', 0.0), ('\xc3\xa5', 0.0), ('\xc3\xa4', 0.0), ('\xc3\xba', 0.0),
               ('\xc3\xb9', 0.0), ('\xc5\xbe', 0.0), ('\xc3\xbe', 0.0), ('\xc3\xbd', 0.0), ('\xc3\xbc', 0.0),
               ('\xc3\xb2', 0.0), ('\xc3\xb1', 0.0), ('\xc3\xb0', 0.0), ('\xc3\xb6', 0.0), ('\xc3\xb4', 0.0),
               ('\xc4\x8f', 0.0), ('\xc4\x8d', 0.0), ('\xc4\x89', 0.0), ('\xc5\xaf', 0.0), ('\xc4\x9f', 0.0),
               ('\xc4\x9d', 0.0), ('\xc4\x9b', 0.0), ('\xc5\xad', 0.0), ('\xc5\xa1', 0.0), ('\xc4\xa5', 0.0),
               ('q', 0.0), ('\xc3\xa3', 0.0), ('\xc5\x99', 0.0), ('\xc4\xb5', 0.0), ('\xc4\xb1', 0.0)],
    'Esperanto': [('a', 12.117), ('i', 10.012), ('e', 8.995), ('o', 8.779), ('n', 7.955), ('l', 6.104), ('s', 6.092),
                  ('r', 5.914), ('t', 5.276), ('k', 4.163), ('j', 3.501), ('u', 3.183), ('d', 3.044), ('m', 2.994),
                  ('p', 2.755), ('v', 1.904), ('g', 1.171), ('f', 1.037), ('b', 0.98), ('c', 0.776),
                  ('\xc4\x9d', 0.691), ('\xc4\x89', 0.657), ('\xc5\xad', 0.52), ('z', 0.494), ('\xc5\x9d', 0.385),
                  ('h', 0.384), ('\xc4\xb5', 0.055), ('\xc4\xa5', 0.022), ('\xc5\x88', 0.0), ('\xc5\x84', 0.0),
                  ('\xc5\x82', 0.0), ('\xc5\x9f', 0.0), ('\xc3\x9f', 0.0), ('\xc5\x9b', 0.0), ('\xc3\xb8', 0.0),
                  ('\xc5\x93', 0.0), ('\xc3\xab', 0.0), ('\xc3\xaa', 0.0), ('\xc3\xa9', 0.0), ('\xc3\xa8', 0.0),
                  ('\xc3\xaf', 0.0), ('\xc3\xae', 0.0), ('\xc3\xad', 0.0), ('\xc3\xac', 0.0), ('\xc5\xa5', 0.0),
                  ('\xc3\xa2', 0.0), ('\xc3\xa1', 0.0), ('\xc3\xa0', 0.0), ('\xc3\xa7', 0.0), ('\xc3\xa6', 0.0),
                  ('\xc3\xa5', 0.0), ('\xc3\xa4', 0.0), ('\xc3\xba', 0.0), ('\xc3\xb9', 0.0), ('\xc5\xbe', 0.0),
                  ('\xc3\xbe', 0.0), ('\xc3\xbd', 0.0), ('\xc3\xbc', 0.0), ('\xc3\xb3', 0.0), ('\xc3\xb2', 0.0),
                  ('\xc3\xb1', 0.0), ('\xc3\xb0', 0.0), ('\xc3\xb6', 0.0), ('\xc3\xb4', 0.0), ('\xc4\x8f', 0.0),
                  ('x', 0.0), ('\xc4\x8d', 0.0), ('\xc4\x87', 0.0), ('\xc4\x85', 0.0), ('\xc5\xaf', 0.0),
                  ('\xc4\x9f', 0.0), ('\xc5\xbc', 0.0), ('\xc4\x9b', 0.0), ('\xc5\xba', 0.0), ('\xc4\x99', 0.0),
                  ('\xc5\xa1', 0.0), ('q', 0.0), ('\xc3\xa3', 0.0), ('w', 0.0), ('y', 0.0), ('\xc5\x99', 0.0),
                  ('\xc4\xb1', 0.0)],
    'Italian': [('e', 11.792), ('a', 11.745), ('i', 10.143), ('o', 9.832), ('n', 6.883), ('l', 6.51), ('r', 6.367),
                ('t', 5.623), ('s', 4.981), ('c', 4.501), ('d', 3.736), ('p', 3.056), ('u', 3.011), ('m', 2.512),
                ('v', 2.097), ('g', 1.644), ('z', 1.181), ('f', 1.153), ('b', 0.927), ('h', 0.636), ('\xc3\xa0', 0.635),
                ('q', 0.505), ('\xc3\xa8', 0.263), ('\xc3\xb9', 0.166), ('w', 0.033), ('\xc3\xac', 0.03), ('y', 0.02),
                ('j', 0.011), ('k', 0.009), ('x', 0.003), ('\xc3\xb2', 0.002), ('\xc5\x88', 0.0), ('\xc5\x84', 0.0),
                ('\xc5\x82', 0.0), ('\xc5\x9d', 0.0), ('\xc5\x9f', 0.0), ('\xc3\x9f', 0.0), ('\xc5\x9b', 0.0),
                ('\xc3\xb8', 0.0), ('\xc5\x93', 0.0), ('\xc3\xab', 0.0), ('\xc3\xaa', 0.0), ('\xc3\xa9', 0.0),
                ('\xc3\xaf', 0.0), ('\xc3\xae', 0.0), ('\xc3\xad', 0.0), ('\xc5\xa5', 0.0), ('\xc3\xa2', 0.0),
                ('\xc3\xa1', 0.0), ('\xc3\xa7', 0.0), ('\xc3\xa6', 0.0), ('\xc3\xa5', 0.0), ('\xc3\xa4', 0.0),
                ('\xc3\xba', 0.0), ('\xc5\xbe', 0.0), ('\xc3\xbe', 0.0), ('\xc3\xbd', 0.0), ('\xc3\xbc', 0.0),
                ('\xc3\xb3', 0.0), ('\xc3\xb1', 0.0), ('\xc3\xb0', 0.0), ('\xc3\xb6', 0.0), ('\xc3\xb4', 0.0),
                ('\xc4\x8f', 0.0), ('\xc4\x8d', 0.0), ('\xc4\x89', 0.0), ('\xc4\x87', 0.0), ('\xc4\x85', 0.0),
                ('\xc5\xaf', 0.0), ('\xc4\x9f', 0.0), ('\xc5\xbc', 0.0), ('\xc4\x9d', 0.0), ('\xc4\x9b', 0.0),
                ('\xc5\xba', 0.0), ('\xc4\x99', 0.0), ('\xc5\xad', 0.0), ('\xc5\xa1', 0.0), ('\xc4\xa5', 0.0),
                ('\xc3\xa3', 0.0), ('\xc5\x99', 0.0), ('\xc4\xb5', 0.0), ('\xc4\xb1', 0.0)]}


def get_frequencies_dict():
    """Parse frequencies_table.txt file"""
    frequencies = {}
    try:
        path = os.path.realpath(__file__)
        pos = path[::-1].index('/')
        with open(path[:-pos] + 'data/frequencies_table.txt') as f:
            languages = f.readline().split('\t')
            i = 0
            for lang in languages:
                lang = lang.replace('\n', '')
                frequencies[lang] = {}
                frequencies[lang]['nr'] = i
                i += 1
            frequencies.pop('Letter')
            for line in f:
                line = line.split('\t')
                let = line[0]
                line.remove(let)
                i = 1
                for letter_freuqency in line:
                    for dic_lang in frequencies:
                        if i == frequencies[dic_lang]['nr']:
                            frequencies[dic_lang][
                                string.lower(let)] = float(letter_freuqency)
                            i += 1
                            break
        for dic_lang in frequencies:
            frequencies[dic_lang].pop('nr')
            sorted_lang = sorted(
                frequencies[dic_lang].items(), key=operator.itemgetter(1), reverse=True)
    except Exception as msg:
        print(msg)
    return frequencies


def get_frequencies(a):
    """Calculate letter frequencies in given string"""
    result = {}
    for letter in a:
        letter = string.lower(letter)
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    for letter in result:
        result[letter] /= float(len(a))
    return result


def compare_by_frequencies(a, b, lang='English', no_of_comparisons=5):
    """Check which text have more similar letter frequencies (compared to language)
    todo: add words, diagraphs etc...

    Args:
        a(string)
        b(string)
        lang(string)
        no_of_comparisons(int): how much letters compare

    Returns:
        int: -1 if a is less similar than b, 0 if equal, 1 if a is more similar
    """
    if lang not in frequencies:
        log.critical_error("[-] Can't find language {}".format(lang))
    language_frequencies = frequencies[lang][:no_of_comparisons]

    freq = {a: get_frequencies(a), b: get_frequencies(b)}
    result = {a: 0, b: 0}

    for freq_tuple in language_frequencies:
        letter = freq_tuple[0]
        letter_frequency = freq_tuple[1]
        for word in [a, b]:
            if letter not in freq[word]:
                result[word] += letter_frequency
            else:
                result[word] += abs(freq[word][letter] - letter_frequency)

    if result[a] < result[b]:  # less means that is closer to language frequencies
        return 1
    elif result[a] > result[b]:
        return -1
    else:
        return 0


def break_one_char_key(ciphertext, lang='English', no_of_comparisons=5, alphabet=False, key_space=False,
                       reliability=100.0):
    """Brute for all one-char keys, return most language-like

    Args:
        ciphertext(string): text xored with short key
        lang(string): key in frequencies dict
        no_of_comparisons(int): used during comparing by frequencies
        alphabet(string/None): plaintext space
        key_space(string/None): key space
        reliability(float): between 0 and 100, used during comparing by frequencies

    Returns:
        list: sorted (by frequencies) list of tuples (key, plaintext)
    """
    if not alphabet:
        alphabet = string.printable
    if not key_space:
        key_space = map(chr, range(256))

    result = {}
    for key in key_space:
        xored = xor(ciphertext, key)
        if is_printable(xored, alphabet=alphabet, reliability=reliability):
            result[key] = xored
    if result:
        return sorted(result.items(), key=operator.itemgetter(1), reverse=True,
                      cmp=lambda x, y: compare_by_frequencies(x, y, lang=lang, no_of_comparisons=no_of_comparisons))
    return False


def guess_key_size(ciphertext, max_key_size=40):
    """Given sentence xored with short key, guess key size
    From: http://trustedsignal.blogspot.com/2015/06/xord-play-normalized-hamming-distance.html

    Args:
         ciphertext(string)
         max_key_size(int)

    Returns:
        list: sorted list of tuples (key_size, probability),
        note that most probable key size not necessary have the largest probability
    """
    if not max_key_size:
        max_key_size = len(ciphertext)/4

    result = {}
    for key_size in range(1, max_key_size):
        blocks = re.findall('.' * key_size, ciphertext, re.DOTALL)
        if len(blocks) < 2:
            break

        diff = i = 0
        while i < len(blocks) - 1:
            if len(blocks[i]) != len(blocks[i + 1]):  # not full-length block
                break
            diff += hamming_distance(blocks[i], blocks[i + 1])
            i += 1
        result[key_size] = diff / float(i)  # average
        result[key_size] /= float(key_size)  # normalize
    result = sorted(result.items(), key=operator.itemgetter(1))

    # now part from given link, case one
    # gcd12 = gcd(result[0][0], result[1][0])
    # gcd13 = gcd(result[0][0], result[2][0])
    # gcd23 = gcd(result[1][0], result[2][0])
    # print gcd12, gcd13, gcd23
    # if (gcd12 != 1) and (gcd12 in [x[0] for x in result[:5]]):
    #     if (gcd12 == gcd13 and gcd12 == gcd23) or (gcd12 == result[0][0] or gcd12 == result[1][0]):
    #         #remove key_size == gcd12 from result list and add it to the beginning
    #         for x in result:
    #             if x[0] == gcd12:
    #                 result.remove(x)
    #                 break
    #         result[0] == (gcd12, 1.0)

    # from link, case two; yep, black magic it is
    gcd_frequencies = defaultdict(lambda: 0)
    for gcd_pairs in itertools.combinations(result[:10], 2):
        gcd_tmp = gcd(gcd_pairs[0][0], gcd_pairs[1][0])
        gcd_frequencies[gcd_tmp] += 1
    gcd_frequencies = sorted(gcd_frequencies.items(), key=operator.itemgetter(1), reverse=True)

    key_sizes = [x[0] for x in result[:10]]
    distances = [x[1] for x in result[:10]]
    for guessed_most_probable_key_size in gcd_frequencies[:5]:
        if guessed_most_probable_key_size[0] != 1 and guessed_most_probable_key_size[1] != 0 and \
                        guessed_most_probable_key_size[0] in key_sizes:
            gmks_position = result[key_sizes.index(guessed_most_probable_key_size[0])]
            if gmks_position[1] < max(distances):
                result.remove(gmks_position)
                result = [gmks_position] + result
    log.info("Guessed key size: {}".format(result))
    return result


def break_repeated_key(ciphertext, lang='English', no_of_comparisons=5, key_size=None, max_key_size=40,
                       alphabet=None, key_space=None, reliability=100.0):
    """Short key encrypted with long plaintext

    Args:
        ciphertext(string): text xored with short key
        lang(string): key in frequencies dict
        no_of_comparisons(int): used during comparing by frequencies
        key_size(int/None)
        max_key_size(int/None)
        alphabet(string/None): plaintext space
        key_space(string/None): key space
        reliability(float): between 0 and 100, used during comparing by frequencies

    Returns:
        list: sorted (by frequencies) list of tuples (key, plaintext)
    """
    if not key_size:
        key_size = guess_key_size(ciphertext, max_key_size)[0][0]

    cipher_same_key_char = [ciphertext[i::key_size] for i in range(key_size)]
    key = {}
    for position, item in enumerate(cipher_same_key_char):
        key_char = break_one_char_key(item, lang=lang, no_of_comparisons=no_of_comparisons, alphabet=alphabet,
                                      key_space=key_space, reliability=reliability)
        if not key_char:
            continue
        key_char = key_char[0]  # get only most probable, because product may be large
        key[position] = key_char

    key = [x[1] for x in key.items()]
    key = [x[0] for x in key]
    if not key:
        return False

    plaintexts = {}
    for guessed_key in itertools.product(*key):
        guessed_key = ''.join(guessed_key)
        plaintexts[guessed_key] = xor(guessed_key, ciphertext)
    return sorted(plaintexts.items(), key=operator.itemgetter(1), reverse=True,
                  cmp=lambda x, y: compare_by_frequencies(x, y, lang=lang, no_of_comparisons=no_of_comparisons))


def break_reuse_key(ciphertexts, lang='English', no_of_comparisons=5, alphabet=None,
                    key_space=None, reliability=100.0):
    """Sentences xored with the same key

    Args:
        ciphertexts(list): texts xored with the same key
        lang(string): key in frequencies dict
        no_of_comparisons(int): used during comparing by frequencies
        alphabet(string/None): plaintext space
        key_space(string/None): key space
        reliability(float): between 0 and 100, used during comparing by frequencies

    Returns:
        list: sorted (by frequencies) list of tuples (key, list(plaintexts))
    """
    if len(ciphertexts) < 2:
        log.critical_error("Too less ciphertexts")

    min_size = min(map(len, ciphertexts))
    ciphertexts = map(lambda one: one[:min_size], ciphertexts)
    log.info("Ciphertexts shrinked to {} bytes".format(min_size))

    pairs = break_repeated_key(''.join(ciphertexts), lang=lang, no_of_comparisons=no_of_comparisons, key_size=min_size,
                               alphabet=alphabet, key_space=key_space, reliability=reliability)

    res = map(lambda pair: (pair[0], chunks(pair[1], min_size)), pairs)
    return res


def break_rot(ciphertext, alphabet=string.lowercase):
    for rot in range(len(alphabet)):
        tr = string.maketrans(alphabet, ''.join([alphabet[rot:], alphabet[:rot]]))
        print(rot, string.translate(ciphertext, tr))