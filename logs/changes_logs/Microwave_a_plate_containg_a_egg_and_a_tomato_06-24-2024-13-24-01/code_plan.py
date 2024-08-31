# Independent SubTasks:
# SubTask 1: Pickup the Plate. (Skills Required: GoToObject, PickupObject)
# SubTask 2: Put the Egg on the Plate. (Skills Required: GoToObject, PickupObject, PutObject)
# SubTask 3: Put the Tomato on the Plate. (Skills Required: GoToObject, PickupObject, PutObject)
# SubTask 4: Put the Plate in the Microwave. (Skills Required: GoToObject, PutObject)
# SubTask 5: Turn on the Microwave. (Skills Required: GoToObject, SwitchOn)
# We can execute SubTask 1 first, then SubTask 2, then SubTask 3, then SubTask 4 and finally SubTask 5.

# Task allocation solution:
# robot0, robot1 and robot2 have 13 skills. Robots have same number of skills (no_skills) and share the same set of skills.
# The first SubTask, 'Pickup the Plate' can be performed by any robots: robot0, robot1, or robot2. There is a need to address mass capacity as there is a skill, 'PickupObject' belonging to ObjectHandlingSkills set. This skill is performed on the object, 'Plate', whose mass capacity is 0.6200000047683716. Hence the SubTask can be performed by any robot with mass capacity greater than or equal to 0.6200000047683716. In this case since robot0 is free and has a mass capacity = 100, this SubTask is assigned to robot0.
# The second SubTask, 'Put the Egg on the Plate' can be performed by any robots: robot0, robot1, or robot2. There is a need to address mass capacity as there are skills, 'PickupObject' and 'PutObject' belonging to ObjectHandlingSkills set. These skills are performed on the object, 'Egg', whose mass capacity is 0.054999999701976776. Hence the SubTask can be performed by any robot with mass capacity greater than or equal to 0.054999999701976776. In this case since robot1 is free and has a mass capacity = 100, this SubTask is assigned to robot1.
# The third SubTask, 'Put the Tomato on the Plate' can be performed by any robots: robot0, robot1, or robot2. There is a need to address mass capacity as there are skills, 'PickupObject' and 'PutObject' belonging to ObjectHandlingSkills set. These skills are performed on the object, 'Tomato', whose mass capacity is 0.11999998986721039. Hence the SubTask can be performed by any robot with mass capacity greater than or equal to 0.11999998986721039. In this case since robot2 is free and has a mass capacity = 100, this SubTask is assigned to robot2.
# The fourth SubTask, 'Put the Plate in the Microwave' can be performed by any robots: robot0, robot1, or robot2. There is a need to address mass capacity as there is a skill, 'PutObject' belonging to ObjectHandlingSkills set. This skill is performed on the object, 'Plate', whose mass capacity is 0.6200000047683716. Hence the SubTask can be performed by any robot with mass capacity greater than or equal to 0.6200000047683716. In this case since robot0 is free and has a mass capacity = 100, this SubTask is assigned to robot0.
# The fifth SubTask, 'Turn on the Microwave' can be performed by any robots: robot0, robot1, or robot2. There is no need to address mass capacity as there are no ObjectHandlingSkills in this SubTask. In this case since robot1 is free, this SubTask is assigned to robot1.

# Task allocation code:
def pickup_plate(robot_list):
    # 0: SubTask 1: Pickup the Plate
    # 1: Go to the Plate using robot0.
    simulate.GoToObject(robot_list[0], 'Plate')
    # 2: Pick up the Plate using robot0.
    simulate.PickupObject(robot_list[0], 'Plate')

def put_egg_on_plate(robot_list):
    # 0: SubTask 2: Put the Egg on the Plate
    # 1: Go to the Egg using robot1.
    simulate.GoToObject(robot_list[1], 'Egg')
    # 2: Pick up the Egg using robot1.
    simulate.PickupObject(robot_list[1], 'Egg')
    # 3: Put the Egg on the Plate using robot1.
    simulate.PutObject(robot_list[1], 'Egg', 'Plate')

def put_tomato_on_plate(robot_list):
    # 0: SubTask 3: Put the Tomato on the Plate
    # 1: Go to the Tomato using robot2.
    simulate.GoToObject(robot_list[2], 'Tomato')
    # 2: Pick up the Tomato using robot2.
    simulate.PickupObject(robot_list[2], 'Tomato')
    # 3: Put the Tomato on the Plate using robot2.
    simulate.PutObject(robot_list[2], 'Tomato', 'Plate')

def put_plate_in_microwave(robot_list):
    # 0: SubTask 4: Put the Plate in the Microwave
    # 1: Go to the Microwave using robot0.
    simulate.GoToObject(robot_list[0], 'Microwave')
    # 2: Put the Plate in the Microwave using robot0.
    simulate.PutObject(robot_list[0], 'Plate', 'Microwave')

def turn_on_microwave(robot_list):
    # 0: SubTask 5: Turn on the Microwave
    # 1: Go to the Microwave using robot1.
    simulate.GoToObject(robot_list[1], 'Microwave')
    # 2: Turn on the Microwave using robot1.
    simulate.SwitchOn(robot_list[1], 'Microwave')

# Perform SubTask 1, then SubTask 2, then SubTask 3, then SubTask 4 and finally SubTask