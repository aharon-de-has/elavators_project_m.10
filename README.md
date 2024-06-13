# elavators_project_m.10

The assignment is to design and build an efficient elevator system using the python language.
After running the code, the user will see the building that will include the floors, elevators and elevator controls.
An elevator call control will be displayed on each floor with the floor number written on it. Pressing the button will order an elevator to the floor (even if there is no elevator available at the moment).
When ordering an elevator to a floor, a decreasing number will be displayed next to the elevator button representing the number of seconds remaining until the elevator arrives.
The elevator algorithm must bring to the minimum possible waiting time for the elevator without extending the waiting times of those who have already ordered an elevator.
Setting/changing the number of floors and the number of elevators in the building must be allowed in a simple way (by changing settings in the code or a settings file).
The elevators will move at a speed of half a second per floor (the movement must be presented in a smooth animation - and not, for example, jumping between floors), and when they reach the destination floor (to which the elevator was ordered), they will be delayed for two seconds.


For the purpose of the project we used 3 classes.  
class Floor, whose data members is the number of the floor.  
1. floor number
2. indicates whether there is already an elevator on the way to this floor

class Elevator whose data members are: 
1. The location of the elevator at the current moment.  
2. How long will it be available?  
3. Elevator number.  
4. The end time of the last elevator movement, for the purpose of calculating the 2 second delay, when the elevator reaches the floor. 
5. The destination of the elevator is initialized to floor 0. 
6. For each elevator there is a queue.  
7. Holds the number of the most recently ordered floor, so that the timer's updates will be update from it

class building that receives a number of floors and a number of elevators and puts them into an array, and additional information which is the height of the building.  
When the building detects a press on one of the buttons, which means that an elevator has been ordered, it sends to a function that colors the button green, sends to a function that finds the most available elevator, enters the queue of that elevator and the time it will come, and sends to another function that displays the time on the screen.   Each elevator is responsible for its own movement, with each iteration moving one pixel.

Since we did not use while, except for the main one, we can order sevaral at the same time
