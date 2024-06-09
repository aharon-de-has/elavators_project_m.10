import pygame
import threading
import time
from ClassFloor import Floor
from ClassElevator import Elevator
from Settings import *


class Building:
    def __init__(self, floors: int, elevators: int):
        self.__floors = []
        for i in range(floors):
            self.__floors.append(Floor(i))
        self.__elevators = []
        for i in range(elevators):
            self.__elevators.append(Elevator(i))
        self.roof = 0

    def get_elevators(self):
        return self.__elevators
    
    def get_floors(self):
        return self.__floors
    
    """The function constantly updates all elevators"""
    def update_all_elevators(self):
        for elevator in self.__elevators:
            elevator.update()
        pygame.display.flip()
        clock.tick(REFRESH_RATE)

    def alloow_floor(self, num_floor, timer): #Allows ordering an elevator to the floor
        floor = a1.get_floors()[num_floor]
        time.sleep(timer)
        floor.set_elv_onway(False)

    
        """Displays the number of second until the elevator arrives
        args:
        1. timer: the second remaining for the elevator to arrive
        2. current y: convert y values to floor number
        3. nearest elevator: defines the end time of the elevator movement"""
    def show_timer(self, timer, current_y, nearest_elevator): 
        my_floor = (zero_line - current_y) // floor_heit #Ordered floor number
        num_floor = Building_floor_screen - my_floor * floor_heit  #y values of the floor
        timer += 0.5
        while timer != 0:
            timer -= 0.5
            pygame.draw.circle(screen, GREY, (show_circle_pos, num_floor + 7), 22)
            font = pygame.font.Font (None, 25)
            number = font.render(f"{timer}", True, (BLACK))
            screen.blit(number, (show_timer_pos, num_floor))
            time.sleep(0.5)
            elevator = a1.get_elevators()[nearest_elevator]
            if my_floor == elevator.get_last_order():
                elevator.set_till_available(timer) #Updates the ramaining time according to the last order
        if timer == 0:
            pygame.draw.circle(screen, GREY, (show_circle_pos, num_floor + 7), 20) #clears the screen if time resets
            
    
        """Looks for the evelevator that will come in the shortest time, 
        and puts the requested floor in the queue of one of the elevator and returns how long it will come
        args:
        int: The number of the floor ordered
        returns:
        1. Enters the floor number into the most available elevator queue
        2. Returns the time remaining for the elevator to arrive"""
    def get_neareste_elevator(self, num_floor): 
        data_elevator = [] * len(self.__elevators)
        for i in range (len(self.__elevators)):
            elevator = a1.get_elevators()[i]
            #Calcuates the time  remaining until the elevator is free + the different from the ending floor to the ordred floor
            old_floor = (zero_line - elevator.get_dst()) // floor_heit
            timer = elevator.get_till_available() + ((abs(old_floor - num_floor)) * 0.5)
            if elevator.get_till_available() != 0:
                timer += 2
            data_elevator.append(timer) #An array of times for each elevator
        elv = a1.get_elevators()[data_elevator.index(min(data_elevator))]
        elv.put_queue(num_floor)
        elv.set_last_order(num_floor) #The timer is counted according to the last order
        elv.set_dst(building_floor - num_floor * floor_heit) #The final location of the elevator
        nearest_elevator = data_elevator.index(min(data_elevator)) #We will identipy the elevator by its index
        timer = min(data_elevator)
        return (nearest_elevator, timer)
    
    
    def green_button(self, num_floor): #painting the button green
        for i in range (num_floor + 1) :
            y = Building_floor_screen - i * floor_heit
        font = pygame.font.Font (None, 25)
        number = font.render(f"{i}", True, (GREEN))
        screen.blit(number, (button_pos, y))
        pygame.display.flip()

    
    def button_management(self): #identifies the booked floor
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT: #There is a lept mouse click
            current_x, current_y = pygame.mouse.get_pos()
            #Marks the exact position of the button
            if left_side < current_x < right_side and self.roof < current_y < zero_line and down < (zero_line - current_y) % floor_heit < up: 
                num_floor = (zero_line - current_y) // floor_heit
                floor = a1.get_floors()[num_floor]
                if floor.get_elv_onway() != True: #There is no elevator on the way to the floor, preventing the arrival of 2 elevators at the same time.
                    floor.set_elv_onway(True)
                    self.green_button(num_floor) #Colors the button green
                    nearest_elevator, timer = a1.get_neareste_elevator(num_floor)
                    my_threead1 = threading.Thread(target=self.show_timer, args=(timer, current_y, nearest_elevator))
                    my_threead1.start() #Displays the remaining time until the elevator arrives
                    my_threead2 = threading.Thread(target=self.alloow_floor, args=(num_floor, timer))
                    my_threead2.start() #Allows ordering an elevator to a floor, after the elevator has already arrived

    
    def constract_the_building(self): #Draws the building
        for i in range (len(self.__floors)): 
            y = building_floor - i * floor_heit
            screen.blit(img1, (left_building, y)) #Draws the building 
            screen.blit(img3,(right_building, y)) #Draw the screen
            pygame.draw.line(screen, (BLACK), [left_building, y], [right_position_black_line, y], 7) #draw the blacg line
            font = pygame.font.Font (None, 25)
            number = font.render(f"{i}", True, (BLACK)) #Add a number to the floor
            screen.blit(number, (button_pos, y + 20)) #Draw the floor numbers
        self.roof = y #The roof of the building, used the mark place of the button
        for i in range (len(self.__elevators)):
            x = location_left_elevator + i * f_heit_line
            screen.blit(img2, (x, building_floor)) #Draw the elevators
    
 
a1 = Building(12, 4)            
a1.constract_the_building()     
    
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        else:
            a1.button_management()
            pygame.display.flip()
    a1.update_all_elevators()
            