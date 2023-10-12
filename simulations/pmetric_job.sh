#!/bin/bash
#$ -N simulation
#$ -l h_vmem=7G
#$ -t 1-50:1
#$ -cwd
#$ -S /bin/bash
#$ -o "/data/origami/niusha/$JOB_NAME/out/$JOB_NAME_$TASK_ID.out"
#$ -e "/data/origami/niusha/$JOB_NAME/err/$JOB_NAME_$TASK_ID.err"

while getops ":s:i" opt; do
    case $opt in
        s) script="$OPTARG"
        ;;
        i) INPUTFILENAME="$OPTARG"
        ;;
        \?) echo "Invalid option -$OPTRAG" >&2 # change it according to container stuff

home_dir="/data/origami/niusha"
PARENT_DIR="${home_dir}/$JOB_NAME"

if [ ! -d "$PARENT_DIR" ]
then 
    echo "Parent directory does not exist"
fi

# line_number=$(echo "$SGE_TASK_ID + 1" | bc)

INPUTFILE="$PARENT_DIR/filenames.txt"
line=$(cut -f $SGE_TASK_ID -d $'\n' $INPUTFILE)

DESTINATION_DIR="${PARENT_DIR}/test-$SGE_TASK_ID" #change this to the name of the folder you want to save the outputs in

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
python /mnt/code/${script}

# normal_simulation_different_effectsize_samplesize.py 

