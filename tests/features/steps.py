import os
import os.path as p
import subprocess

from lettuce import *

def touch(filepath):
    dirs = os.path.dirname(filepath)
    if not os.path.isdir(dirs):
        os.makedirs(dirs)
    open(filepath,'w').close()

def check_soft_link(filepath, expected_to):
    to = os.readlink(filepath)
    if not to == expected_to: 
        raise OSError, "%s is softlinked to %s, not %s" % (
                filepath, to, expected_to)

@step("I create the following hardlinked files:")
def create_hardlinked_files(step):
    files = [ world.join_workdir(h['file']) for h in step.hashes ]
    source = files[0]
    touch(source)
    for f in files[1:]:
        os.link(source, f)

@step("I run 'soften (.+)'")
def run_soften(step, soften_args):
    cmd = "python %s %s" % (world.soften, soften_args,)
    subprocess.check_call(cmd.split(), cwd=world.workdir)
        
@step("the following files are softlinked to '(.+)'")
def are_softlinked_to(step, expected_to):
    files = [ world.join_workdir(h['file']) for h in step.hashes ]
    for f in files:
        check_soft_link(f, expected_to)
        
@step("the following files are softlinked to the absolute path of '(.+)'")
def are_softlinked_to_absolute_path(step, expected_to):
    files = [ world.join_workdir(h['file']) for h in step.hashes ]
    expected_to = p.realpath(world.join_workdir(expected_to))
    for f in files:
        check_soft_link(f, expected_to)
