
import os
import argparse
import logging
import time
import numpy as np
import matplotlib.pyplot as plt 

logging.basicConfig(level=logging.INFO)
start_time = time.time()
_description = 'Misura le occorrenze relative delle lettere in un file'

def process(file_path):
    """Main processing routine"""
    """controlli sull'input: se tali condizioni non sono verificate 
    il programma si interrompe"""
    assert file_path.endswith('.txt')
    assert os.path.isfile(file_path)

    """Context managment"""
    logging.info('Opening file %s...', file_path)
    with open(file_path) as input_file:
        data = input_file.read()
    logging.info('Done. %d caratteri trovati', len(data))
    num_occ=len(data)
   


    #inizializza un dizionario
    letters = 'abcdefghijklmnopqrstuvxywz'
    occorrenze = {}
    for ch in letters:
        occorrenze[ch] = 0
    for ch in data.lower():
        if ch in letters:
            occorrenze[ch] +=  1
            #occorrenze_rel=occorrenze[ch]/num_occ
    print(occorrenze)
    occorrenze_rel={}
    for ch in letters:
        occorrenze_rel[ch]=occorrenze[ch]/num_occ
    print(occorrenze_rel)
    
    with open("occ.txt", "w") as f:
        f.write("{}\n".format("\n".join([str(n) for n in occorrenze.values()])))
    
    #create histogram from dictionary
    plt.bar(list(occorrenze.keys()), occorrenze.values(), color='g')
    plt.show()
        
    
        
    
if __name__=='__main__':
    parser = argparse.ArgumentParser(description=_description)
    parser.add_argument('infile', help='path to the input text file')
    args = parser.parse_args()
    process(args.infile)
    

elapsed_time = time.time()-start_time
print('Elapsed time: ', elapsed_time)