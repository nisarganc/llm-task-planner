# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Slice the Lettuce. (Skills Required: GoToObject, PickupObject, SliceObject, PutObject)
# SubTask 2: Trash the Mug. (Skills Required: GoToObject, PickupObject, PutObject)
# SubTask 3: Switch off the Light. (Skills Required: GoToObject, SwitchOff)
# We can parallelize SubTask 1, SubTask 2 and SubTask 3 because they don't depend on each other.

# CODE
def slice_lettuce():
    # 0: SubTask 1: Slice the Lettuce
    # 1: Go to the Knife.
    GoToObject('Knife')
    # 2: Pick up the Knife.
    PickupObject('Knife')
    # 3: Go to the Lettuce.
    GoToObject('Lettuce')
    # 4: Slice the Lettuce.
    SliceObject('Lettuce')
    # 5: Go to the countertop.
    GoToObject('CounterTop')
    # 6: Put the Knife back on the CounterTop.
    PutObject('Knife', 'CounterTop')

def trash_mug():
    # 0: SubTask 2: Trash the Mug
    # 1: Go to the Mug.
    GoToObject('Mug')
    # 2: Pick up the Mug.
    PickupObject('Mug')
    # 3: Go to the GarbageCan.
    GoToObject('GarbageCan')
    # 4: Put the Mug in the GarbageCan.
    PutObject('Mug', 'GarbageCan')

def switch_off_light():
    # 0: SubTask 3: Switch off the Light
    # 1: Go to the LightSwitch.
    GoToObject('LightSwitch')
    # 2: Switch off the LightSwitch.
    SwitchOff('LightSwitch')

# Parallelize SubTask 1, SubTask 2 and SubTask 3
task1_thread = threading.Thread(target=slice_lettuce)
task2_thread = threading.Thread(target=trash_mug)
task3_thread = threading.Thread(target=switch_off_light)

# Start executing SubTask 1, SubTask 2 and SubTask 3 in parallel
task1_thread.start()
task2_thread.start()
task3_thread.start()

# Wait for both SubTask 1, SubTask 2 and SubTask 3 to finish
task1_thread.join()
task2_thread.join()
task3_thread.join()

# Task Slice the lettuce, trash the mug and switch off the light is done