#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:57:10 2019

@author: michal
"""

from graphManager import GraphManager
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sm = GraphManager()
        sm.printStatus()
    else:
        sm = GraphManager()
        sm.printStatus(True)
    
