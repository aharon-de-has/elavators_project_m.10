import pygame
import queue
import sys
import time
import threading

pygame.init()

WHITE = (245, 245, 245)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GREY = (220, 220, 220)


window_width, window_heigh = 1024, 633
size = (window_width, window_heigh)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("elevator")
screen.fill(WHITE)
pygame.display.flip()

img_bld = 'WhatsApp Image 2024-05-30 at 09.15.01.jpeg'
img1 = pygame.image.load(img_bld).convert()
# screen.blit(img1,(20, 613))
# pygame.display.flip()

img_elv = 'WhatsApp Image 2024-05-29 at 18.33.11.jpeg'
img2 = pygame.image.load(img_elv).convert()


img_screen = 'WhatsApp Image 2024-05-30 at 09.59.45.jpg'
img3 = pygame.image.load(img_screen).convert()
# screen.blit(img3,(200, 100))
# pygame.display.flip()


clock = pygame.time.Clock()
REFRESH_RATE = 97

zero_line = 620
building_floor = 570
floor_heit = 51
f_heit_line = 57


class Elevator():
    def __init__(self, num):
        self.__current_floor = building_floor
        self.__till_available = 0
        self.__queue = queue.Queue()
        self.__num = num

    def black_button(self, num_floor):
        for i in range (num_floor + 1) :
            y = building_floor - i * floor_heit
        font = pygame.font.Font (None, 25)
        number = font.render(f"{i}", True, (BLACK))
        screen.blit(number, (300, y + 20))

    def update(self):
        if self.__queue.qsize() > 0:
            next_floor  = self.__queue.queue[0]
            dst = building_floor - next_floor * floor_heit
            src = self.__current_floor
            if dst != src:
                diff = dst - self.__current_floor 
                direction  = diff / abs(diff)
                self.__current_floor += direction * 1
                x = 395 + self.__num * f_heit_line
                screen.blit(img2,(x, self.__current_floor))
            if dst == self.__current_floor:
                self.__queue.get()
                pygame.mixer.music.load("ding.mp3")
                pygame.mixer.music.play()
                black_button(next_floor)
                # time.sleep(2)


    def get_current_floor(self):
        return self.__current_floor
    
    def set_current_floor(self, new_y):
        self.__current_floor = new_y

    def set_num(self, nearest_elevator):
        self.__num = nearest_elevator

    def get_till_available(self):
        return self.__till_available
    
    def set_till_available(self, timer):
        self.__till_available = timer
    
    def put_queue(self, item):
        self.__queue.put(item)

   
       

    
class Floor():
    def __init__(self, num):
        self.__floor_num = num

        
class Building:
    def __init__(self, floors: int, elevators: int):
        self.__floors = []
        for i in range(floors):
            self.__floors.append(Floor(i))
        self.__num_elevators = elevators
        self.__elevators = []
        for i in range(elevators):
            self.__elevators.append(Elevator(i))
        self.roof = 0
        
    
    def get_elevators(self):
        return self.__elevators
    def update_all_elevators(self):
        for elevator in self.__elevators:
            elevator.update()
            pygame.display.flip()
            clock.tick(REFRESH_RATE * self.__num_elevators) 
    

    def constract_the_building(self):
        for i in range (len(self.__floors)):
            y = building_floor - i * floor_heit
            screen.blit(img1, (20, y))
            screen.blit(img3,(280, y))
            pygame.draw.line(screen, (BLACK), [20, y], [386, y], 7)
            font = pygame.font.Font (None, 25)
            number = font.render(f"{i}", True, (BLACK))
            screen.blit(number, (300, y + 20))
        self.roof = y #the roof of the building
        for i in range (len(self.__elevators)):
            x = 395 + i * f_heit_line
            screen.blit(img2, (x, 570))


    def button(self): #identifies the booked floor
        LEFT = 1
        left_side = 290
        right_side = 320
        down = 10
        up = 31
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            current_x, current_y = pygame.mouse.get_pos()
            if left_side < current_x < right_side and self.roof < current_y < zero_line and down < (zero_line - current_y) % floor_heit < up: 
                num_floor = (zero_line - current_y) // floor_heit
                green_button(num_floor)
                nearest_elevator, timer = a1.get_neareste_elevator(num_floor)
                my_threead1 = threading.Thread(target=self.show_timer, args=(timer, current_y, nearest_elevator))
                my_threead1.start()
                # self.move_elv(num_floor, nearest_elevator)
                # pygame.mixer.music.load("ding.mp3")
                # pygame.mixer.music.play()
                # black_button(num_floor)
                

    def show_timer(self, timer, current_y, nearest_elevator):
        my_floor = (zero_line - current_y) // floor_heit
        num_floor = building_floor - my_floor * floor_heit + 20
        timer += 0.5
        while timer != 0:
            timer -= 0.5
            elevator = a1.get_elevators()[nearest_elevator]
            elevator.set_till_available(timer)
            pygame.draw.circle(screen, GREY, (350, num_floor + 7), 20)
            pygame.display.flip()
            font = pygame.font.Font (None, 25)
            number = font.render(f"{timer}", True, (BLACK))
            screen.blit(number, (340, num_floor))
            pygame.display.flip()
            time.sleep(0.5)
        if timer == 0:
            pygame.draw.circle(screen, GREY, (350, num_floor + 7), 20)
            pygame.display.flip()

    
    def move_elv(self, num_floor, nearest_elevator):
        elevator = a1.get_elevators()[nearest_elevator]
        x = 395 + nearest_elevator * f_heit_line
        y = elevator.get_current_floor()
        screen.blit(img2,(x, y))
        pygame.display.flip()
        new_y = building_floor - (num_floor * floor_heit)
        while y != new_y:
            if new_y < y:
                y -= 1
            else:
                y += 1
            screen.blit(img2,(x, y))
            pygame.display.flip()
            clock.tick(REFRESH_RATE) 
            elevator.set_current_floor(y)


      



    def get_neareste_elevator(self, num_floor):
        data_elevator = [] * len(self.__elevators)
        for i in range (len(self.__elevators)):
            elevator = a1.get_elevators()[i]
            new_floor = (zero_line - elevator.get_current_floor()) // floor_heit
            timer = elevator.get_till_available() + ((abs(new_floor - num_floor)) * 0.5)
            if elevator.get_till_available() != 0:
                timer += 2
            data_elevator.append(timer)
        elv = a1.get_elevators()[data_elevator.index(min(data_elevator))]
        elv.put_queue(num_floor)
        nearest_elevator = data_elevator.index(min(data_elevator))
        elevator = a1.get_elevators()[nearest_elevator]
        elevator.set_num(nearest_elevator)
        elevator.set_till_available(timer)
        timer = min(data_elevator)
        return (nearest_elevator, timer)
        
     
    



    
def black_button(num_floor):
    for i in range (num_floor + 1) :
        y = building_floor - i * floor_heit
    font = pygame.font.Font (None, 25)
    number = font.render(f"{i}", True, (BLACK))
    screen.blit(number, (300, y + 20))
   
    
    

def green_button(num_floor): #painting the button green
    for i in range (num_floor + 1) :
        y = building_floor - i * floor_heit
    font = pygame.font.Font (None, 25)
    number = font.render(f"{i}", True, (GREEN))
    screen.blit(number, (300, y + 20))
    pygame.display.flip()
   




          
    

a1 = Building(12, 5)            
a1.constract_the_building()                   
 
        

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        else:
            a1.button()
            # print(pygame.mouse.get_pos())
            pygame.display.flip()
            # clock.tick(REFRESH_RATE) 
    a1.update_all_elevators()
            













# def get_neareste_elevator(self, num_floor):
#         data_elevator = [] * len(self.__elevators)
#         for i in range (len(self.__elevators)):
#             elevator = a1.get_elevators()[i]
#             new_floor = (zero_line - elevator.get_current_floor()) // floor_heit
#             timer = elevator.get_till_available() + ((abs(new_floor - num_floor)) * 0.5)
#             if elevator.get_till_available() != 0:
#                 timer += 2
#             data_elevator.append(timer)
#         nearest_elevator = data_elevator.index(min(data_elevator))
#         timer = min(data_elevator)
#         return (nearest_elevator, timer)
        







    # def move_elv(num_floor):
    #     elevator = a1.get_elevators()[2]
    #     x = 395
    #     y = elevator.get_current_floor()
    #     screen.blit(img2,(x, y))
    #     pygame.display.flip()
    #     new_y = building_floor - (num_floor * floor_heit)
    #     while y != new_y:
    #         # pygame.time.delay(8)
    #         if new_y < y:
    #             y -= 1
    #         else:
    #             y += 1
    #         # img2.fill(WHITE)
    #         screen.blit(img2,(x, y))
    #         pygame.display.flip()
    #     elevator.set_current_floor(y)




    # # def move_elv(self, num_floor, nearest_elevator):
    #     for i in range (len(self.__elevators)):
    #         elv = a1.get_elevators()[i]
    #         y = elv.get_current_floor
    #         new_y = building_floor - num_floor * floor_heit
    #     while y != new_y:
    #         # queue_elevator = [] * len(self.__elevators)
    #         # for i in range (len(self.__elevators)):
    #         #     elevator = a1.get_elevators()[i]
    #         #     x = 395 + i * f_heit_line
    #         #     y = elevator.get_current_floor()
    #         # screen.blit(img2,(x, y))
    #         # pygame.display.flip()
    #         for i in range (len(elv)):
    #             if i.queue:
    #                 if new_y < y:
    #                     y -= 1
    #                 else:
    #                     y += 1
    #         # a1.button()
    #                 screen.blit(img2,(x, y))
    #                 pygame.display.flip()
    #                 clock.tick(REFRESH_RATE) 
    #             elevator.set_current_floor(y)
        




 


