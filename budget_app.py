class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):

        title = self.name.center(30, "*") + "\n"
        items = ""

        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"
            items += f"{description:<23}{amount:>7}\n"

        total = f"Total: {self.get_balance()}"

        return title + items + total


def create_spend_chart(categories):

    title = "Percentage spent by category\n"

    spent = []
    total_spent = 0

    for category in categories:
        amount = 0
        for item in category.ledger:
            if item["amount"] < 0:
                amount += -item["amount"]
        spent.append(amount)
        total_spent += amount

    percentages = []

    for s in spent:
        percent = int((s / total_spent) * 100)
        percent = percent - (percent % 10)
        percentages.append(percent)

    chart = ""

    for i in range(100, -1, -10):

        chart += str(i).rjust(3) + "| "

        for p in percentages:
            if p >= i:
                chart += "o  "
            else:
                chart += "   "

        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    names = [c.name for c in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):

        line = "     "

        for name in names:

            if i < len(name):
                line += name[i] + "  "
            else:
                line += "   "

        if i != max_len - 1:
            line += "\n"

        chart += line

    return title + chart

food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

food.deposit(1000, "initial deposit")
food.withdraw(200, "groceries")

clothing.deposit(500)
clothing.withdraw(100)

auto.deposit(1000)
auto.withdraw(400)

print(food)
print(create_spend_chart([food, clothing, auto]))