# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Switch off the lights. (Skills Required: GoToObject, SwitchOff)
# We can execute SubTask 1.

# CODE
def make_kitchen_dark():
    # 0: SubTask 1: Make the kitchen dark
    # 1: Go to the LightSwitch.
    GoToObject('LightSwitch')
    # 2: Switch off the LightSwitch.
    SwitchOff('LightSwitch')

# Execute SubTask 1
make_kitchen_dark()

# Task make the kitchen dark is done