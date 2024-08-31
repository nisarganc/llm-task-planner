def make_kitchen_dark(robot_list):
    # robot_list = [robot1]
    # 0: SubTask 1: Make the kitchen dark
    # 1: Go to the LightSwitch using robot1.
    GoToObject(robot_list[0],'LightSwitch')
    # 2: Switch off the LightSwitch using robot1.
    SwitchOff(robot_list[0],'LightSwitch')

# Execute SubTask 1
make_kitchen_dark([robots[0]])

# Task make the kitchen dark is done