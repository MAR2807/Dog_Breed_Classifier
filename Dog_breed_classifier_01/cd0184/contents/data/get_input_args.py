#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Mohamed R
# DATE CREATED:  6/22/2024                               
# REVISED DATE:  7/01/2024
# PURPOSE: A function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

def get_input_args():

    # Creates Parse using ArgumentParser
    parser = argparse.ArgumentParser(description = "Arguments")
    
    # Creates 3 command line arguments as mentioned above using add_argument() from ArguementParser method
    parser.add_argument("--dir", type=str, default="pet_images")
    parser.add_argument("--arch", type=str, default="vgg")
    parser.add_argument("--dogfile", type=str, default="dognames.txt")
  
    return parser.parse_args()
