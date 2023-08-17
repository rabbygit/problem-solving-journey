import heapq


class SeatManager:

    def __init__(self, n: int):
        self.available = [i for i in range(n, 0, -1)]
        heapq.heapify(self.available)

    def reserve(self) -> int:
        return heapq.heappop(self.available)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available, seatNumber)
