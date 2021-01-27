import copy
import random

from .hillclimber import HillClimber


class HillClimber_double(HillClimber):

    def switch_houses_double_swap(self, new_grid):
        """
        based on the random switches but instead of picking only 2 houses and batteries at random, 
        this method retrieves 4 random houses. 2 from both batteries.
        """

        random_battery = random.choice(list(new_grid.batteries.values()))
        random_battery_2 = random.choice(list(new_grid.batteries.values()))
        while random_battery == random_battery_2:
            random_battery_2 = random.choice(list(new_grid.batteries.values()))
        # Get a random house from each battery
        house_1 = random.choice(random_battery.connect)
        house_2 = random.choice(random_battery.connect)
        while house_1 == house_2:
            house_2 = random.choice(random_battery.connect)
        output_1_2 = float(house_1.output) + float(house_2.output)
        house_3 = random.choice(random_battery_2.connect)
        house_4 = random.choice(random_battery_2.connect)
        while house_3 == house_4:
            house_4 = random.choice(random_battery_2.connect)
        output_3_4 = float(house_3.output) + float(house_4.output)
        new_battery_output = float(random_battery.total_output) - float(output_1_2) + float(output_3_4)
        new_battery_output_2 = float(random_battery_2.total_output) - float(output_3_4) + float(output_1_2)
        if new_battery_output <= float(random_battery.capacity) and new_battery_output_2 <= float(random_battery.capacity):
            old_distance_1 = self.get_manh_distance(house_1, random_battery) + self.get_manh_distance(house_2, random_battery)
            new_distance_1 = self.get_manh_distance(house_3, random_battery) + self.get_manh_distance(house_4, random_battery)
            old_distance_2 = self.get_manh_distance(house_3, random_battery_2) + self.get_manh_distance(house_4, random_battery_2)
            new_distance_2 = self.get_manh_distance(house_1, random_battery_2) + self.get_manh_distance(house_2, random_battery_2)
            if new_distance_1 <= old_distance_1 and new_distance_2 <= old_distance_2:
                random_battery.disconnect_house(house_1)
                random_battery.disconnect_house(house_2)
                random_battery_2.disconnect_house(house_3)
                random_battery_2.disconnect_house(house_4)
                random_battery.set_connection(house_3)
                random_battery.set_connection(house_4)
                random_battery_2.set_connection(house_1)
                random_battery_2.set_connection(house_2)
                return True
        return False


