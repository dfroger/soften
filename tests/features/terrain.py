from lettuce import *

import os
import os.path as p
import shutil
import functools

@before.each_scenario
def setup_workdir(scenario):
    this_script_dir = p.dirname(p.abspath(__file__))
    world.workdir = p.realpath(p.join(this_script_dir, '..', 'workdir'))
    world.join_workdir = functools.partial(p.join, world.workdir)
    world.soften = p.realpath(p.join(this_script_dir, 
                                     '..','..','soften','soften.py') )
    if p.isdir(world.workdir):
        shutil.rmtree(world.workdir)
    os.mkdir(world.workdir)
