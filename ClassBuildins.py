import pygame
import threading
import time
from ClassFloor import Floor
from ClassElevator import Elevator


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
REFRESH_RATE = 96

zero_line = 620
building_floor = 570
floor_heit = 51
f_heit_line = 57



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
    
    # def get_floors(self):
    #     return self.__floors
    
    def update_all_elevators(self):
        for elevator in self.__elevators:
            elevator.update()
        pygame.display.flip()
        clock.tick(REFRESH_RATE)

    
        """displays the number of second left until the elevator arrives"""
    def show_timer(self, timer, current_y, nearest_elevator): 
        my_floor = (zero_line - current_y) // floor_heit
        num_floor = building_floor - my_floor * floor_heit + 20
        timer += 0.5
        while timer != 0:
            timer -= 0.5
            elevator = a1.get_elevators()[nearest_elevator]
            elevator.set_till_available(timer)
            pygame.draw.circle(screen, GREY, (350, num_floor + 7), 22)
            pygame.display.flip()
            font = pygame.font.Font (None, 25)
            number = font.render(f"{timer}", True, (BLACK))
            screen.blit(number, (340, num_floor))
            pygame.display.flip()
            time.sleep(0.5)
        if timer == 0:
            pygame.draw.circle(screen, GREY, (350, num_floor + 7), 20)
            pygame.display.flip()
    
        """looks for the evelevator that will come in the shortest time, 
        and puts the requested floor in the queue of one of the elevator and returns how long it will come"""
    
    def get_neareste_elevator(self, num_floor): 
        data_elevator = [] * len(self.__elevators)
        for i in range (len(self.__elevators)):
            elevator = a1.get_elevators()[i]
            old_floor = (zero_line - elevator.get_dst()) // floor_heit
            timer = elevator.get_till_available() + ((abs(old_floor - num_floor)) * 0.5)
            if elevator.get_till_available() != 0:
                timer += 2
            data_elevator.append(timer)
        elv = a1.get_elevators()[data_elevator.index(min(data_elevator))]
        elv.put_queue(num_floor)
        elv.set_dst(building_floor - num_floor * floor_heit)
        nearest_elevator = data_elevator.index(min(data_elevator))
        timer = min(data_elevator)
        return (nearest_elevator, timer)
    
    def green_button(self, num_floor): #painting the button green
        for i in range (num_floor + 1) :
            y = building_floor - i * floor_heit
        font = pygame.font.Font (None, 25)
        number = font.render(f"{i}", True, (GREEN))
        screen.blit(number, (300, y + 20))
        pygame.display.flip()
    
    def button_management(self): #identifies the booked floor
        LEFT = 1
        left_side = 290
        right_side = 320
        down = 10
        up = 31
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            current_x, current_y = pygame.mouse.get_pos()
            if left_side < current_x < right_side and self.roof < current_y < zero_line and down < (zero_line - current_y) % floor_heit < up: 
                num_floor = (zero_line - current_y) // floor_heit
                self.green_button(num_floor)
                nearest_elevator, timer = a1.get_neareste_elevator(num_floor)
                my_threead1 = threading.Thread(target=self.show_timer, args=(timer, current_y, nearest_elevator))
                my_threead1.start()

    def constract_the_building(self): #draws the building
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
            screen.blit(img2, (x, building_floor))
    
 
a1 = Building(10, 5)            
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
            