# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Scalene','5,3,4 is a Right Scalene triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testRightTriangleA1(self):
        self.assertEqual(classify_triangle(5,12,13),'Right','5,12,13 is a Right triangle')
    
    def testInvalidInput(self):
        self.assertEqual(classify_triangle(3,4,8),'NotATriangle','3,4,8 is not a triangle')

    def testInvalidInput1(self):
        self.assertEqual(classify_triangle(201,4,6),'InvalidInput','a_side is > 200')

    def testInvalidInput2(self):
        self.assertEqual(classify_triangle(3,-4,6),'InvalidInput','b_side is < 0')

    def testInvalidInput3(self):
        self.assertEqual(classify_triangle(3,4,89.9),'InvalidInput','c_side is not integer')
    
    def testIsocelesTriangle(self):
        self.assertEqual(classify_triangle(4,4,6),'Isoceles','a_side is equal to b_side')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

