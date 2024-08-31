Set of actions required to perform the given task:
1. GoToObject <robot><Mug>
2. PickupObject <robot><Mug>
3. GoToObject <robot><CoffeeMachine>
4. PutObject <robot><Mug><CoffeeMachine>
5. SwitchOn <robot><CoffeeMachine>

Dependencies between actions: 
step1 is independent of all other steps
step2 is dependent on step1
step3 is dependent on step2
step4 is dependent on step3
step5 is dependent on step4

Order of execution rules: Based on the action dependencies and the number of robots available. 
1. robot0 start step1
2. robot0 wait to finish step1 and then start step2
3. robot0 wait to finish step2 and then start step3
4. robot0 wait to finish step3 and then start step4
5. robot0 wait to finish step4 and then start step5