#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Mohamed R
# DATE CREATED:  6/22/2024                               
# REVISED DATE:  7/01/2024
# PURPOSE: A function: adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog.
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. It will add
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list.
#
##
 
def adjust_results4_isadog(results_dic, dogfile):
  #read dogfile into a dictionary with key being dogname and value being 1 to indicate it is a dog
  #check if pet_image_label is of dog
  #check if classifier label is of dog
  #append results_dic values with index 3 and 4 with values 0 or 1 
  dog_names = []

  with open(dogfile, 'r') as file:
    for line in file:
      dog_names.append(line.lower().strip())

  
  

  for filename, pet_info in results_dic.items():

    classification_label_formatted = [word.strip().lower() for word in pet_info[1].split(',')]
    pet_label_formatted = pet_info[0].lower().strip()
    
    if pet_label_formatted in dog_names and any(word in dog_names for word in classification_label_formatted):
       results_dic[filename].extend([1,1])
    elif pet_label_formatted in dog_names and all(word not in dog_names for word in classification_label_formatted):
      results_dic[filename].extend([1,0])
    elif pet_label_formatted not in dog_names and any(word in dog_names for word in classification_label_formatted) :
      results_dic[filename].extend([0,1])
    else:
      results_dic[filename].extend([0,0])

  None
