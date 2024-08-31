# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Prepare the Plate with Egg and Tomato. (Skills Required: GoToObject, PickupObject, PutObject)
# SubTask 2: Microwave the Plate. (Skills Required: GoToObject, PickupObject, PutObject, OpenObject, CloseObject, SwitchOn, SwitchOff)
# We can execute SubTask 1 first and then SubTask 2, since they cannot be parallized. 

# CODE
def prepare_plate():
    # 0: SubTask 1: Prepare the Plate with Egg and Tomato
    # 1: Go to the Egg.
    GoToObject('Egg')
    # 2: Pick up the Egg.
    PickupObject('Egg')
    # 3: Go to the Plate.
    GoToObject('Plate')
    # 4: Put the Egg on the Plate.
    PutObject('Egg', 'Plate')
    # 5: Go to the Tomato.
    GoToObject('Tomato')
    # 6: Pick up the Tomato.
    PickupObject('Tomato')
    # 7: Go to the Plate.
    GoToObject('Plate')
    # 8: Put the Tomato on the Plate.
    PutObject('Tomato', 'Plate')

def microwave_plate():
    # 0: SubTask 2: Microwave the Plate
    # 1: Go to the Plate.
    GoToObject('Plate')
    # 2: Pick up the Plate.
    PickupObject('Plate')
    # 3: Go to the Microwave.
    GoToObject('Microwave')
    # 4: Open the Microwave.
    OpenObject('Microwave')
    # 5: Put the Plate in the Microwave.
    PutObject('Plate', 'Microwave')
    # 6: Close the Microwave.
    CloseObject('Microwave')
    # 7: Switch on the Microwave.
    SwitchOn('Microwave')
    # 8: Wait for a while to let the food cook.
    time.sleep(5)
    # 9: Switch off the Microwave.
    SwitchOff('Microwave')
    # 10: Open the Microwave.
    OpenObject('Microwave')
    # 11: Pick up the Plate.
    PickupObject('Plate')
    # 12: Close the Microwave.
    CloseObject('Microwave')
    # 13: Go to the CounterTop.
    GoToObject('CounterTop')
    # 14: Put the Plate on the CounterTop.
    PutObject('Plate', 'CounterTop')

# Execute SubTask 1
prepare_plate()

# Execute SubTask 2
microwave_plate()

# Task Microwave a plate containg a egg and a tomato is done