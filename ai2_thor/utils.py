from ai2thor.controller import Controller
from ai2thor.platform import CloudRendering
from scipy.spatial import distance
from typing import Tuple
import numpy as np

def get_ai2_thor_objects(floor_plan_id):
    # connector to ai2thor to get object list
    controller = Controller(scene="FloorPlan"+str(floor_plan_id), platform=CloudRendering)
    objs = list([obj["objectType"] for obj in controller.last_event.metadata["objects"]])
    obj_mass = list([obj["mass"] for obj in controller.last_event.metadata["objects"]])
    controller.stop()
    objs_dict = []
    for i, obj in enumerate(objs):
        obj_dict = {'name': obj , 'mass' : obj_mass[i]} # obj_dict = {'name': obj , 'mass' : 1.0}    
        objs_dict.append(obj_dict)
    return objs_dict


def closest_node(node, nodes, no_robot, clost_node_location):
    crps = []
    distances = distance.cdist([node], nodes)[0]
    dist_indices = np.argsort(np.array(distances))
    for i in range(no_robot):
        pos_index = dist_indices[(i * 5) + clost_node_location[i]]
        crps.append (nodes[pos_index])
    return crps

def distance_pts(p1: Tuple[float, float, float], p2: Tuple[float, float, float]):
    return ((p1[0] - p2[0]) ** 2 + (p1[2] - p2[2]) ** 2) ** 0.5