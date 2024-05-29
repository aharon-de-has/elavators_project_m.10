import pygame
import queue
import numpy

window_width = 700
window_heigh = 500

pygame.init()
size = (window_width, window_heigh)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("game")

pygame.quit()

WHITE = (255, 255, 255)
finish = False
while not finish:
    screen.fill(WHITE)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True



# class Elevator():
#     def __init__(self):
#         self.__current_floor = 0
#         self.__till_available = 0
#         self.__queue = queue.Queue()

#     def move_elevator():
#         pygame

    
# class Floor():
#     def __init__(self, num):
#         self.__floor_num = num
#         pygame.mouse
#         pygame.timer

        
# class Building:
#     def __init__(self, floors: int, elevators: int):
#         self.__floors = []
#         for i in range(floors):
#             self.__floors.append(Floor(i))
#         self.__elevators = []
#         for i in range(elevators):
#             self.__elevators.append(Elevator(i))
#         self.__request = queue.Queue()

    

#     def get_neareste_elevator(self,__request):
#         data_elevator = [] * len(self.__elevators)
#         for elevator in self.__elevators:
#             timer = self.__till_available + ((abs(self.current_floor - self.__floor_num)) * 0.5)
#             if self.__till_available != 0:
#                 timer += 2
#             data_elevator[elevator] = timer
#         self.__queue.put(data_elevator.index(min(data_elevator))) #need to be precise
#         return min(data_elevator)

    
#     def control(self, floor_num): 
#         self.__request.put(floor_num)
#         neareste = get_neareste_elevator(__request) #need to be precise
        


    
    




