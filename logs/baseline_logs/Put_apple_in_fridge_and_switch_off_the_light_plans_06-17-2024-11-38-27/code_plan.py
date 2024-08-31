def put_apple_in_fridge(robot_list):
    # robot_list = [robot1]
    # 0: SubTask 1: Put apple in the fridge
    # 1: Go to the Apple using robot1.
    GoToObject(robot_list[0],'Apple')
    # 2: Pick up the Apple using robot1.
    PickupObject(robot_list[0],'Apple')
    # 3: Go to the Fridge using robot1.
    GoToObject(robot_list[0],'Fridge')
    # 4: Open the Fridge using robot1.
    OpenObject(robot_list[0],'Fridge')
    # 5: Put Apple in the Fridge using robot1
    PutObject(robot_list[0],'Apple', 'Fridge')
    # 6: Close Fridge using robot1
    CloseObject(robot_list[0],'Fridge')

def switch_off_light(robot_list):
    # robot_list = [robot2]
    # 0: SubTask 2: Switch off the light
    # 1: Go to the LightSwitch using robot2.
    GoToObject(robot_list[0],'LightSwitch')
    # 2: Switch off the LightSwitch using robot2.
    SwitchOff(robot_list[0],'LightSwitch')

# Parallelize SubTask 1 and SubTask 2
task1_thread = threading.Thread(target=put_apple_in_fridge, args=([robots[0]],))
task2_thread = threading.Thread(target=switch_off_light, args=([robots[1]],))

# Start executing SubTask 1 and SubTask 2 in parallel
task1_thread.start()
task2_thread.start()

# Wait for both SubTask 1 and SubTask 2 to finish
task1_thread.join()
task2_thread.join()

# Task put apple in fridge and switch off the light is done