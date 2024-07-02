#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Mohamed R
# DATE CREATED:  6/22/2024                               
# REVISED DATE:  7/01/2024
# PURPOSE: A function: classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. It will add the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 
import os


def classify_images(images_dir, results_dic, model):
    #call the classifier.py function and pass the necessary inputs
    # take the output from the classifier.py function store it into string: classifier_labels
    # compare the classifier labels to the pet labels
    #  append value to matched labels index 1 being the classifier label and index 2 being a 1 or 0 if there was a match

    
    for filename, pet_info in results_dic.items():
      file_path = os.path.join(images_dir,filename)

      pet_label = pet_info[0].lower().strip()

      classifier_labels = classifier(file_path, model)

      formatted_classifier_labels = classifier_labels.lower().strip()
      

      if pet_label in formatted_classifier_labels:
         results_dic[filename].extend([classifier_labels, 1])
      else:
         results_dic[filename].extend([classifier_labels, 0])
    

    None 