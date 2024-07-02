#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Mohamed R
# DATE CREATED:  6/22/2024                               
# REVISED DATE:  7/01/2024
# PURPOSE: A function: calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages.   
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary contains the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images 
#            n_notdogs_img - number of NON-dog images 
#            n_match - number of matches between pet & classifier labels 
#            n_correct_dogs - number of correctly classified dog images 
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##

def calculates_results_stats(results_dic):
    results_stats_dic = {}

    n_correct_breed = 0
    



    n_images = len(results_dic)
    n_dogs_img = sum(1 for value in results_dic.values() if value[3] == 1)
    
    n_match = sum(1 for value in results_dic.values() if value[2] == 1)
    n_correct_dogs = sum(1 for value in results_dic.values() if value[4] == 1 and value[3]==1)
    n_correct_notdogs = sum(1 for value in results_dic.values() if value[4] == 0)
    n_correct_breed = sum(1 for value in results_dic.values() if value[3] == 1 and value[2] == 1)
    

    n_notdogs_img = n_images - n_dogs_img

    pct_match = (n_match / n_images) * 100 if n_images > 0 else 0
    pct_correct_dogs = (n_correct_dogs / n_dogs_img) * 100 if n_dogs_img > 0 else 0
    pct_correct_breed = (n_correct_breed / n_dogs_img) * 100 if n_dogs_img > 0 else 0
    pct_correct_notdogs = (n_correct_notdogs / n_notdogs_img) * 100 if n_notdogs_img > 0 else 0


    results_stats_dic['n_images'] = n_images
    results_stats_dic['n_dogs_img'] = n_dogs_img
    results_stats_dic['n_notdogs_img'] = n_notdogs_img
    results_stats_dic['n_match'] = n_match
    results_stats_dic['n_correct_dogs'] = n_correct_dogs
    results_stats_dic['n_correct_notdogs'] = n_correct_notdogs
    results_stats_dic['n_correct_breed'] = n_correct_breed
    results_stats_dic['pct_match'] = pct_match
    results_stats_dic['pct_correct_dogs'] = pct_correct_dogs
    results_stats_dic['pct_correct_breed'] = pct_correct_breed
    results_stats_dic['pct_correct_notdogs'] = pct_correct_notdogs
   
    return results_stats_dic
