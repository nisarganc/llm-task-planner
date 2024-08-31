# Independent SubTasks:
# SubTask 1: Put apple in fridge. (Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject)
# SubTask 2: Switch off the light. (Skills Required: GoToObject, SwitchOff)
# We can execute SubTask 1 and SubTask 2 in parallel.

# Task allocation solution:
# robot0, robot1 and robot2 have same number of skills (no_skills) and share the same set of skills.
# The first SubTask, 'Put apple in fridge' can be performed by any robots: robot0, robot1, or robot2. There is a need to address mass capacity as there are skills, 'PickupObject' and 'PutObject' belonging to ObjectHandlingSkills set. These skills are performed on the object, 'Apple', whose mass capacity is 0.2. Hence the SubTask can be performed by any robot with mass capacity greater than or equal to 0.2. In this case since robot0 is free and has a mass capacity = 100, this SubTask is assigned to robot0.
# The second SubTask, 'Switch off the light' can be performed by any robots: robot0, robot1, or robot2. There is no need to address mass capacity as there are no ObjectHandlingSkills in this SubTask. In this case since robot1 is free, this SubTask is assigned to robot1.
# The two SubTasks can be executed in parallel with robot0 allocated to SubTask 1 and robot1 allocated to SubTask 2.

# Task allocation code:
def put_apple_in_fridge(robot_list):
    # 0: SubTask 1: Put apple in fridge
    # 1: Go to the Apple using robot0.
    simulate.GoToObject(robot_list[0], 'Apple')
    # 2: Pick up the Apple using robot0.
    simulate.PickupObject(robot_list[0], 'Apple')
    # 3: Go to the Fridge using robot0.
    simulate.GoToObject(robot_list[0], 'Fridge')
    # 4: Open the Fridge using robot0.
    simulate.OpenObject(robot_list[0], 'Fridge')
    # 5: Put the Apple in the Fridge using robot0.
    simulate.PutObject(robot_list[0], 'Apple', 'Fridge')
    # 6: Close the Fridge using robot0.
    simulate.CloseObject(robot_list[0], 'Fridge')

def switch_off_light(robot_list):
    # 0: SubTask 2: Switch off the light
    # 1: Go to the LightSwitch using robot1.
    simulate.GoToObject(robot_list[1], 'LightSwitch')
    # 2: Switch off the LightSwitch using robot1.
    simulate.SwitchOff(robot_list[1], 'LightSwitch')

# Perform SubTask 1 and SubTask 2 in parallel
task1_thread = threading.Thread(target=put_apple_in_fridge, args=(robots,))
task2_thread = threading.Thread(target=switch_off_light, args=(robots,))

# Start executing SubTask 1 and SubTask 2
task1_thread.start()
task2_thread.start()

# Wait for both SubTask 1 and SubTask 2 to finish
task1_thread.join()
task2_thread.join()

# Task, 'Put apple in fridge and switch off the light' is done.