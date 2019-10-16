#! /bin/bash

HOME=$PWD

Samples=5
it=1
mkdir profile_test/SWEEP
while [ $it -le $Samples ]
do
    mkdir profile_test/SWEEP/d$it 
    echo "echo \"The $it Job stars !\"" >> profile_test/SWEEP/d${it}/run_profile.sh
    echo "sleep 15" >> profile_test/SWEEP/d${it}/run_profile.sh
    echo "hostname >> result_${it}.txt" >> profile_test/SWEEP/d${it}/run_profile.sh
    echo "echo \"Job done !\"" >> profile_test/SWEEP/d${it}/run_profile.sh
    chmod +x profile_test/SWEEP/d${it}/run_profile.sh
    ((it++))
done
