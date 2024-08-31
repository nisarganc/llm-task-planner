import os
from pathlib import Path
import subprocess
import argparse
from glob import glob
import json
import sys

import numpy as np

sys.path.append(".") # to the root directory
from ai2_thor.sim import AI2ThorSimulator

import threading

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--scene", type=int, required=True)
    parser.add_argument("--robots", type=int, required=True)
    args = parser.parse_args()

    
    simulate = AI2ThorSimulator(args.scene, args.robots)


