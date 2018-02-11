import os
import sys
import csv

class CarBase:
    def __init__(self,car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self,car_type, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(car_type,brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self,car_type, brand, photo_file_name, carrying, body_width, body_height, body_length):
        super().__init__(car_type, brand, photo_file_name, carrying)                  
        self.body_width = float(body_width)
        self.body_height = float(body_height)
        self.body_length = float(body_length)
    def get_body_volume(self):
        return self.body_width*self.body_height*self.body_length
             


class SpecMachine(CarBase):
    def __init__(self,car_type, brand, photo_file_name, carrying, extra):
        super().__init__( car_type,brand, photo_file_name, carrying)
        self.extra = extra


def fill_car(val):
    #if isinstance(val[2], int):
        return Car(val[0],val[3], val[1], val[5],  int(val[2]))

def fill_track(val):
        s = val[4]
        if s == "":
            s = [0,0,0]
            return Truck(val[0], val[3], val[1], val[5], s[0], s[1], s[2])
        else:
            s = val[4].split('x')
            #print(s)
            return Truck(val[0],val[3], val[1], val[5], s[0], s[1], s[2])

def fill_spec(val):
    return SpecMachine(val[0],val[3], val[1], val[5], val[6])

def get_car_list(csv_filename):
    car_list = []
    try:       
        with open(csv_filename) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
    except IOError:
        return ""
    else:   
            with open(csv_filename) as csv_fd:
                reader = csv.reader(csv_fd, delimiter=';')
                next(reader)  # пропускаем заголовок
                for row in reader:
                        if len(row):
                            #print(row[0].lower())
                            if row[0] and row[1] and row[5] and row[3]:
                                if row[0].lower() == 'car':
                                    
                                    #print('e')
                                    car_list.append(fill_car(row))                       
                                elif row[0].lower() == 'truck':
                                    #print('2')
                                   
                                    car_list.append(fill_track(row))                           
                                elif row[0].lower() == 'spec_machine':
                                    #print('4')
                                    car_list.append(fill_spec(row))      
                                else:
                                    continue
                            else:
                                continue
                        else:
                            continue
    return car_list

def _main():
    val = sys.argv[1]
    print(get_car_list(val))

if __name__ == '__main__':
    _main()