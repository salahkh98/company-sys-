from company import Company
from data import Data

data = Data()
company = Company()

running = True
while running:

    input("press enter to show all company data: ")

    print("---------------------------")
    print("press (1) to show Orders: ")
    print("press (2) to show Products: ")
    print("press (3) to show Clients: ")
    print("press (4) to show Employees: ")
    print("press (5) to remove or add new person: ")
    print("---------------------------")

    choice = int(input("enter your choice: "))
    while choice <= 0 or choice > 5:
        print("this choice not in choices....try again!!")
        choice = int(input("enter your choice: "))
    
    if choice == 1:
        for order in data.orders:
            print("\n--------------------")
            print("order ID: " + str(order.id))
            print("Date: " + str(order.date))
            print("Is paid: " + str(order.is_paid))
            print("Client: " + str(order.person.name))
            print("Product: " + str(order.product.name))
            print("--------------------")


        print("press (1) to add new order: ")
        print("press (2) to remove order: ")
        print("press (3) to show specific order: ")

        choice = int(input("enter your choice: "))
        while choice <= 0 or choice > 3:
            print("this not in choices.....try again!!")
            choice = int(input("enter your choice: "))

        if choice == 1:
            company.add_order()
        elif choice == 2:
            company.remove_order()
        else:
            company.print_order_details()

    elif choice == 2:
        print("\n  'all products'  ")
        for pro in Data.products:
            print("\n---------------------")
            print("Product ID: " + str(pro.id))
            print("Name: " + str(pro.name))
            print("Price: " + str(pro.price))
            print("---------------------")


        print("\npress (1) to add new product: ")
        print("press (2) to remove product: ")
        print("press (3) to show specific product: ")

        choice = int(input("\nenter your choice: "))
        while choice <= 0 or choice > 3:
            print("this choice not with choices.....try again!!")
            choice = int(input("\nenter your choice: "))
        if choice == 1:
            company.add_product()
        elif choice == 2:
            company.remove_product()
        else:
            company.print_product_details()

    elif choice == 3:
        print("  'all Clients'  ")
        for client in Data.clients:
            print("\n------------------------")
            print("Client ID: " + str(client.id))
            print("Name: " + str(client.name))
            print("Phone: " + str(client.phone))
            print("Gender: " + str(client.gender))
            print("Email: " + str(client.email))
            print("------------------------")
        
        print("press (1) to show client orders: ")

        print()
        choice = int(input("enter your choice: "))
        while choice <= 0 or choice >1:
            print("this choice not with choices.....try again!!")
            choice = int(input("enter your choice: "))
        if choice == 1:
            company.print_person_orders()


    elif choice == 4:
        print("  'all Employees'  ")
        for employee in Data.employees:
            print("\n------------------------")
            print("Employee ID: " + str(employee.id))
            print("Name: " + str(employee.name))
            print("Phone: " + str(employee.phone))
            print("Gender: " + str(employee.gender))
            print("Salary: " + str(employee.salary))
            print("Working time: " + str(employee.working_time))
            print("------------------------")


    elif choice == 5:
        company.add_person()