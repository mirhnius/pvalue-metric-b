#!/bin/bash
#$ -N simulation
#$ -l h_vmem=7G
#$ -t 1-50:1
#$ -cwd
#$ -S /bin/bash
#$ -o "/data/origami/niusha/$JOB_NAME/out/$JOB_NAME_$TASK_ID.out"
#$ -e "/data/origami/niusha/$JOB_NAME/err/$JOB_NAME_$TASK_ID.err"

home_dir="/data/origami/niusha"
PARENT_DIR="${home_dir}/$JOB_NAME"

if [ ! -d "$PARENT_DIR" ]
then 
    echo "Parent directory does not exist"
fi

# line_number=$(echo "$SGE_TASK_ID + 1" | bc)

INPUTFILE="$PARENT_DIR/filenames.txt"
line=$(cut -f $SGE_TASK_ID -d $'\n' $INPUTFILE)

INPUTFILENAME="${INPUTFILES[$SGE_TASK_ID -1]}"
DESTINATION_DIR="${PARENT_DIR}/test-$SGE_TASK_ID"

if [ ! -d "$DESTINATION_DIR" ]
then 
    mkdir -p $DESTINATION_DIR
fi


# cp $INPUTFILENAME $DESTINATION_DIR
cd $DESTINATION_DIR

#Run the program
export SGE_TASK_ID
export line


singularity exec --bind ${home_dir}/code/pmetric:/mnt/code \
--bind ${home_dir}/pmetric_input:/mnt/input:ro \
--bind ${home_dir}/pemetric_outputs:/mnt/out \
${home_dir}/pmetric_python.sif \
python /mnt/code/normal_simulation_different_effectsize_samplesize.py 


# mv  ${DESTINATION_DIR}/melodic_Tmodes ${DESTINATION_DIR}/Tmodes
# rm ${DESTINATION_DIR}/eigenvalues_percent
# find ${DESTINATION_DIR} -maxdepth 1 -type f -name "melodic*" -delete
# find ${DESTINATION_DIR} -maxdepth 1 -type f -name "*.nii.gz" -delete 
