class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        cars = [(p, s) for p, s in zip(position, speed)]  # [position, speed]
        cars.sort(reverse = True)

        time_stack = []
        for pos, speed in cars:
            time = (target - pos) / float(speed)
            time_stack.append(time)
            if len(time_stack) >= 2 and time_stack[-1] <= time_stack[-2]:
                # means they collide, so pop off the stack because it's technically part of one fleet now
                time_stack.pop()

        return len(time_stack)
        