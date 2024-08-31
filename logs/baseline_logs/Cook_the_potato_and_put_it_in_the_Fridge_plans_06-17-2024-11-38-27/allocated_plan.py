# Robot 1, 2 and 3 have 13 skills. All robots do have same number of skills.
# All the robots share the same set and number of skills (no_skills) & all objects DONOT have same mass. In this case where all robots have same skills and all objects have different mass- Focus on Task Allocation based on Mass alone. 
# Analyze the mass required for each object being PickedUp by the 'PickupObject' skill, and the mass capacity each robot possesses. In this scenario, we have two main subtasks: 'Cook the Potato' and 'Put the cooked Potato in the Fridge'.
# For the 'Cook the Potato' subtask, mass of the Potato is 0.18000000715255737 which is less than or equal to any robot's mass capacity. Hence it can be performed by any robot with a mass capacity greater than or equal to 0.18000000715255737.
# For 'Put the cooked Potato in Fridge', again, it can be performed by any robot with a mass capacity greater than or equal to 0.18000000715255737.
# No teams are required since SubTasks can be performed with individual robots as explained above.
# The 'Cook the Potato' subtask is assigned to Robot 1 since it has a higher mass capacity which might be useful for other tasks later on.
# The 'Put cooked potato in fridge' subtask is assigned to Robot 2 since it has a lower but sufficient mass capacity for this task.