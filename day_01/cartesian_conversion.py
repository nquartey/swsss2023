# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 14:58:57 2023

A 3D plot script for spherical coordinates
"""
import numpy as np
import matplotlib.pyplot as plt


__author__ = 'Nii-Boi Quartey'
__email__ = 'nquartey@umich.edu'

def spherical_conversion(r, theta, phi):
    '''
    Converts spherical coordinates to cartesian coordinates
    '''
    
    x = r*np.sin(theta)*np.cos(phi)
    y = r*np.sin(theta)*np.sin(phi)
    z = r*np.cos(phi)

    return (x, y, z)


#3D plot
fig = plt.figure()
axes = fig.add_subplot(projection = '3d')
r = np.linspace(0, 2*np.pi)
theta = np.linspace(0, 2*np.pi)
phi = np.linspace(0, 2*np.pi)
x, y, z = spherical_conversion(r, theta, phi)
axes.plot(x, y, z)
plt.title('Spherical to Cartesian Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

#Unit testing
assert np.allclose(spherical_conversion(1, 0, 0), (0, 0, 1)), 'Error'
assert np.allclose(spherical_conversion(1, np.pi, np.pi), (0, 0, -1)), 'Error'
assert np.allclose(spherical_conversion(1, 2*np.pi, 2*np.pi), (0, 0, 1)), 'Error'
assert np.allclose(spherical_conversion(1, -np.pi, -2*np.pi), (0, 0, 1)), 'Error'
assert np.allclose(spherical_conversion(1, -2*np.pi, np.pi), (0, 0, -1)), 'Error'