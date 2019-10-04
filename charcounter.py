
import os
import argparse
import logging
import time
import numpy as np
import matplotlib.pyplot as plt 

logging.basicConfig(level=logging.INFO)

#starts to measure elapsed time
start_time = time.time()

_description = 'Measure the relative frequences of letters in a text book'

def process(file_path):
    """Main processing routine"""
    """checks on input: it makes sure the file exists"""
    assert file_path.endswith('.txt')
    assert os.path.isfile(file_path)

    """Context managment"""
    logging.info('Opening file %s...', file_path)
    with open(file_path) as input_file:
        data = input_file.read()
    logging.info('Done. %d characters found', len(data))
    num_occ=len(data)
   


    #creates a dictionary with all the alphabet letters as keys
    #initialize the count to zero for each letter
    letters = 'abcdefghijklmnopqrstuvxywz'
    occurrences = {}
    #loops over the text book
    for ch in letters:
        occurrences[ch] = 0
    #casts everything in lower case and counts
    for ch in data.lower():
        if ch in letters:
            occurrences[ch] +=  1
    #print(occurrences)
    
    #creates a dictionary with relative frequences 
    occ_rel={}
    #loops to measure the relative frequences
    for ch in letters:
        occ_rel[ch]=occurrences[ch]/num_occ
    #print(occ_rel)
    
    #measures elapsed time and prints
    elapsed_time = time.time()-start_time
    print("Elapsed time: ", elapsed_time)
    
    
    #creates an histogram using the keys and the values from the dictionary
    plt.bar(list(occ_rel.keys()), occ_rel.values(), color='g')
    plt.title('Histogram of relative frequences')
    plt.xlabel('letters')
    plt.ylabel('relative frequences')
    plt.show()
        
    
    
    
if __name__=='__main__':
    parser = argparse.ArgumentParser(description=_description)
    parser.add_argument('infile', help='path to the input text file')
    args = parser.parse_args()
    process(args.infile)
    
