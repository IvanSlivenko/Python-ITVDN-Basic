class Car:
    def __init__(self, name):
        self.__name_speed_dict = {
            "Mersedes": 250,
            "BMW": 300
        }
        self.__max_speed = self._define_max_speed(name)
        self.__car_name = self._define_name_car((name))


    def _define_name_car(self, name):
        for i in self.__name_speed_dict.keys():
            if i == name:
                return i


    def _define_max_speed(self, name):
        return self.__name_speed_dict.get(name, 0)

    def distanse_time_on_max_speed(self, distance):
        if not self.__max_speed:
            print("No speed param specified.")
            return 0
        print(f' Для автомобіля з назвою {self.__car_name}: час подолання дистанції {distance} складає {round(distance / self.__max_speed,2)} години')
        return distance / self.__max_speed


car_a = Car(name='BMW')
car_b = Car(name='Mersedes')
car_a.distanse_time_on_max_speed(distance=167)
car_b.distanse_time_on_max_speed(distance=167)

# print(car_a.distanse_time_on_max_speed(distance=167))
# print(car_b.distanse_time_on_max_speed(distance=167))
print('------------------------------------------------')