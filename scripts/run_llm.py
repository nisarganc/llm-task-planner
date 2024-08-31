import json
import os
import argparse
from datetime import datetime
import sys
import time

import openai

sys.path.append(".") # to the root directory
import resources.actions as actions
import resources.robots as robots
import ai2_thor.utils as utils
from llm.model import GPT


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()

    # samples from simulator
    parser.add_argument("--floor-plan", type=int, required=True)

    # gpt version
    parser.add_argument("--gpt-version", type=str, default="gpt-4", 
                        choices=['gpt-3.5-turbo', 'gpt-4', 'gpt-3.5-turbo-16k'])
    
    # few shot prompt sets
    examples_path = os.getcwd() + "/data/few_shot_examples/"
    parser.add_argument("--task-decomposition-set", type=str, default=examples_path+"task_decompose_new.txt", 
                        choices=[examples_path+'task_decompose.py', examples_path+'task_decompose_new.txt'])
    
    parser.add_argument("--task-allocation-set", type=str, default=examples_path+"task_allocation_new.py", 
                        choices=[examples_path+'task_allocation.py', examples_path+'task_allocation_new.txt', examples_path+'task_allocation_new.py'])
    
    parser.add_argument("--robot-allocation-set", type=str, default=examples_path+"robot_allocation.py",     
                        choices=[examples_path+'robot_allocation.py'])
    
    # test set
    parser.add_argument("--test-set", type=str, default=os.getcwd() + "/data/test_set/", 
                        choices=[os.getcwd() + "/data/test_set/"])
    
    # log results
    parser.add_argument("--log-results", type=str, default=f"./logs/changes_logs/")

    # setup        
    args = parser.parse_args()
    openai.api_key = os.getenv("OPENAI_API_KEY")
        
    # read the tasks list       
    test_tasks = []
    test_robots = []  
    gt_test_tasks = []    
    test_trans = []
    test_max_trans = []  
    with open (f"{args.test_set}/FloorPlan{args.floor_plan}.json", "r") as f:
        for line in f.readlines():
            test_tasks.append(list(json.loads(line).values())[0])
            test_robots.append(list(json.loads(line).values())[1])
            gt_test_tasks.append(list(json.loads(line).values())[2])
            test_trans.append(list(json.loads(line).values())[3])
            test_max_trans.append(list(json.loads(line).values())[4])
    print(f"\n----Test set tasks----\n{test_tasks}")
    print(f"\n----Robots for the tasks----\n{test_robots}")
    print(f"\n----Ground Truth for the tasks----\n{gt_test_tasks}")

    # For each task, collect information about skills of robots mentioned in the task
    test_skilledrobots = []
    for robot_list in test_robots:
        task_robots = []
        for r_id in robot_list:
            rob = robots.robots[r_id]
            task_robots.append(rob)
        test_skilledrobots.append(task_robots)        
 
    ########################## Task Decomposition ##########################
    
    # read input train prompts
    decompose_prompt_file = open(args.task_allocation_set, "r")
    decompose_prompt = decompose_prompt_file.read()
    decompose_prompt_file.close()
    prompt = decompose_prompt
    
    # generate decomposed plan
    decomposed_plan = []
    for i, task in enumerate(test_tasks):
        curr_prompt =  f"{prompt}\n\n# TASK DESCRIPTION: {task}"
        curr_prompt += f"\n\n# Environment objects:"
        curr_prompt += f"\nobjects = {utils.get_ai2_thor_objects(args.floor_plan)}\n\n"
        curr_prompt += f"\n# Available robots:"
        curr_prompt += f"\nrobots = {test_skilledrobots[i]}\n\n"
        
        if "gpt" not in args.gpt_version:
            # older gpt versions
            _, text = GPT(curr_prompt, args.gpt_version, max_tokens=1000, stop=["def"], frequency_penalty=0.15)
        else:           
            messages = [{"role": "system", "content": f"You are a task decomposition and a robot allocation expert. As a task demposition expert, analyse the task given, decompose it into independent sub-tasks, and parallelize SubTasks where ever possible. Each SubTask should be completed by a single robot. Each sub-task is strictly composed of a set of sequential actions taken from the skillset = " + actions.ai2thor_actions + f". Strictly use the objects available in the scene which are listed in the variable, objects. As a robot allocation expert for the given set of SubTasks, assign each SubTask to a minimum number of robots from the set of available robots. A robot or team of robots should be assigned to each SubTask based on their skills and mass capacity. Robot Allocation Rules: 1. Each SubTask should be assigned to a robot that posses all the skills and can handle the mass of the objects involved in the SubTask. 2. If not a team of minimum number of robots should be formed that collectively possess all the skills for that SubTask and can handle the mass of the objects in case of ObjectHandlingSkills = [PickupObject, PutObject, DropHandObject, ThrowObject, PushObject, PullObject] within that SubTask. 3. Check if a SubTask is performed sequentially after other SubTasks (i.e., it depends on the completion of other SubTasks), if yes, then assign it to a robot or a team that can start as soon as the preceding SubTasks are complete based on skills and mass capacity. 4. Further, If multiple SubTasks can be performed in parallel (i.e., if the SubTask does not depend on the completion of other SubTask), assign different robots or teams if available, but again make sure allocation also satisfies skills and mass capacity so that parallel SubTasks can be started at the same time."},
                        {"role": "user", "content": curr_prompt}]
            _, text = GPT(messages,args.gpt_version, max_tokens=1300, frequency_penalty=0.0)

        decomposed_plan.append(text)
        print(f"\n---------Generated task decomposition solution for <{task}>---------\n{text}")
        
        # wait for 1 min
        time.sleep(180)

    ############################ save generated plan ########################################
    
    if not os.path.isdir(args.log_results):
        os.makedirs(args.log_results)
    now = datetime.now() # current date and time
    date_time = now.strftime("%m-%d-%Y-%H-%M-%S")
    
    for idx, task in enumerate(test_tasks):
        line = {}
        # replace space with underscore
        task = task.replace(" ", "_")
        folder_name = f"{task}_{date_time}"
        os.mkdir(args.log_results+folder_name) 

        line["task_name"] = task
        line["floor_no"] = args.floor_plan
        line["robots"] = test_skilledrobots[idx]
        line["ground_truth"] = gt_test_tasks[idx]
        line["max_trans"] = test_max_trans[idx]
    
        with open(f"{args.log_results}{folder_name}/log.json", 'w') as f:
            f.write(json.dumps(line) + "\n")

        with open(f"{args.log_results}{folder_name}/code_plan.py", 'w') as d:
            d.write(decomposed_plan[idx])
            