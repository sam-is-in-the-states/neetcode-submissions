class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))

        stack = []

        for pos, spd in reversed(cars):
            t = (target - pos) / spd

            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)