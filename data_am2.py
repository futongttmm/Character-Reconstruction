# yield# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 17:40:29 2019

@author: yeap
"""
from itertools import chain

    
# Create the training patterns
    
a_pattern =  [
                  [0, 0, 1, 0, 0],
                  [0, 1, 0, 1, 0],
                  [1, 0, 0, 0, 1],
                  [1, 1, 1, 1, 1],
                  [1, 0, 0, 0, 1],
                  [1, 0, 0, 0, 1],
                  [1, 0, 0, 0, 1],
             ]

u_pattern =  [
                  [1, 0, 0, 0, 1],
                  [1, 0, 0, 0, 1],
                  [1, 0, 0, 0, 1],
                  [1, 0, 0, 0, 1],
                  [1, 0, 0, 0, 1],
                  [1, 0, 0, 0, 1],
                  [1, 1, 1, 1, 1], 
             ]

t_pattern =  [
                  [1, 1, 1, 1, 1],
                  [0, 0, 1, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 1, 0, 0],
             ]


s_pattern =  [
                  [1, 1, 1, 1, 1],
                  [1, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 1],
                  [1, 1, 1, 1, 1],
             ]


a_list = list(chain.from_iterable(a_pattern))


u_list = list(chain.from_iterable(u_pattern))


t_list = list(chain.from_iterable(t_pattern))


s_list = list(chain.from_iterable(s_pattern))

 

data  = [   
                a_list,
                u_list,
                t_list,
                s_list,
        ]

desired  = [   
                a_list,
                u_list,
                t_list,
                s_list,
            ]