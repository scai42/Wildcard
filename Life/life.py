# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    life.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: scai <marvin@42.fr>                        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/05 02:57:11 by scai              #+#    #+#              #
#    Updated: 2019/09/05 02:58:18 by scai             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import sys
import time
import pygame
from random import getrandbits
from sys import exit
from utils import Timer

"""
variables
"""
power = 1:10
wealth = 1:10
fame = 1:10

"""
design
"""
CGREEN2 = '\33[92m'
CBLUEG2 = '\33[104m'
CREDBG  = '\33[41m'
UNDERLINE = '\033[4m'

"""
routines
"""

def birth():
    print("You are born.")
    print('\x1b[6;30;42m' + 'Planet Earth is home to 7.7 billion people.' + '\x1b[0m')
    print "Enter a digit between 1 and 10."

    home = raw_input("   ")
    time.sleep(0.5)
    print('')

