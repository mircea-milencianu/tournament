#!/bin/bash

#BSUB -J all_strategies_run
#BSUB -e error_%J.txt
#BSUB –o output_%J.txt
#BSUB -n 16
#BSUB -R "span[ptile=20]"
#BSUB –q strategies_queue 

python full_tour.py