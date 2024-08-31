# Independent SubTasks:
# SubTask 1: Turn off the light. (Skills Required: GoToObject, SwitchOff)
# We can execute SubTask 1 first.

# Task allocation solution:
# robot0, robot1 and robot2 have same number of skills (no_skills) and share the same set of skills.
# The first and only main SubTask, 'Turn off the light' can be performed by any robot with 'GoToObject' and 'SwitchOff' skills. In this case, robot0, robot1 and robot2 have all these skills. There is no need to address mass capacity as there are no ObjectHandlingSkills in this SubTask.
# The SubTask can be executed by any robot. In this case since robot0 is free, this SubTask is assigned to robot0.

# Task allocation code:
def turn_off_light(robot_list):
    # 0: SubTask 1: Turn off the light
    # 1: Go to the LightSwitch using robot0.
    simulate.GoToObject(robot_list[0], 'LightSwitch')
    # 2: Switch off the LightSwitch using robot0.
    simulate.SwitchOff(robot_list[0], 'LightSwitch')

# Execute SubTask 1
turn_off_light(robots)

# Task, 'Make the kitchen dark' is done.