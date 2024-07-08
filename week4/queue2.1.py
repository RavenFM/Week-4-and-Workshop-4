# Done

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.value

    def is_empty(self):
        return self.front is None

    def items(self):
        result = []
        current = self.front
        while current:
            result.append(current.value)
            current = current.next
        return result

class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor not in self.flavors:
            print("Sorry, we don't have that flavor.")
            print()
            return
        if scoops < 1 or scoops > 3:
            print("Please choose between 1-3 scoops")
            print()
            return
        
        print("Order created!")
        print()
        order = {"customer": customer, "flavor": flavor, "scoops": scoops}
        self.orders.enqueue(order)

    def show_all_orders(self):
        if self.orders.is_empty():
            print("No orders.")
            print()
            return
        print("All Pending Ice Cream Orders:")
        for order in self.orders.items():
            print(f"Customer: {order['customer']} -- Flavor: {order['flavor']} -- Scoops: {order['scoops']}")
        print()

    def next_order(self):
        if self.orders.is_empty():
            print("No pending orders.")
            print()
            return
        next_order = self.orders.dequeue()
        print(f"Next Order Up!\nCustomer: {next_order['customer']} -- Flavor: {next_order['flavor']} -- Scoops: {next_order['scoops']}")
        print()

# Testing
shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
