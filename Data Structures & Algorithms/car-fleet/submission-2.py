class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # n cars going to destination
        # given array position and speed
        # pos[i] is position of ith car (m)
        # speed[i] is speed of ith car (mph)

        # desitination is pos *target* miles
        # car can't pass another car ahead of it, but can catch up AND drive at same speed
        # car fleet is set of cars driving at same pos. A single car is considered 1 fleet
        # if car catches up to car fleet when fleet reaches destination, it is considered in fleet
        # return num of different car fleets
        # must be O(nlogn)

        fleet = 0
        cars = zip(position, speed)

        sorted_cars = sorted(cars, reverse=True)

        fleet_leader_time = 0
        for pos, speed in sorted_cars:
            time = (target - pos) / speed
            
            if time > fleet_leader_time:
                fleet += 1
                fleet_leader_time = time

            


        return fleet    

        