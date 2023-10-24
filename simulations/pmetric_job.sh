#!/bin/bash
#$ -N normal_simulation
#$ -l h_vmem=3G
#$ -t 5-6:1
#$ -cwd
#$ -S /bin/bash
#$ -o "/data/origami/niusha/$JOB_NAME/out/$JOB_NAME_$TASK_ID.out"
#$ -e "/data/origami/niusha/$JOB_NAME/err/$JOB_NAME_$TASK_ID.err"

# script=$1
# INPUTFILENAME=$2

script=simulations/normal_simulation_different_effectsize_samplesize.py
INPUTFILENAME=simulation_combinations.csv

home_dir="/data/origami/niusha"
PARENT_DIR="${home_dir}/$JOB_NAME"

if [ ! -d "$PARENT_DIR" ]
then 
    echo "Parent directory does not exist"
fi

export SGE_TASK_ID
echo $SGE_TASK_ID hey

singularity exec -e --bind ${home_dir}/code/pvalue-metric-b:/mnt/code \
            --bind $PARENT_DIR:/mnt/output \
            ${home_dir}/pmetric_python.sif \
            python3 /mnt/code/${script} "$SGE_TASK_ID" "$INPUTFILENAME"

# simulations/normal_simulation_different_effectsize_samplesize.py
# simulation_combinations.csv

#qsub 