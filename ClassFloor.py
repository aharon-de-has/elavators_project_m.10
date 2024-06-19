from Settings import *
import time

class Floor():
    def __init__(self, num):
        self.__floor_num = num
        self.__elv_onway = False #checks whether an elevator has already been orded for the floor, so that 2 elevators do not come to ona floor
      


    def set_elv_onway(self, item):
        self.__elv_onway = item

    def get_elv_onway(self):
        return self.__elv_onway  
