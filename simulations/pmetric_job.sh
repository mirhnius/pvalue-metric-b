#!/bin/bash
#$ -N simulation
#$ -l h_vmem=7G
#$ -t 1-50:1
#$ -cwd
#$ -S /bin/bash
#$ -o "/data/origami/niusha/$JOB_NAME/out/$JOB_NAME_$SGE_TASK_ID.out"
#$ -e "/data/origami/niusha/$JOB_NAME/err/$JOB_NAME_$SGE_TASK_ID.err"

script=$1
INPUTFILENAME=$2

home_dir="/data/origami/niusha"
PARENT_DIR="${home_dir}/$JOB_NAME"

if [ ! -d "$PARENT_DIR" ]
then 
    echo "Parent directory does not exist"
fi

#Run the program
export SGE_TASK_ID
export INPUTFILENAME

singularity exec -e --bind ${home_dir}/code/pmetric:/mnt/code \
            --bind $PARENT_DIR:/mnt/out \
            ${home_dir}/pmetric_python.sif \
            python3 /mnt/code/${script} 
