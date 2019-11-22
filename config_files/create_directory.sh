#! /bin/bash

HOME=$PWD

Samples=$1
job_duration=$2
PROFILE_TEST_DIR=$3

it=1
mkdir $PROFILE_TEST_DIR/SWEEP
while [ $it -le $Samples ]
do
    mkdir $PROFILE_TEST_DIR/SWEEP/d$it 
    echo "echo \"The $it Job stars !\"" >> $PROFILE_TEST_DIR/SWEEP/d${it}/run_profile.sh
    echo "sleep ${job_duration}" >> $PROFILE_TEST_DIR/SWEEP/d${it}/run_profile.sh
    echo "hostname >> result_${it}.txt" >> $PROFILE_TEST_DIR/SWEEP/d${it}/run_profile.sh
    echo "echo \"Job done !\"" >> $PROFILE_TEST_DIR/SWEEP/d${it}/run_profile.sh
    chmod +x $PROFILE_TEST_DIR/SWEEP/d${it}/run_profile.sh
    ((it++))
done
