#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Mohamed R
# DATE CREATED:  6/22/2024                               
# REVISED DATE:  7/01/2024
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
import re

def get_pet_labels(image_dir):

    results_dic = {}

    for filename in listdir(image_dir):

      label_words = filename.split('.')[0].lower().replace('_',' ').strip()

      pet_label = re.sub(r'\d+', '', label_words)
      results_dic[filename] = [pet_label]

    # iterate through pet_images
    # format it in lower case and without leading and trailing whitespace 
    # add all file names to results_dic
    # return results_dic


    return results_dic
