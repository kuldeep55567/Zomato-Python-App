class Order:
    def __init__(self, order_id, customer_name, dish_ids, status):
        self.order_id = order_id
        self.customer_name = customer_name
        self.dish_ids = dish_ids
        self.status = status    

def menuItem(name, id, price, stock):
    obj = {}
    obj["name"] = name
    obj["id"] = id
    obj["price"] = price
    obj["stock"] = stock
    return obj

class Zomato:
    def __init__(self):
       self.menu=[]
       self.orders=[]
       self.next_order_id=1

    def addDish(self, dish):
        self.menu.append(dish)
        print(f"Dish '{dish['name']}' added to Inventory.")

    def removeDish(self, id):
        for i in self.menu:
            if i['id'] == id:
                self.menu.remove(i)
                print(f"Dish '{i['name']}' has been removed from Inventory.")
                return
        print("Dish not found in the menu.")

    def updateStock(self, id, stock):
        for i in self.menu:
            if i['id'] == id:
                i['stock'] = stock
                print(f"Dish '{i['name']}' Stock's has been updated")
                return
        print("Dish not found in Inventory.")

    def takeOrder(self, cName, dish_id,quantity):
        dishes = []
        for id in dish_id:
            found = False
            for dish in self.menu:
                if dish['id'] == id:
                    found = True
                    if dish['stock'] >= quantity:
                        dish['stock'] -=quantity
                        dishes.append(dish)
                    else:
                        print(f"Dish '{dish['name']}' is currently out of Stock.")
                    break
            if not found:
                print(f"Dish with ID '{id}' not found in Inventory")

        if dishes:
            order_id = self.next_order_id
            order = Order(order_id, cName, dish_ids, "received")
            self.orders.append(order)
            self.next_order_id += 1
            print(f"Order placed successfully. Order ID: {order_id}")

    def update_order_status(self, id, status):
        for o in self.orders:
            if o.order_id == id:
                o.status = status
                print(f"Order ID {id} status has been updated to '{status}'.")
                return
        print("Order not found.")

    def review_orders(self):
        if self.orders:
            print("All orders:")
            for order in self.orders:
                print(f"Order ID: {order.order_id}, Customer: {order.customer_name}, Status: {order.status}")
        else:
            print("No orders found.")

def print_menu():
    print("\n====Restaurant Menu====")
    for dish in zomato.menu:
        print(f"Dish ID: {dish['id']}, Name: {dish['name']}, Price: {dish['price']}, Stock: {dish['stock']}")

def print_options():
    print("\n=====Zomato Restaurant Management=====")
    print("1. Add dish to the menu")
    print("2. Remove dish from the menu")
    print("3. Update Stock of item")
    print("4. Recieve new order:")
    print("5. Update order status")
    print("6. Review all orders")
    print("7. View Menu")
    print("8. Exit")

# create an instance of zomato = Zomato()
zomato = Zomato()
# main program loop
while True:
    print_options()
    choice = input("Enter your choice: ")
    if choice == "1":
        dish_id = input("Enter dish ID: ")
        dish_name = input("Enter dish name: ")
        price = float(input("Enter dish price: "))
        stock = input("Enter dish Stock: ")
        dish = menuItem(dish_name, dish_id, price, stock)
        zomato.addDish(dish)

    elif choice == "2":
        dish_id = input("Enter dish ID to remove: ")
        zomato.removeDish(dish_id)
    elif choice == "3":
        dish_id = input("Enter dish ID to update Stocks: ")
        stock= input("Enter dish Stocks: ")
        zomato.updateStock(dish_id, stock)

    elif choice == "4":
        customer_name = input("Enter customer name: ")
        quantity = input("Enter Dish Quantity: ")
        dish_ids = input("Enter dish IDs (comma-separated): ").split(",")
        zomato.takeOrder(customer_name, dish_ids,quantity)

    elif choice == "5":
        order_id = input("Enter order ID to update status: ")
        status = input("Enter new status: ")
        zomato.update_order_status(order_id, status)

    elif choice == "6":
        zomato.review_orders()
    elif choice == "7":
        print_menu()
    elif choice == "8":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")