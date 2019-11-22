# -*- coding: utf-8 -*-
#
# This source file is part of the FabSim software toolkit, which is distributed under the BSD 3-Clause license.
# Please refer to LICENSE for detailed information regarding the licensing.
#
# This file contains FabSim definitions specific to FabDummy.

#from base import ClassTimeIt
import time
import os
from base.fab import *
# Add local script, blackbox and template path.
add_local_paths("FabProfile")

@task
def profile_ensemble(samples=10, job_time=15, recreate=True, config="profile_test",**args):
    """
    Submits an ensemble of job.
    One job is run for each dile in <config_file_directory>/dummy_test/SWEEP.
    samples : The number of job you want to launch
    job_time : The duration of the job
    recreate : If set to True, will recreate all the jobs in the SWEEP dir
    job_size : *TODO* The size of the job directory
    """
    
    path_to_config = find_config_file_path(config)

    # Creation of the SWEEP dir, contening all the information of the jobs
    if recreate is True:
        os.system("rm -rf %s/profile_test/* "%os.path.dirname(path_to_config) ) # this semantic to avoid "rm -rf %s/*" --> might be a pb if %s is ""
        os.system("/bin/bash %s/create_directory.sh %s %s %s"%(os.path.dirname(path_to_config), samples, job_time, path_to_config))
    
    # Start the ensemble run
    T1 = time.time()
    print("local config file path at: %s" %path_to_config)
    sweep_dir = path_to_config + "/SWEEP"
    env.script = 'profile'
    env.input_name_in_config = 'profile.txt'

    run_ensemble(config, sweep_dir, **args)
    
    T2 = time.time()
    Total_time = T2 - T1
    print(" Total time is %s sec" %Total_time)

    
