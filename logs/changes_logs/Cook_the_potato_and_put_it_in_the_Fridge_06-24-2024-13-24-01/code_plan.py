# Independent SubTasks:
# SubTask 1: Cook the Potato. (Skills Required: GoToObject, PickupObject, SwitchOn, PutObject)
# SubTask 2: Put the cooked Potato in the Fridge. (Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject)
# We can execute SubTask 1 first and then SubTask 2.

# Task allocation solution:
# robot0, robot1 and robot2 have same skills and mass capacity. 
# The first SubTask, 'Cook the Potato' can be performed by any robot with 'GoToObject', 'PickupObject', 'SwitchOn', and 'PutObject' skills. In this case, all robots have these skills. There is a need to address mass capacity as there are skills, 'PickupObject' and 'PutObject' belonging to ObjectHandlingSkills set. These skills are performed on the object, 'Potato', whose mass capacity is 0.18000000715255737. Hence the SubTask can be performed by any robot with mass capacity greater than or equal to 0.18000000715255737. In this case, we can assign this SubTask to robot0.
# The second SubTask, 'Put the cooked Potato in the Fridge' can be performed by any robot with 'GoToObject', 'PickupObject', 'OpenObject', 'PutObject', and 'CloseObject' skills. In this case, all robots have these skills. There is a need to address mass capacity as there are skills, 'PickupObject' and 'PutObject' belonging to ObjectHandlingSkills set. These skills are performed on the object, 'Potato', whose mass capacity is 0.18000000715255737. Hence the SubTask can be performed by any robot with mass capacity greater than or equal to 0.18000000715255737. In this case, we can assign this SubTask to robot1.
# The two SubTasks can be executed sequentially with robot0 allocated to SubTask 1 and robot1 allocated to SubTask 2.

# Task allocation code:
def cook_potato(robot_list):
    # 0: SubTask 1: Cook the Potato
    # 1: Go to the Potato using robot0.
    simulate.GoToObject(robot_list[0], 'Potato')
    # 2: Pick up the Potato using robot0.
    simulate.PickupObject(robot_list[0], 'Potato')
    # 3: Go to the StoveBurner using robot0.
    simulate.GoToObject(robot_list[0], 'StoveBurner')
    # 4: Switch on the StoveBurner using robot0.
    simulate.SwitchOn(robot_list[0], 'StoveBurner')
    # 5: Put the Potato on the StoveBurner using robot0.
    simulate.PutObject(robot_list[0], 'Potato', 'StoveBurner')

def put_cooked_potato_in_fridge(robot_list):
    # 0: SubTask 2: Put the cooked Potato in the Fridge
    # 1: Go to the Potato using robot1.
    simulate.GoToObject(robot_list[1], 'Potato')
    # 2: Pick up the Potato using robot1.
    simulate.PickupObject(robot_list[1], 'Potato')
    # 3: Go to the Fridge using robot1.
    simulate.GoToObject(robot_list[1], 'Fridge')
    # 4: Open the Fridge using robot1.
    simulate.OpenObject(robot_list[1], 'Fridge')
    # 5: Put the Potato in the Fridge using robot1.
    simulate.PutObject(robot_list[1], 'Potato', 'Fridge')
    # 6: Close the Fridge using robot1.
    simulate.CloseObject(robot_list[1], 'Fridge')

# Perform SubTask 1 and then SubTask 2
cook_potato(robots)
put_cooked_potato_in_fridge(robots)

# Task, 'Cook the potato and put it in the Fridge' is done.