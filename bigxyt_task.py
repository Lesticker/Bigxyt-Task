import os
class Activity:
    def __init__(self, id, order, type, price, quantity):
        self.id = id
        self.order = order
        self.type = type
        self.price = price
        self.quantity = quantity
    
    def printer(self):
        return f"{self.id} {self.order} {self.type} {self.price} {self.quantity}"

    def __str__(self):
        return f"{self.id} {self.order} {self.type} {self.price} {self.quantity}"
        

orders = list()

if os.path.isfile("orders.csv"):
    with open("orders.csv") as f:
        csv_orders = f.readlines()
        for orders_line in csv_orders:
            order_info = orders_line.rstrip().split(" ")
            order = Activity(
                order_info[0],
                order_info[1],
                order_info[2],
                order_info[3],
                order_info[4])
            orders.append(order)

user_input = ""
         
while user_input != "q":

    print("Options")
    print("1 - Create order")
    print("2 - Display orders")
    print("3 - Find best prices")
    print("q - Quit")
    user_input = input ("Choose option: ")

    if user_input == "1":
        print("Enter Order")

        while True:
            try:
                id = int(input("enter order id: ").zfill(3))
            except ValueError:
                print("This is not a number. Try again.")
            else:
                break

        order = input("Buy or Sell order? ")
        type = input("Add or Remove? ")

        while True:
            try:
                price = float(input("Enter price: "))
            except ValueError:
                print("This is not a number. Try again.")
            else:
                break

        while True:
            try:
                quantity = int(input("Enter amount: "))
            except ValueError:
                print("This is not a number. Try again.")
            else:
                break

        new_order = Activity(id, order, type, price, quantity)
        orders.append(new_order)

        with open("orders.csv", "w") as f:
            for i in orders:
                f.write(f"{i.id} {i.order} {i.type} {i.price} {i.quantity}\n")
    
        print("New order has been made")

    elif user_input == "2":

        for i in orders:
            print(i)

    elif user_input == "3":

        count = len(open("orders.csv").readlines(  ))
        f = open("orders.csv", "r")

        sell_list = []
        buy_list = []
        
        lowest_sell_price = 0
        summary_sell_quantity = 0
        
        highest_buy_price = 0
        summary_buy_quantity = 0
        
        price_sell = 0
        price_buy = 0
        
        for value in range(count):
            value = f.readline().split()
        
            if value[1] == "Sell":
                sell_list.append(value)
                price_sell_next = float(value[3])

                if price_sell_next < price_sell or price_sell == 0:
                    summary_sell_quantity = int(value[4])
                    lowest_sell_price = price_sell_next
                    price_sell = price_sell_next
                
                elif price_sell_next == price_sell:
                    sell_quantity_next = int(value[4])
                    summary_sell_quantity = sell_quantity_next + summary_sell_quantity
        
            if value[1] == "Buy":
                buy_list.append(value)
                price_buy_next = float(value[3])

                if price_buy_next > price_buy:
                    summary_buy_quantity = int(value[4])
                    highest_buy_price = price_buy_next
                    price_buy = price_buy_next
        
                elif price_buy_next == price_buy:
                    buy_quantity_next = int(value[4])
                    summary_buy_quantity =buy_quantity_next + summary_buy_quantity

        sell_list = min(sell_list, key=lambda x: float(x[3]))
        sell_list[4] = summary_sell_quantity
        print("Summed best Sell Orders: ", sell_list)

        buy_list = max(buy_list, key=lambda x: float(x[3]))
        buy_list[4] = summary_buy_quantity
        print("Summed best Buy Orders: ", buy_list)
            
    elif user_input =="q":
        break


