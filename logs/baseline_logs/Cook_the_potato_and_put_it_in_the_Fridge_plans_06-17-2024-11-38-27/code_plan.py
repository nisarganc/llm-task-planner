def cook_potato(robot_list):
    # robot_list = [robot1]
    # 0: SubTask 1: Cook the Potato
    # 1: Go to the Potato using robot1.
    GoToObject(robot_list[0],'Potato')
    # 2: Pick up the Potato using robot1.
    PickupObject(robot_list[0],'Potato')
    # 3: Go to the Pan using robot1.
    GoToObject(robot_list[0],'Pan')
    # 4: Put the Potato in the Pan using robot1.
    PutObject(robot_list[0],'Potato', 'Pan')
    # 5: Pick up the pan with potato in it using robot1.
    PickupObject(robot_list[0],'Pan')
    # 6: Go to the StoveBurner using robot1.
    GoToObject(robot_list[0],'StoveBurner')
    # 7: Put the Pan on the stove burner using robot1.
    PutObject(robot_list[0],'Pan', 'StoveBurner')
    # 7: Switch on the StoveKnob using robot1.
    SwitchOn(robot_list[0],'StoveKnob')
    # 7: Wait for a while to let the Potato cook using robot1.
    time.sleep(5)
    # 8: Switch off the StoveKnob using robot1.
    SwitchOff(robot_list[0],'StoveKnob')
    
def put_cooked_potato_in_fridge(robot_list):
     # robot_list = [robot2]
     # 0: SubTask 2: Put cooked potato in fridge
     # 9: Go to the Potato using robot2.
     GoToObject(robot_list[0],'Potato')
     #10. Pick up cooked potato from pan using robot2
     PickupObject(robot_list[0],'Potato')
     # 1: Go to the Fridge using robot2.
     GoToObject(robot_list[0],'Fridge')
     # 2: Open the Fridge using robot2.
     OpenObject(robot_list[0],'Fridge')
     # 3: Put the cooked Potato in the Fridge using robot2
     PutObject(robot_list[0],'Potato', 'Fridge')
     # 4: Close Fridge using robot2
     CloseObject(robot_list[0],'Fridge')

# Execute SubTask 1 with robot1
cook_potato([robots[0]])

# Execute SubTask 2 with robot2
put_cooked_potato_in_fridge([robots[1]])

# Task Cook the potato and put it in the Fridge is done