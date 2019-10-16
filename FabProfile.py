# -*- coding: utf-8 -*-
#
# This source file is part of the FabSim software toolkit, which is distributed under the BSD 3-Clause license.
# Please refer to LICENSE for detailed information regarding the licensing.
#
# This file contains FabSim definitions specific to FabDummy.

#from base import ClassTimeIt
import time
from base.fab import *
# Add local script, blackbox and template path.
add_local_paths("FabProfile")

@task
def profile_ensemble(config="profile_test",**args):
    """
    Submits an ensemble of job.
    One job is run for each dile in <config_file_directory>/dummy_test/SWEEP.
    """
    T1 = time.time()
    path_to_config = find_config_file_path(config)
    print("local config file path at: %s" %path_to_config)
    sweep_dir = path_to_config + "/SWEEP"
    env.script = 'profile'
    env.input_name_in_config = 'profile.txt'

    run_ensemble(config, sweep_dir, **args)
    
    T2 = time.time()
    Total_time = T2 - T1
    print(" Total time is %s sec" %Total_time)

    
