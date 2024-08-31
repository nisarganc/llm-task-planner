def put_mug_in_coffee_machine(robot_list):
    # robot_list = [robot1]
    # 0: SubTask 1: Put mug in the coffee machine
    # 1: Go to the Mug using robot1.
    GoToObject(robot_list[0],'Mug')
    # 2: Pick up the Mug using robot1.
    PickupObject(robot_list[0],'Mug')
    # 3: Go to the CoffeeMachine using robot1.
    GoToObject(robot_list[0],'CoffeeMachine')
    # 4: Put Mug in the CoffeeMachine using robot1
    PutObject(robot_list[0],'Mug', 'CoffeeMachine')

def switch_on_coffee_machine(robot_list):
    # robot_list = [robot3]
    # 0: SubTask 2: Switch on the coffee machine
    # 1: Go to the CoffeeMachine using robot3.
    GoToObject(robot_list[0],'CoffeeMachine')
    # 2: Switch on the CoffeeMachine using robot3.
    SwitchOn(robot_list[0],'CoffeeMachine')

# Execute SubTask 1 with Robot 1
put_mug_in_coffee_machine([robots[0]])

# Execute SubTask 2 with Robot 3
switch_on_coffee_machine([robots[2]])

# Task put mug in the coffee machine and switch on the coffee machine is done