Dog Breed Classifier

This project uses a Convolutional Neural Network (CNN) model to classify images of dogs. It compares the classified results with the actual labels of the images and calculates statistics to help determine the effectiveness of the model.

Table of Contents
Installation
Usage
Project Structure
Functions
Result Files
Example Commands
Installation:
- Before running the scripts, ensure you have the necessary dependencies installed. The main dependency is torchvision.
- To install torchvision, run: pip install torchvision

Usage
The primary script for running the image classification is check_images.py. This script requires three inputs:

--dir: Directory with images
--arch: CNN model architecture (e.g., vgg, alexnet, resnet)
--dogfile: File that contains dog names

Example Command:
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt

If no arguments are provided, the program will default to:
pet_images directory
vgg architecture
dognames.txt file


Project Structure: 
Dog_breed_classifier
│
├── cd0184
   └── contents
       └── data
           ├── pet_images/
           ├── uploaded_images/
           ├── adjust_results4_isadog.py
           ├── alexnet_uploaded-images.txt
           ├── calculates_results_stats.py
           ├── check_images.py
           ├── classifier.py
           ├── classify_images.py
           ├── dognames.txt
           ├── get_input_args.py
           ├── get_pet_labels.py
           ├── imagenet1000_clsid_to_human.txt
           ├── print_results.py
           ├── resnet_uploaded-images.txt
           ├── run_models_batch.sh
           ├── vgg_uploaded-images.txt
           └── Readme



Functions
- adjust_results4_isadog.py: Adjusts the results to determine if the label is a dog.
- calculates_results_stats.py: Calculates statistics of the results.
- classifier.py: Contains the CNN model. 
- classify_images.py: Classifies images using the specified CNN model.
- get_input_args.py: Parses command-line arguments.
- get_pet_labels.py: Extracts pet labels from the images.
- print_results.py: Prints the results in a formatted manner.

Result Files

The project generates result files for each architecture tested with the uploaded images:
- resnet_uploaded-images.txt
- alexnet_uploaded-images.txt
- vgg_uploaded-images.txt
- These files contain the classification results for images tested using different CNN architectures.

Example Commands:
- Running the Primary Script
- python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
- Alternatively python check_images.py will do the same as the above command as default


Running the Batch Script:

If you want to add a batch script named run_models_batch.sh, you can run it as follows:
- If using vsCode change launch profile to git bash
- ./run_models_batch.sh
- Make sure to navigate to the directory containing the script before running the command
