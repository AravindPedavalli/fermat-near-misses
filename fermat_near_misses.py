#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Fermat's Last Theorem Near Misses
# File: fermat_near_misses.py
# External Files: None
# Created By: Aravind Pedavalli & Venkat Reddy Kusukuntla
# Emails: AravindPedavalli@lewisu.edu & venkatreddykusukun@lewisu.edu
# Course: SU24-CPSC-60500-001 - Software Engineering
# Group: Assignment 1 Group 07
# Date: 07/28/2024
# Description: This program finds near misses for Fermat's Last Theorem for given n and k.
# Resources: https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem, https://www.youtube.com/watch?v=ReOQ300AcSU, 

def find_near_misses(n, k):
    """Function to find near misses for Fermat's Last Theorem"""
    smallest_relative_miss = float('inf')
    best_x, best_y, best_z = None, None, None

    for x in range(10, k + 1):
        for y in range(10, k + 1):
            # Calculate x^n + y^n
            sum_xy_n = x**n + y**n
            # Estimate z such that z^n is close to x^n + y^n
            z = int(sum_xy_n ** (1/n))
            z_n = z**n
            z_plus_1_n = (z + 1)**n

            # Calculate misses
            miss = min(abs(sum_xy_n - z_n), abs(z_plus_1_n - sum_xy_n))
            relative_miss = miss / sum_xy_n

            # Check if we found a new smallest relative miss
            if relative_miss < smallest_relative_miss:
                smallest_relative_miss = relative_miss
                best_x, best_y, best_z = x, y, z

            # Output the current results
            print(f"x={x}, y={y}, z={z}, actual miss={miss}, relative miss={relative_miss:.6f}")

    # Print the smallest miss at the end
    print(f"\nSmallest relative miss: x={best_x}, y={best_y}, z={best_z}, relative miss={smallest_relative_miss:.6f}")

if __name__ == "__main__":
    # Input for n and k
    n = int(input("Enter the power n (2 < n < 12): "))
    k = int(input("Enter the range limit k (k > 10): "))
    find_near_misses(n, k)


# In[ ]:




