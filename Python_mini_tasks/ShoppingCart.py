class ShoppingCart:
    def __init__(self, prices):
        self.prices = prices

    def total_bill(self):
        return sum(self.prices)

    def costliest_item(self):
        return max(self.prices)

    def discounted_bill(self):
        total = self.total_bill()

        if total > 5000:
            total = total - (0.15 * total)

        return total


prices = list(map(int, input("Prices: ").split()))

s = ShoppingCart(prices)

print("Total Bill:", s.total_bill())
print("Costliest Item:", s.costliest_item())
print("Discounted Bill:", int(s.discounted_bill()))