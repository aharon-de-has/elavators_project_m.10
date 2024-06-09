import pygame
import queue
import time
from Settings import *

class Elevator():
    def __init__(self, num):
        self.__current_y = building_floor
        self.__till_available = 0
        self.__queue = queue.Queue() #Queue for each elevator
        self.__num = num
        self.__t_end = 0 #End time of the last iteration, for the purpose of calculation the delay of 2 sec
        self.__dst = self.__current_y #The destination of the elevator
        self.__last_order = None #Calculation of the remaining time according to the last order
    

    def black_button(self, num_floor): #Paints the button black
        for i in range (num_floor + 1) :
            y = building_floor - i * floor_heit + 20
        font = pygame.font.Font (None, 25)
        number = font.render(f"{i}", True, (BLACK))
        screen.blit(number, (button_pos, y))


    """As long as there are orders in the queue, move the elevator by one pixel each iteration"""
    def update(self):
        t_start = time.perf_counter()
        if t_start - self.__t_end >= 2: #Checks that 2 second have passed since the end of the last operations
            if self.__queue.qsize() > 0:
                next_floor  = self.__queue.queue[0]
                dst = building_floor - next_floor * floor_heit 
                if dst != self.__current_y:
                    diff = dst - self.__current_y 
                    direction  = diff / abs(diff)
                    self.__current_y += direction * 1
                    x = location_left_elevator + self.__num * f_heit_line
                    screen.blit(img2,(x, self.__current_y))
                if dst == self.__current_y:
                    self.__queue.get() #Remove from the queue at the end of the action
                    pygame.mixer.music.load("ding.mp3") #Play the sound
                    pygame.mixer.music.play()
                    self.black_button(next_floor)
                    self.__t_end = time.perf_counter()
                    
                
           


    def get_current_floor(self):
        return self.__current_y
    
    def get_dst(self):
        return self.__dst
    
    def set_dst(self, new_floor):
        self.__dst = new_floor
    
    def set_current_floor(self, new_y):
        self.__current_y = new_y

    def set_num(self, num_elv):
        self.__num = num_elv

    def get_till_available(self):
        return self.__till_available
    
    def set_till_available(self, timer):
        self.__till_available = timer
    
    def put_queue(self, item):
        self.__queue.put(item)

    def get_dst(self):
        return self.__dst
    
    def set_last_order(self, item):
        self.__last_order = item

    def get_last_order(self):
        return self.__last_order
   
    



   