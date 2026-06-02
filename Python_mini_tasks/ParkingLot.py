class ParkingLot:
    def __init__(self, vehicles):
        self.vehicles = vehicles

    def duplicates(self):
        seen = set()
        dup = set()

        for v in self.vehicles:
            if v in seen:
                dup.add(v)
            else:
                seen.add(v)

        return list(dup)

    def unique_count(self):
        return len(set(self.vehicles))


vehicles = list(map(int, input("Vehicle Numbers: ").split()))

p = ParkingLot(vehicles)

print("Duplicate Vehicles:", p.duplicates())
print("Unique Vehicles:", p.unique_count())