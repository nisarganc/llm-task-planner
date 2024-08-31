# Robot 1, 2 and 3 have 13 skills. All robots do have same number of skills.
# All the robots share the same set and number of skills (no_skills) & all objects DONOT have same mass. In this case where all robots have same skills and all objects have different mass- Focus on Task Allocation based on Mass alone. 
# Analyze the mass required for each object being PickedUp by the 'PickupObject' skill, and the mass capacity each robot possesses. In this scenario, we have two main subtasks: 'Put apple in the fridge' and 'Switch off the light'.
# For the 'Put apple in the fridge' subtask, mass of Apple is 0.20000000298023224 which is less than or equal to any robot's mass capacity. Hence it can be performed by any robot with a mass capacity greater than or equal to 0.20000000298023224.
# For the 'Switch off light' subtask, no object needs to be picked up hence no need to consider object's mass for this task.
# No teams are required since SubTasks can be performed with individual robots as explained above.
# The 'Put apple in fridge' subtask is assigned to Robot 1 since it has a higher available capacity after performing this task compared to other Robots.
# The 'Switch off light' subtask is assigned to Robot 2 since it has not been assigned any task yet and it has enough skill set required for this task.