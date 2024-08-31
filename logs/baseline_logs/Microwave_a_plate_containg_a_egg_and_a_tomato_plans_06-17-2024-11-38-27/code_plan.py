def prepare_plate(robot_list):
    # robot_list = [robot3]
    # 0: SubTask 1: Prepare the Plate with Egg and Tomato
    # 1: Go to the Egg using robot3.
    GoToObject(robot_list[0],'Egg')
    # 2: Pick up the Egg using robot3.
    PickupObject(robot_list[0],'Egg')
    # 3: Go to the Plate using robot3.
    GoToObject(robot_list[0],'Plate')
    # 4: Put the Egg on the Plate using robot3.
    PutObject(robot_list[0],'Egg', 'Plate')
    # 5: Go to the Tomato using robot3.
    GoToObject(robot_list[0],'Tomato')
    # 6: Pick up the Tomato using robot3.
    PickupObject(robot_list[0],'Tomato')
    # 7: Go to the Plate using robot3.
    GoToObject(robot_list[0],'Plate')
    # 8: Put the Tomato on the Plate using robot3.
    PutObject(robot_list[0],'Tomato', 'Plate')

def microwave_plate(robot_list):
     # robot_list = [robot1,robot2,robot3]
     # 0: SubTask 2: Microwave the Plate
     # 1: Go to the Plate using robot1.
     GoToObject(robot_list[0],'Plate')
     # 2: Pick up the Plate using robot1.
     PickupObject(robot_list[0],'Plate')
     # 3: Go to the Microwave using robot1.
     GoToObject(robot_list[0],'Microwave')
     # 4: Open the Microwave using robot1.
     OpenObject(robot_list[0],'Microwave')
     # 5: Put the Plate in the Microwave using robot1.
     PutObject(robot_list[0],'Plate', 'Microwave')
     # 6: Close the Microwave using robot1.
     CloseObject(robot_list[0],'Microwave')
     # 7: Switch on the Microwave using robot2.
     SwitchOn(robot_list[1],'Microwave')
     # 8: Wait for a while to let the food cook.
     time.sleep(5)
     # 9: Switch off the Microwave using robot2.
     SwitchOff(robot_list[1],'Microwave')
     # 10: Open the Microwave using robot1.
     OpenObject(robot_list[0],'Microwave')
     # 11: Pick up the Plate using robot1.
     PickupObject(robot_list[0],'Plate')
     # 12: Close the Microwave using robot1.
     CloseObject(robot_list[0],'Microwave')
     # 13: Go to the CounterTop using robot1.
     GoToObject(robot_list[0],'CounterTop')
     # 14: Put the Plate on the CounterTop using robot1.
     PutObject(robot_list[0],'Plate', 'CounterTop')

# Execute SubTask 1
prepare_plate([robots[2]])

# Execute SubTask 2
microwave_plate([robots[0],robots[1],robots[2]])

# Task Microwave a plate containing an egg and a tomato is done