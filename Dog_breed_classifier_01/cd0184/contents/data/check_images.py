#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
#                                                                              
# PROGRAMMER: Mohamed R
# DATE CREATED: 6/22/2024                                 
# REVISED DATE: 7/01/2024
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time, sleep


# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    
    # Measures total program runtime by collecting start time
    start_time = time()
    
    in_arg = get_input_args()



    
    
    # This function creates the results dictionary that contains the results, 
    # this dictionary is returned from the function call as the variable results
    results = get_pet_labels(in_arg.dir)



  
    # Creates Classifier Labels with classifier function, Compares Labels, 
    # and adds these results to the results dictionary - results
    classify_images(in_arg.dir, results, in_arg.arch)

   

    
 
    # Adjusts the results dictionary to determine if classifier correctly 
    # classified images as 'a dog' or 'not a dog'. This demonstrates if 
    # model can correctly classify dog images as dogs (regardless of breed)
    adjust_results4_isadog(results, in_arg.dogfile)



   

    # dictionary is returned from the function call as the variable results_stats    
    # Calculates results of run and puts statistics in the Results Statistics
    # Dictionary - called results_stats
    results_stats = calculates_results_stats(results)


  
    # Prints summary results, incorrect classifications of dogs (if requested)
    # and incorrectly classified breeds (if requested)
    print_results(results, results_stats, in_arg.arch, True, True)
    
    # Measure total program runtime by collecting end time
    end_time = time()
    
    # Computes overall runtime in seconds & prints it in hh:mm:ss format
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )
    

# Call to main function to run the program
if __name__ == "__main__":
    main()
