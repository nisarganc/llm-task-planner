# Independent SubTasks:
# SubTask 1: Put Mug in the CoffeeMachine. (Skills Required: GoToObject, PickupObject, PutObject)
# SubTask 2: Switch on the CoffeeMachine. (Skills Required: GoToObject, SwitchOn)
# We can execute SubTask 1 first and then SubTask 2.

# Task allocation solution:
# robot0, robot1 and robot2 have same skills and mass capacity. 
# The first SubTask, 'Put Mug in the CoffeeMachine' can be performed by any robot with 'GoToObject', 'PickupObject', and 'PutObject' skills. In this case, all robots have these skills. There is a need to address mass capacity as there is a skill, 'PickupObject' belonging to ObjectHandlingSkills set. This skill is performed on the object, 'Mug', whose mass capacity is 1.0. All robots have mass capacity greater than or equal to 1.0. Hence any robot can be allocated to this SubTask. We allocate robot0 to this SubTask.
# The second SubTask, 'Switch on the CoffeeMachine' can be performed by any robot with 'GoToObject' and 'SwitchOn' skills. In this case, all robots have these skills. There is no need to address mass capacity as there are no ObjectHandlingSkills in this SubTask. Since robot0 is already engaged with SubTask 1, we allocate robot1 to this SubTask.

# Task allocation code:
def put_mug_in_coffee_machine(robot_list):
    # 0: SubTask 1: Put Mug in the CoffeeMachine
    # 1: Go to the Mug using robot0.
    simulate.GoToObject(robot_list[0], 'Mug')
    # 2: Pick up the Mug using robot0.
    simulate.PickupObject(robot_list[0], 'Mug')
    # 3: Go to the CoffeeMachine using robot0.
    simulate.GoToObject(robot_list[0], 'CoffeeMachine')
    # 4: Put the Mug in the CoffeeMachine using robot0.
    simulate.PutObject(robot_list[0], 'Mug', 'CoffeeMachine')

def switch_on_coffee_machine(robot_list):
    # 0: SubTask 2: Switch on the CoffeeMachine
    # 1: Go to the CoffeeMachine using robot1.
    simulate.GoToObject(robot_list[1], 'CoffeeMachine')
    # 2: Switch on the CoffeeMachine using robot1.
    simulate.SwitchOn(robot_list[1], 'CoffeeMachine')

# Perform SubTask 1 and then SubTask 2
put_mug_in_coffee_machine(robots)
switch_on_coffee_machine(robots)

# Task, 'put mug in the coffee machine and switch on the coffee machine' is done.