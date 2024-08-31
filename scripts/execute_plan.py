import os
from pathlib import Path
import subprocess
import argparse
from glob import glob
import json
import sys

import numpy as np

sys.path.append(".") # to the root directory
from ai2_thor.simulator import AI2ThorSimulator

import threading


def generate_video():
    frame_rate = 5
    # input_path, prefix, char_id=0, image_synthesis=['normal'], frame_rate=5
    cur_path = os.path.dirname(__file__) + "/*/"
    for imgs_folder in glob(cur_path, recursive = False):
        view = imgs_folder.split('/')[-2]
        if not os.path.isdir(imgs_folder):
            print("The input path: {} you specified does not exist.".format(imgs_folder))
        else:
            command_set = ['ffmpeg', '-i',
                                '{}/img_%05d.png'.format(imgs_folder), 
                                '-framerate', str(frame_rate),
                                '-pix_fmt', 'yuv420p',
                                '{}/video_{}.mp4'.format(os.path.dirname(__file__), view)]
            subprocess.call(command_set)

def append_trans_ctr(allocated_plan):
    brk_ctr = 0
    code_segs = allocated_plan.split("\n\n")
    fn_calls = []
    for cd in code_segs:
        if "def" not in cd and "threading.Thread" not in cd and "join" not in cd and cd[-1] == ")":
            # fn_calls.append(cd)
            brk_ctr += 1
    print ("No Breaks: ", brk_ctr)
    return brk_ctr
            

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--command", type=str, required=True)
    args = parser.parse_args()

    expt_name = args.command
    
    # import the log file
    log_path = os.getcwd() + "/logs/changes_logs/" + expt_name
    test_log = json.load(log_path + "/log.json")

    simulate = AI2ThorSimulator(test_log)

    code_plan = Path(log_path + "/code_plan.py").read_text()

    # append lines of code file code_plan.py here
    exec(code_plan) 


