# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Put apple in the fridge. (Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject)
# SubTask 2: Switch off the light. (Skills Required: GoToObject, SwitchOff)
# We can parallelize SubTask 1 and SubTask 2 because they don't depend on each other.

# CODE
def put_apple_in_fridge():
    # 0: SubTask 1: Put apple in the fridge
    # 1: Go to the Apple.
    GoToObject('Apple')
    # 2: Pick up the Apple.
    PickupObject('Apple')
    # 3: Go to the Fridge.
    GoToObject('Fridge')
    # 4: Open the Fridge.
    OpenObject('Fridge')
    # 5: Put Apple in the Fridge
    PutObject('Apple', 'Fridge')
    # 6: Close Fridge
    CloseObject('Fridge')

def switch_off_light():
    # 0: SubTask 2: Switch off the light
    # 1: Go to the LightSwitch.
    GoToObject('LightSwitch')
    # 2: Switch off the LightSwitch.
    SwitchOff('LightSwitch')

# Parallelize SubTask 1 and SubTask 2
task1_thread = threading.Thread(target=put_apple_in_fridge)
task2_thread = threading.Thread(target=switch_off_light)

# Start executing SubTask 1 and SubTask 2 in parallel
task1_thread.start()
task2_thread.start()

# Wait for both SubTask 1 and SubTask 2 to finish
task1_thread.join()
task2_thread.join()

# Task put apple in fridge and switch off the light is done