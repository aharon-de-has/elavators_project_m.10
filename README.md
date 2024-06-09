# elavators_project_m.10
For the purpose of the project we used 3 classes.  
class Floor, whose data members is the number of the floor.  
class Elevator whose data members are: 
1. The location of the elevator at the current moment.  
2. How long will it be available?  
3. Elevator number.  
4. The end time of the last elevator movement, for the purpose of calculating the 2 second delay, when the elevator reaches the floor. 
5. The destination of the elevator is initialized to floor 0. 
6. For each elevator there is a queue.  
class building that receives a number of floors and a number of elevators and puts them into an array, and additional information which is the height of the building.  
When the building detects a press on one of the buttons, which means that an elevator has been ordered, it sends to a function that colors the button green, sends to a function that finds the most available elevator, enters the queue of that elevator and the time it will come, and sends to another function that displays the time on the screen.   Each elevator is responsible for its own movement, with each iteration moving one pixel.
