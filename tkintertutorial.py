#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:19:43 2023

@author: ozgurseker
"""

import tkinter as tk 
import colors as c

class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")
        self.main_grid = tk.Frame(
            self, bg=c.GRID_COLOR, bd=3, width=600, height=600
        )
        self.main_grid.grid(pady=(100,0))
        
    



