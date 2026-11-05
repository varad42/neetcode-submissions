class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars = sorted(cars, reverse=True)
        stack = []

        for position,speed in cars:
            current_car_time = (target - position) / speed
            if len(stack) == 0 or current_car_time > stack[-1]:
                stack.append(current_car_time)

        return len(stack)
            