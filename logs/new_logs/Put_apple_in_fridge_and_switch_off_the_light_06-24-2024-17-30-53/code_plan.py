Set of actions required to perform the given task:
1. GoToObject <robot0><Apple>
2. PickupObject <robot0><Apple>
3. GoToObject <robot0><Fridge>
4. OpenObject <robot0><Fridge>
5. PutObject <robot0><Apple><Fridge>
6. CloseObject <robot0><Fridge>
7. GoToObject <robot1><LightSwitch>
8. SwitchOff <robot1><LightSwitch>

Dependencies between actions: 
step1 is independent of all other steps
step2 is dependent on step1
step3 is dependent on step2
step4 is dependent on step3
step5 is dependent on step4
step6 is dependent on step5
step7 is independent of all other steps
step8 is dependent on step7

Order of execution rules: Based on the action dependencies and the number of robots available. 
1. robot0 start step1 and robot1 start step7
2. robot0 wait to finish step1 and robot1 wait to finish step7
3. robot0 start step2 and robot1 start step8
4. robot0 wait to finish step2 then start step3
5. robot0 wait to finish step3 then start step4
6. robot0 wait to finish step4 then start step5
7. robot0 wait to finish step5 then start step6