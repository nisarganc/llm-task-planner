# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Cook the Potato. (Skills Required: GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff)
# SubTask 2: Put the cooked Potato in the Fridge. (Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject)
# We can execute SubTask 1 first and then SubTask 2, since they cannot be parallized. 

# CODE
def cook_potato():
    # 0: SubTask 1: Cook the Potato
    # 1: Go to the Potato.
    GoToObject('Potato')
    # 2: Pick up the Potato.
    PickupObject('Potato')
    # 3: Go to the Pan.
    GoToObject('Pan')
    # 4: Put the Potato in the Pan.
    PutObject('Potato', 'Pan')
    # 5: Pick up the pan with potato in it.
    PickupObject('Pan')
    # 6: Go to the StoveBurner.
    GoToObject('StoveBurner')
    # 7: Put the Pan on the stove burner.
    PutObject('Pan', 'StoveBurner')
    # 7: Switch on the StoveKnob.
    SwitchOn('StoveKnob')
    # 7: Wait for a while to let the Potato cook.
    time.sleep(5)
    # 8: Switch off the StoveKnob.
    SwitchOff('StoveKnob')
    # 9: Go to the Potato.
    GoToObject('Potato')
    # 10: Pick up the Potato.
    PickupObject('Potato')

def put_cooked_potato_in_fridge():
    # 0: SubTask 2: Put the cooked Potato in the Fridge
    # 1: Go to the Fridge.
    GoToObject('Fridge')
    # 2: Open the Fridge.
    OpenObject('Fridge')
    # 3: Put the cooked Potato in the Fridge
    PutObject('Potato', 'Fridge')
    # 4: Close Fridge
    CloseObject('Fridge')

# Execute SubTask 1
cook_potato()

# Execute SubTask 2
put_cooked_potato_in_fridge()

# Task Cook the potato and put it in the Fridge is done