def slice_lettuce(robot_list):
    # robot_list = [robot1]
    # 0: SubTask 1: Slice the Lettuce
    # 1: Go to the Knife using robot1.
    GoToObject(robot_list[0],'Knife')
    # 2: Pick up the Knife using robot1.
    PickupObject(robot_list[0],'Knife')
    # 3: Go to the Lettuce using robot1.
    GoToObject(robot_list[0],'Lettuce')
    # 4: Slice the Lettuce using robot1.
    SliceObject(robot_list[0],'Lettuce')
    # 5: Go to the countertop using robot1.
    GoToObject(robot_list[0],'CounterTop')
    # 6: Put the Knife back on the CounterTop using robot1.
    PutObject(robot_list[0],'Knife', 'CounterTop')

def trash_mug(robot_list):
    # robot_list = [robot2]
    # 0: SubTask 2: Trash the Mug
    # 1: Go to the Mug using robot2.
    GoToObject(robot_list[0],'Mug')
    # 2: Pick up the Mug using robot2.
    PickupObject(robot_list[0],'Mug')
    # 3: Go to the GarbageCan using robot2.
    GoToObject(robot_list[0],'GarbageCan')
    # 4: Put the Mug in the GarbageCan using robot2.
    PutObject(robot_list[0],'Mug', 'GarbageCan')

def switch_off_light(robot_list):
     # robot_list = [robot3]
     # 0: SubTask 3: Switch off the Light
     # 1: Go to the LightSwitch using robot3.
     GoToObject(robot_list[0],'LightSwitch')
     # 2: Switch off the LightSwitch using robot3.
     SwitchOff(robot_list[0],'LightSwitch')

# Parallelize SubTask 1, SubTask 2 and SubTask 3
task1_thread = threading.Thread(target=slice_lettuce, args=([robots[0]],))
task2_thread = threading.Thread(target=trash_mug, args=([robots[1]],))
task3_thread = threading.Thread(target=switch_off_light, args=([robots[2]],))

# Start executing SubTask 1, SubTask 2 and SubTask 3 in parallel
task1_thread.start()
task2_thread.start()
task3_thread.start()

# Wait for both SubTask 1, SubTask 2 and SubTask 3 to finish
task1_thread.join()
task2_thread.join()
task3_thread.join()

# Task Slice the lettuce, trash the mug and switch off the light is done