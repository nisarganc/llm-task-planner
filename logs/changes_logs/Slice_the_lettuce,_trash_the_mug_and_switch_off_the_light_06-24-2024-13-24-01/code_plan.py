# Independent SubTasks:
# SubTask 1: Slice the Lettuce. (Skills Required: GoToObject, PickupObject, SliceObject, PutObject)
# SubTask 2: Trash the Mug. (Skills Required: GoToObject, PickupObject, ThrowObject)
# SubTask 3: Switch off the Light. (Skills Required: GoToObject, SwitchOff)
# We can execute SubTask 1, SubTask 2 and SubTask 3 in parallel.

# Task allocation solution:
# robot0, robot1 and robot2 have same skills and mass capacity. 
# The first SubTask, 'Slice the Lettuce' can be performed by any robot with 'GoToObject', 'PickupObject', 'SliceObject', and 'PutObject' skills. In this case, robot0 has all these skills. There is a need to address mass capacity as there are skills, 'PickupObject' and 'PutObject' belonging to ObjectHandlingSkills set. These skills are performed on the object, 'Lettuce', whose mass capacity is 0.4699999988079071. The robot0 with that skill has mass capacity greater or equal to the mass of Lettuce. Hence robot0 can be allocated to perform this SubTask.
# The second SubTask, 'Trash the Mug' can be performed by any robot with 'GoToObject', 'PickupObject', and 'ThrowObject' skills. In this case, robot1 has all these skills. There is a need to address mass capacity as there are skills, 'PickupObject' and 'ThrowObject' belonging to ObjectHandlingSkills set. These skills are performed on the object, 'Mug', whose mass capacity is 1.0. The robot1 with that skill has mass capacity greater or equal to the mass of Mug. Hence robot1 can be allocated to perform this SubTask.
# The third SubTask, 'Switch off the Light' can be performed by any robot with 'GoToObject' and 'SwitchOff' skills. In this case, robot2 has all these skills. There is no need to address mass capacity as there are no ObjectHandlingSkills in this SubTask. Hence robot2 can be allocated to perform this SubTask.
# The three SubTasks can be executed in parallel with robot0 allocated to SubTask 1, robot1 allocated to SubTask 2 and robot2 allocated to SubTask 3.

# Task allocation code:
def slice_lettuce(robot_list):
    # 0: SubTask 1: Slice the Lettuce
    # 1: Go to the Knife using robot0.
    simulate.GoToObject(robot_list[0], 'Knife')
    # 2: Pick up the Knife using robot0.
    simulate.PickupObject(robot_list[0], 'Knife')
    # 3: Go to the Lettuce using robot0.
    simulate.GoToObject(robot_list[0], 'Lettuce')
    # 4: Slice the Lettuce using robot0.
    simulate.SliceObject(robot_list[0], 'Lettuce')
    # 5: Go to the countertop using robot0.
    simulate.GoToObject(robot_list[0], 'CounterTop')
    # 6: Put the Knife back on the CounterTop using robot0.
    simulate.PutObject(robot_list[0], 'Knife', 'CounterTop')

def trash_mug(robot_list):
    # 0: SubTask 2: Trash the Mug
    # 1: Go to the Mug using robot1.
    simulate.GoToObject(robot_list[1], 'Mug')
    # 2: Pick up the Mug using robot1.
    simulate.PickupObject(robot_list[1], 'Mug')
    # 3: Go to the GarbageCan using robot1.
    simulate.GoToObject(robot_list[1], 'GarbageCan')
    # 4: Throw the Mug in the GarbageCan using robot1.
    simulate.ThrowObject(robot_list[1], 'Mug', 'GarbageCan')

def switch_off_light(robot_list):
    # 0: SubTask 3: Switch off the Light
    # 1: Go to the LightSwitch using robot2.
    simulate.GoToObject(robot_list[2], 'LightSwitch')
    # 2: Switch off the LightSwitch using robot2.
    simulate.SwitchOff(robot_list[2], 'LightSwitch')

# Perform SubTask 1, SubTask 2 and SubTask 3 in parallel
task1_thread = threading.Thread(target=slice_lettuce, args=(robots,))
task2_thread = threading.Thread(target=trash_mug, args=(robots,))
task3_thread = threading.Thread(target=switch_off_light, args=(robots,))

# Start executing SubTask 1, SubTask 2 and SubTask 3
task1_thread.start()
task2_thread.start()
task3_thread.start()

# Wait for both SubTask 1, SubTask 2 and SubTask 3 to finish
task1_thread.join()
task2_thread.join()
task3_thread.join()

# Task, 'Slice the lettuce, trash the mug and switch off the light' is done.