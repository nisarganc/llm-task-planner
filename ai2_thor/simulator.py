import time
import math
import numpy as np
import re
import sys
import random
from ai2thor.controller import Controller

import threading
import cv2
import os
import shutil
from glob import glob

sys.path.append(".") # to the root directory
from ai2_thor.utils import closest_node, distance_pts

total_exec = 0
success_exec = 0

# create a class called ai2thor simulator
class AI2ThorSimulator:
    def __init__(self, test_log):
        # super(AI2ThorSimulator, self).__init__(test_log)

        # initialize simulator
        self.c = Controller(height=1000, width=1000)
        self.c.reset("FloorPlan" + str(test_log["floor_no"]))
        self.no_robot = len(test_log["robots"])   

        # initialize n agents into the scene
        self.multi_agent_event = self.c.step(dict(action='Initialize', agentMode="default", snapGrid=False, gridSize=0.5, rotateStepDegrees=20, visibilityDistance=100, fieldOfView=90, agentCount=self.no_robot))

        # add a top view camera
        event = self.c.step(action="GetMapViewCameraProperties")
        event = self.c.step(action="AddThirdPartyCamera", **event.metadata["actionReturn"])

        # get reachable positions
        self.reachable_positions_ = self.c.step(action="GetReachablePositions").metadata["actionReturn"]
        self.reachable_positions = positions_tuple = [(p["x"], p["y"], p["z"]) for p in self.reachable_positions_]

        # randomize postions of the agents
        for i in range (self.no_robot):
            init_pos = random.choice(self.reachable_positions_)
            self.c.step(dict(action="Teleport", position=init_pos, agentId=i))
        
        objs = list([obj["objectId"] for obj in self.c.last_event.metadata["objects"]])
        
        # x = c.step(dict(action="RemoveFromScene", objectId='Lettuce|+01.11|+00.83|-01.43'))
        # c.step({"action":"InitialRandomSpawn", "excludedReceptacles":["Microwave", "Pan", "Chair", "Plate", "Fridge", "Cabinet", "Drawer", "GarbageCan"]})
        # c.step({"action":"InitialRandomSpawn", "excludedReceptacles":["Cabinet", "Drawer", "GarbageCan"]})

        self.action_queue = []
        self.task_over = False
        recp_id = None

        for i in range (self.no_robot):
            self.multi_agent_event = self.c.step(action="LookDown", degrees=35, agentId=i)

        actions_thread = threading.Thread(target=self.exec_actions)
        actions_thread.start()        

    def exec_actions(self):
  
        # delete if current output already exist
        cur_path = os.path.dirname(__file__) + "/*/"
        for x in glob(cur_path, recursive = True):
            shutil.rmtree (x)
        
        # create new folders to save the images from the agents
        for i in range(self.no_robot):
            folder_name = "agent_" + str(i+1)
            folder_path = os.path.dirname(__file__) + "/" + folder_name
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
        
        # create folder to store the top view images
        folder_name = "top_view"
        folder_path = os.path.dirname(__file__) + "/" + folder_name
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        img_counter = 0
        
        while not self.task_over:
            if len(self.action_queue) > 0:
                try:
                    act = self.action_queue[0]
                    if act['action'] == 'ObjectNavExpertAction':
                        self.multi_agent_event = self.c.step(dict(action=act['action'], position=act['position'], agentId=act['agent_id']))
                        next_action = self.multi_agent_event.metadata['actionReturn']

                        if next_action != None:
                            self.multi_agent_event = self.c.step(action=next_action, agentId=act['agent_id'], forceAction=True)
                    
                    elif act['action'] == 'MoveAhead':
                        self.multi_agent_event = self.c.step(action="MoveAhead", agentId=act['agent_id'])
                        
                    elif act['action'] == 'MoveBack':
                        self.multi_agent_event = self.c.step(action="MoveBack", agentId=act['agent_id'])
                            
                    elif act['action'] == 'RotateLeft':
                        self.multi_agent_event = self.c.step(action="RotateLeft", degrees=act['degrees'], agentId=act['agent_id'])
                        
                    elif act['action'] == 'RotateRight':
                        self.multi_agent_event = self.c.step(action="RotateRight", degrees=act['degrees'], agentId=act['agent_id'])
                        
                    elif act['action'] == 'PickupObject':
                        total_exec += 1
                        self.multi_agent_event = self.c.step(action="PickupObject", objectId=act['objectId'], agentId=act['agent_id'], forceAction=True)
                        if self.multi_agent_event.metadata['errorMessage'] != "":
                            print (self.multi_agent_event.metadata['errorMessage'])
                        else:
                            success_exec += 1
    
                    elif act['action'] == 'PutObject':
                        total_exec += 1
                        self.multi_agent_event = self.c.step(action="PutObject", objectId=act['objectId'], agentId=act['agent_id'], forceAction=True)
                        if self.multi_agent_event.metadata['errorMessage'] != "":
                            print (self.multi_agent_event.metadata['errorMessage'])
                        else:
                            success_exec += 1
    
                    elif act['action'] == 'ToggleObjectOn':
                        total_exec += 1
                        self.multi_agent_event = self.c.step(action="ToggleObjectOn", objectId=act['objectId'], agentId=act['agent_id'], forceAction=True)
                        if self.multi_agent_event.metadata['errorMessage'] != "":
                            print (self.multi_agent_event.metadata['errorMessage'])
                        else:
                            success_exec += 1
                    
                    elif act['action'] == 'ToggleObjectOff':
                        total_exec += 1
                        self.multi_agent_event = self.c.step(action="ToggleObjectOff", objectId=act['objectId'], agentId=act['agent_id'], forceAction=True)
                        if self.multi_agent_event.metadata['errorMessage'] != "":
                            print (self.multi_agent_event.metadata['errorMessage'])
                        else:
                            success_exec += 1
                        
                    elif act['action'] == 'OpenObject':
                        total_exec += 1
                        self.multi_agent_event = self.c.step(action="OpenObject", objectId=act['objectId'], agentId=act['agent_id'], forceAction=True)
                        if self.multi_agent_event.metadata['errorMessage'] != "":
                            print (self.multi_agent_event.metadata['errorMessage'])
                        else:
                            success_exec += 1
    
                        
                    elif act['action'] == 'CloseObject':
                        total_exec += 1
                        self.multi_agent_event = self.c.step(action="CloseObject", objectId=act['objectId'], agentId=act['agent_id'], forceAction=True)
                        if self.multi_agent_event.metadata['errorMessage'] != "":
                            print (self.multi_agent_event.metadata['errorMessage'])
                        else:
                            success_exec += 1
                            
                    elif act['action'] == 'SliceObject':
                        total_exec += 1
                        self.multi_agent_event = self.c.step(action="SliceObject", objectId=act['objectId'], agentId=act['agent_id'], forceAction=True)
                        if self.multi_agent_event.metadata['errorMessage'] != "":
                            print (self.multi_agent_event.metadata['errorMessage'])
                        else:
                            success_exec += 1
                            
                    elif act['action'] == 'ThrowObject':
                        total_exec += 1
                        self.multi_agent_event = self.c.step(action="ThrowObject", moveMagnitude=7, agentId=act['agent_id'], forceAction=True)
                        if self.multi_agent_event.metadata['errorMessage'] != "":
                            print (self.multi_agent_event.metadata['errorMessage'])
                        else:
                            success_exec += 1
                            
                    elif act['action'] == 'BreakObject':
                        total_exec += 1
                        self.multi_agent_event = self.c.step(action="BreakObject", objectId=act['objectId'], agentId=act['agent_id'], forceAction=True)
                        if self.multi_agent_event.metadata['errorMessage'] != "":
                            print (self.multi_agent_event.metadata['errorMessage'])
                        else:
                            success_exec += 1
    
                    
                    elif act['action'] == 'Done':
                        self.multi_agent_event = self.c.step(action="Done")
                        
                        
                except Exception as e:
                    print (e)
                    
                for i,e in enumerate(self.multi_agent_event.events):
                    cv2.imshow('agent%s' % i, e.cv2img)
                    f_name = os.path.dirname(__file__) + "/agent_" + str(i+1) + "/img_" + str(img_counter).zfill(5) + ".png"
                    cv2.imwrite(f_name, e.cv2img)
                top_view_rgb = cv2.cvtColor(c.last_event.events[0].third_party_camera_frames[-1], cv2.COLOR_BGR2RGB)
                cv2.imshow('Top View', top_view_rgb)
                f_name = os.path.dirname(__file__) + "/top_view/img_" + str(img_counter).zfill(5) + ".png"
                cv2.imwrite(f_name, top_view_rgb)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
                
                img_counter += 1    
                self.action_queue.pop(0)



    def GoToObject(self, robots, dest_obj):
        global recp_id
        
        # check if robots is a list
        
        if not isinstance(robots, list):
            # convert robot to a list
            robots = [robots]
        no_agents = len (robots)
        # robots distance to the goal 
        dist_goals = [10.0] * len(robots)
        prev_dist_goals = [10.0] * len(robots)
        count_since_update = [0] * len(robots)
        clost_node_location = [0] * len(robots)
        
        # list of objects in the scene and their centers
        objs = list([obj["objectId"] for obj in self.c.last_event.metadata["objects"]])
        objs_center = list([obj["axisAlignedBoundingBox"]["center"] for obj in self.c.last_event.metadata["objects"]])
        if "|" in dest_obj:
            # obj alredy given
            dest_obj_id = dest_obj
            pos_arr = dest_obj_id.split("|")
            dest_obj_center = {'x': float(pos_arr[1]), 'y': float(pos_arr[2]), 'z': float(pos_arr[3])}
        else:
            for idx, obj in enumerate(objs):
                
                match = re.match(dest_obj, obj)
                if match is not None:
                    dest_obj_id = obj
                    dest_obj_center = objs_center[idx]
                    if dest_obj_center != {'x': 0.0, 'y': 0.0, 'z': 0.0}:
                        break # find the first instance
            
        print ("Going to ", dest_obj_id, dest_obj_center)
            
        dest_obj_pos = [dest_obj_center['x'], dest_obj_center['y'], dest_obj_center['z']] 
        
        # closest reachable position for each robot
        # all robots cannot reach the same spot 
        # differt close points needs to be found for each robot
        crp = closest_node(dest_obj_pos, self.reachable_positions, no_agents, clost_node_location)
        
        goal_thresh = 0.25
        # at least one robot is far away from the goal
        
        while all(d > goal_thresh for d in dist_goals):
            for ia, robot in enumerate(robots):
                robot_name = robot['name']
                agent_id = int(robot_name[-1]) - 1
                
                # get the pose of robot        
                metadata = self.c.last_event.events[agent_id].metadata
                location = {
                    "x": metadata["agent"]["position"]["x"],
                    "y": metadata["agent"]["position"]["y"],
                    "z": metadata["agent"]["position"]["z"],
                    "rotation": metadata["agent"]["rotation"]["y"],
                    "horizon": metadata["agent"]["cameraHorizon"]}
                
                prev_dist_goals[ia] = dist_goals[ia] # store the previous distance to goal
                dist_goals[ia] = distance_pts([location['x'], location['y'], location['z']], crp[ia])
                
                dist_del = abs(dist_goals[ia] - prev_dist_goals[ia])
                # print (ia, "Dist to Goal: ", dist_goals[ia], dist_del, clost_node_location[ia])
                if dist_del < 0.2:
                    # robot did not move 
                    count_since_update[ia] += 1
                else:
                    # robot moving 
                    count_since_update[ia] = 0
                    
                if count_since_update[ia] < 8:
                    self.action_queue.append({'action':'ObjectNavExpertAction', 'position':dict(x=crp[ia][0], y=crp[ia][1], z=crp[ia][2]), 'agent_id':agent_id})
                else:    
                    #updating goal
                    clost_node_location[ia] += 1
                    count_since_update[ia] = 0
                    crp = closest_node(dest_obj_pos, self.reachable_positions, no_agents, clost_node_location)
        
                time.sleep(0.5)

        # align the robot once goal is reached
        # compute angle between robot heading and object
        metadata = self.c.last_event.events[agent_id].metadata
        robot_location = {
            "x": metadata["agent"]["position"]["x"],
            "y": metadata["agent"]["position"]["y"],
            "z": metadata["agent"]["position"]["z"],
            "rotation": metadata["agent"]["rotation"]["y"],
            "horizon": metadata["agent"]["cameraHorizon"]}
        
        robot_object_vec = [dest_obj_pos[0]-robot_location['x'], dest_obj_pos[2]-robot_location['z']]
        y_axis = [0, 1]
        unit_y = y_axis / np.linalg.norm(y_axis)
        unit_vector = robot_object_vec / np.linalg.norm(robot_object_vec)
        
        angle = math.atan2(np.linalg.det([unit_vector,unit_y]),np.dot(unit_vector,unit_y))
        angle = 360*angle/(2*np.pi)
        angle = (angle + 360) % 360
        rot_angle = angle - robot_location['rotation']
        
        if rot_angle > 0:
            self.action_queue.append({'action':'RotateRight', 'degrees':abs(rot_angle), 'agent_id':agent_id})
        else:
            self.action_queue.append({'action':'RotateLeft', 'degrees':abs(rot_angle), 'agent_id':agent_id})
            
        print ("Reached: ", dest_obj)
        if dest_obj == "Cabinet" or dest_obj == "Fridge" or dest_obj == "CounterTop":
            recp_id = dest_obj_id
        
    def PickupObject(self, robots, pick_obj):
        if not isinstance(robots, list):
            # convert robot to a list
            robots = [robots]
        no_agents = len (robots)
        # robots distance to the goal 
        for idx in range(no_agents):
            robot = robots[idx]
            print ("PIcking: ", pick_obj)
            robot_name = robot['name']
            agent_id = int(robot_name[-1]) - 1
            # list of objects in the scene and their centers
            objs = list([obj["objectId"] for obj in self.c.last_event.metadata["objects"]])
            objs_center = list([obj["axisAlignedBoundingBox"]["center"] for obj in self.c.last_event.metadata["objects"]])
            
            for idx, obj in enumerate(objs):
                match = re.match(pick_obj, obj)
                if match is not None:
                    pick_obj_id = obj
                    dest_obj_center = objs_center[idx]
                    if dest_obj_center != {'x': 0.0, 'y': 0.0, 'z': 0.0}:
                        break # find the first instance
            # GoToObject(robot, pick_obj_id)
            # time.sleep(1)
            print ("Picking Up ", pick_obj_id, dest_obj_center)
            self.action_queue.append({'action':'PickupObject', 'objectId':pick_obj_id, 'agent_id':agent_id})
            time.sleep(1)
        
    def PutObject(self, robot, put_obj, recp):
        robot_name = robot['name']
        agent_id = int(robot_name[-1]) - 1
        objs = list(set([obj["objectId"] for obj in self.c.last_event.metadata["objects"]]))
        objs_center = list([obj["axisAlignedBoundingBox"]["center"] for obj in self.c.last_event.metadata["objects"]])
        objs_dists = list([obj["distance"] for obj in self.c.last_event.metadata["objects"]])

        metadata = self.c.last_event.events[agent_id].metadata
        robot_location = [metadata["agent"]["position"]["x"], metadata["agent"]["position"]["y"], metadata["agent"]["position"]["z"]]
        dist_to_recp = 9999999 # distance b/w robot and the recp obj
        for idx, obj in enumerate(objs):
            match = re.match(recp, obj)
            if match is not None:
                dist = objs_dists[idx]
                if dist < dist_to_recp:
                    recp_obj_id = obj
                    dest_obj_center = objs_center[idx]
                    dist_to_recp = dist
                    
        
        global recp_id         
        # if recp_id is not None:
        #     recp_obj_id = recp_id
        # GoToObject(robot, recp_obj_id)
        # time.sleep(1)
        self.action_queue.append({'action':'PutObject', 'objectId':recp_obj_id, 'agent_id':agent_id})
        time.sleep(1)
            
    def SwitchOn(self, robot, sw_obj):
        print ("Switching On: ", sw_obj)
        robot_name = robot['name']
        agent_id = int(robot_name[-1]) - 1
        objs = list(set([obj["objectId"] for obj in self.c.last_event.metadata["objects"]]))
        
        # turn on all stove burner
        if sw_obj == "StoveKnob":
            for obj in objs:
                match = re.match(sw_obj, obj)
                if match is not None:
                    sw_obj_id = obj
                    self.GoToObject(robot, sw_obj_id)
                    # time.sleep(1)
                    self.action_queue.append({'action':'ToggleObjectOn', 'objectId':sw_obj_id, 'agent_id':agent_id})
                    time.sleep(0.1)
        
        # all objects apart from Stove Burner
        else:
            for obj in objs:
                match = re.match(sw_obj, obj)
                if match is not None:
                    sw_obj_id = obj
                    break # find the first instance
            self.GoToObject(robot, sw_obj_id)
            time.sleep(1)
            self.action_queue.append({'action':'ToggleObjectOn', 'objectId':sw_obj_id, 'agent_id':agent_id})
            time.sleep(1)            
            
    def SwitchOff(self, robot, sw_obj):
        print ("Switching Off: ", sw_obj)
        robot_name = robot['name']
        agent_id = int(robot_name[-1]) - 1
        objs = list(set([obj["objectId"] for obj in self.c.last_event.metadata["objects"]]))
        
        # turn on all stove burner
        if sw_obj == "StoveKnob":
            for obj in objs:
                match = re.match(sw_obj, obj) 
                if match is not None:
                    sw_obj_id = obj
                    self.action_queue.append({'action':'ToggleObjectOff', 'objectId':sw_obj_id, 'agent_id':agent_id})
                    time.sleep(0.1)
        
        # all objects apart from Stove Burner
        else:
            for obj in objs:
                match = re.match(sw_obj, obj)
                if match is not None:
                    sw_obj_id = obj
                    break # find the first instance
            self.GoToObject(robot, sw_obj_id)
            time.sleep(1)
            self.action_queue.append({'action':'ToggleObjectOff', 'objectId':sw_obj_id, 'agent_id':agent_id})
            time.sleep(1)      
        
    def OpenObject(self, robot, sw_obj):
        robot_name = robot['name']
        agent_id = int(robot_name[-1]) - 1
        objs = list(set([obj["objectId"] for obj in self.c.last_event.metadata["objects"]]))
        
        for obj in objs:
            match = re.match(sw_obj, obj)
            if match is not None:
                sw_obj_id = obj
                break # find the first instance
            
        global recp_id
        if recp_id is not None:
            sw_obj_id = recp_id
        
        self.GoToObject(robot, sw_obj_id)
        time.sleep(1)
        self.action_queue.append({'action':'OpenObject', 'objectId':sw_obj_id, 'agent_id':agent_id})
        time.sleep(1)
        
    def CloseObject(self, robot, sw_obj):
        robot_name = robot['name']
        agent_id = int(robot_name[-1]) - 1
        objs = list(set([obj["objectId"] for obj in self.c.last_event.metadata["objects"]]))
        
        for obj in objs:
            match = re.match(sw_obj, obj)
            if match is not None:
                sw_obj_id = obj
                break # find the first instance
            
        global recp_id
        if recp_id is not None:
            sw_obj_id = recp_id
            
        self.GoToObject(robot, sw_obj_id)
        time.sleep(1)
        
        self.action_queue.append({'action':'CloseObject', 'objectId':sw_obj_id, 'agent_id':agent_id}) 
        
        if recp_id is not None:
            recp_id = None
        time.sleep(1)
        
    def BreakObject(self, robot, sw_obj):
        robot_name = robot['name']
        agent_id = int(robot_name[-1]) - 1
        objs = list(set([obj["objectId"] for obj in self.c.last_event.metadata["objects"]]))
        
        for obj in objs:
            match = re.match(sw_obj, obj)
            if match is not None:
                sw_obj_id = obj
                break # find the first instance
        self.GoToObject(robot, sw_obj_id)
        time.sleep(1)
        self.action_queue.append({'action':'BreakObject', 'objectId':sw_obj_id, 'agent_id':agent_id}) 
        time.sleep(1)
        
    def SliceObject(self, robot, sw_obj):
        print ("Slicing: ", sw_obj)
        robot_name = robot['name']
        agent_id = int(robot_name[-1]) - 1
        objs = list(set([obj["objectId"] for obj in self.c.last_event.metadata["objects"]]))
        
        for obj in objs:
            match = re.match(sw_obj, obj)
            if match is not None:
                sw_obj_id = obj
                break # find the first instance
        self.GoToObject(robot, sw_obj_id)
        time.sleep(1)
        self.action_queue.append({'action':'SliceObject', 'objectId':sw_obj_id, 'agent_id':agent_id})      
        time.sleep(1)
        
    def CleanObject(self, robot, sw_obj):
        robot_name = robot['name']
        agent_id = int(robot_name[-1]) - 1
        objs = list(set([obj["objectId"] for obj in self.c.last_event.metadata["objects"]]))

        for obj in objs:
            match = re.match(sw_obj, obj)
            if match is not None:
                sw_obj_id = obj
                break # find the first instance
        self.GoToObject(robot, sw_obj_id)
        time.sleep(1)
        self.action_queue.append({'action':'CleanObject', 'objectId':sw_obj_id, 'agent_id':agent_id}) 
        time.sleep(1)
        
    def ThrowObject(self, robot, sw_obj):
        robot_name = robot['name']
        agent_id = int(robot_name[-1]) - 1
        objs = list(set([obj["objectId"] for obj in self.c.last_event.metadata["objects"]]))

        for obj in objs:
            match = re.match(sw_obj, obj)
            if match is not None:
                sw_obj_id = obj
                break # find the first instance
        
        self.action_queue.append({'action':'ThrowObject', 'objectId':sw_obj_id, 'agent_id':agent_id}) 
        time.sleep(1)