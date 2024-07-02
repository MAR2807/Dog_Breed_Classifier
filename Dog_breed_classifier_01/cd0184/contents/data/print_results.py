#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Mohamed Rafeek
# DATE CREATED:  6/22/2024                               
# REVISED DATE:  7/01/2024
# PURPOSE: A function: print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#           also allows the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):

        print(f"\n Model Architecture: {model}")

        print("\n Statistics:")          
        for key, value in results_stats_dic.items():
               if(key.startswith('p')):
                        print(f"{key:}: {value:.2f}")



        if print_incorrect_dogs and ((results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs']) != results_stats_dic['n_images']):
                print("Misclassified dogs:")
                for filename, pet_info in results_dic.items():
                     if pet_info[3] != pet_info[4] :
                        print("Real: {:26} Classifier: {:30}".format(pet_info[0], pet_info[1]))


        if print_incorrect_breed and results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']:
                print("Misclassified breeds:")
                for filename, pet_info in results_dic.items():                 
                    if pet_info[3] == 1 and pet_info[4] == 1 and pet_info[2] == 0:
                      print("Real: {:26} Classifier: {:30}".format(pet_info[0], pet_info[1]))


None
                
