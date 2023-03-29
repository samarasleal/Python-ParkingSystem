#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 17:16:09 2017

@author: samara
"""

from cx_Freeze import setup, Executable
 
setup(
      name = 'InterfacePrincipal', 
      version = '1.0',
      options = {'build_exe': {
              'packages': ['tkinter','PIL', 'pymysql', 'datetime']}},
      executables = [Executable(
                   script='setup.py',
                   base=None,
                   icon='carro.ico')]
      )


