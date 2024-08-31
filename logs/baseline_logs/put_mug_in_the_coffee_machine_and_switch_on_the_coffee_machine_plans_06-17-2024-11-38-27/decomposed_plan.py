# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Put mug in the coffee machine. (Skills Required: GoToObject, PickupObject, PutObject)
# SubTask 2: Switch on the coffee machine. (Skills Required: GoToObject, SwitchOn)
# We can execute SubTask 1 first and then SubTask 2, since they cannot be parallized. 

# CODE
def put_mug_in_coffee_machine():
    # 0: SubTask 1: Put mug in the coffee machine
    # 1: Go to the Mug.
    GoToObject('Mug')
    # 2: Pick up the Mug.
    PickupObject('Mug')
    # 3: Go to the CoffeeMachine.
    GoToObject('CoffeeMachine')
    # 4: Put Mug in the CoffeeMachine
    PutObject('Mug', 'CoffeeMachine')

def switch_on_coffee_machine():
    # 0: SubTask 2: Switch on the coffee machine
    # 1: Go to the CoffeeMachine.
    GoToObject('CoffeeMachine')
    # 2: Switch on the CoffeeMachine.
    SwitchOn('CoffeeMachine')

# Execute SubTask 1
put_mug_in_coffee_machine()

# Execute SubTask 2
switch_on_coffee_machine()

# Task put mug in the coffee machine and switch on the coffee machine is done