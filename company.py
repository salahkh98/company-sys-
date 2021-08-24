from data import Data
from data import Product
from data import Client
from data import Employee
from data import Order
import random

class Company:

    def add_product(self):
        
        id = int(input("enter the id: "))
        for product in Data.products:
            if product.id == id:
                print("this id already taken.....try again!!")
                return
        name = input("enter the product name: ")
        price = float(input("enter the product price: "))

        new_product = Product(id , name , price)
        Data.products.append(new_product)


    def add_person(self):
        choice = int(input("1: to add new client -------- 2: to add new employee (1 :: 2): "))
        if choice == 1:
            id = int(input("enter the id: "))
            for person in Data.clients:
                if person.id == id:
                    print("this id already taken......try again!!")
                    return
            
            name = input("enter the name: ")
            phone = input("enter the phone number: ")
            gender = input("enter the gender: ")
            email = input("enter email: ")
            
            new_client = Client(id , name , phone , gender , email)
            Data.clients.append(new_client)

        elif choice == 2:
            id = int(input("enter the id: "))
            for person in Data.employees:
                if person.id == id:
                    print("this id already taken......try again!!")
                    return
            
            name = input("enter the name: ")
            phone = input("enter the phone number: ")
            gender = input("enter the gender: ")
            salary = float(input("enter the salary: "))
            working_time = input("enter the working time: ")

            new_employeer = Employee(id , name , phone , gender , salary , working_time)

            Data.employees.append(new_employeer)

        else:
            print("this choice not in the choices....try again!!")
            return

        
    def add_order(self):
        id = int(input("enter the id: "))
        for order in Data.orders:
            if order.id == id:
                print("this id already taken.....try again!!")
                return
        date = input("enter the bill date: ")
        is_paid = bool(random.randint(0,1))

        person_bill = int(input("enter the person id: "))
        person_found = False
        for person in Data.clients:
            if person.id == person_bill:
                person_found = True
                person_bill = person
            else:
                pass
        if person_found == False:
            print("the person with id " + str(person_bill) + " not found ....... try again!!")
            return
                

        product_found = False
        product_bill = int(input("enter the product id: "))
        for pro in Data.products:
            if product_bill == pro.id:
                product_bill = pro
                product_found = True
            else:
                pass
        if not product_found:
            print("product with id" , str(product_bill) + " not found ..... try again!!")
            return
        
        new_order = Order(id , date , is_paid , person_bill , product_bill)
        Data.orders.append(new_order)


    def remove_order(self):
        id = int(input("enter the order id: "))
        for order in Data.orders:
            if order.id == id:
                Data.orders.remove(order)
                return
        print("order with id" , str(id) , "not found.....try again!!")
        


    def remove_product(self):
        id = int(input("enter the product id: "))
        for pro in Data.products:
            if pro.id == id:
                Data.products.remove(pro)
                return
        print("the product with id" , str(id) , "not found.....try again!!")
        

    def remove_person(self):
        choice = int(input("1: to remove client -------- 2: to remove employee (1 :: 2):"))
        if choice == 1:
            id = int(input("enter the person id: "))
            for person in Data.clients:
                if person.id == id:
                    Data.clients.remove(person)
                    print("done client with id " + str(id) + " removed!")
                    return
            print("the person with id" , str(id) , "not found ...... try again!!")

        elif choice == 2:
            id = int(input("enter the person id: "))
            for person in Data.employees:
                if person.id == id:
                    Data.employees.remove(person)
                    return
            print("the person with id" , str(id) , "not found ...... try again!!")


        else:
            print("this choice not in the choices....try again!!")
            return

    def print_person_info(self):
        choice = int(input("1: to show info for client -------- 2: to show info for employee (1 :: 2):"))
        if choice == 1:
            id = int(input("enter the person id: "))
            for person in Data.clients:
                if person.id == id:
                    print("\n------------------")
                    print("id: " + str(person.id))
                    print("name: " + str(person.name))
                    print("phone: " + str(person.phone))
                    print("gender: " + str(person.gender))
                    print("email: " + str(person.email))
                    print("------------------")
                    return
            print("client with id " + str(id) + " not found.....try again!!")

        elif choice == 2:
            id = int(input("enter the person id: "))
            for person in Data.employees:
                if person.id == id:
                    print("\n------------------")
                    print("id: " + str(person.id))
                    print("name: " + str(person.name))
                    print("phone: " + str(person.phone))
                    print("gender: " + str(person.gender))
                    print("salary: " + str(person.salary))
                    print("working time: " + str(person.working_time))
                    print("------------------")
                    return
            print("employee with id " + str(id) + " not found.....try again")

        else:
            print("this choice not in the choices.....try again!!")
            return


    def print_product_details(self):
        id = int(input("enter the product id: "))
        for pro in Data.products:
            if pro.id == id:
                print("\n---------------------")
                print("id: " + str(pro.id))
                print("name: " + str(pro.name))
                print("price: " + str(pro.price))
                print("------------------------")
                return
        print("the product with id " + str(id) + " not found......try again!!")
        return


    def print_order_details(self):
        id = int(input("enter the product id: "))
        for order in Data.orders:
            if order.id == id:
                print("\n---------------------")
                print("id: " + str(order.id))
                print("date: " + str(order.date))
                print("is paid: " + str(order.is_paid))
                print("client: " + str(order.person.name))
                print("product: " + str(order.product.name))
                print("------------------------")
                return
        print("the product with id " + str(id) + "not found........try again!!")
        return


    def print_person_orders(self):
        id = int(input("enter the client id: "))
        print("\n--------------------------------------")
        for client in Data.clients:
            if client.id == id:
                print("\nall orders of client " + str(client.name) +":")
                for order in Data.orders:
                    if client.name == order.person.name or client.phone == order.person.phone:
                        print("\norder id: " + str(order.id))
                        print("order date: " + str(order.date))
                        print("order paid: " + str(order.is_paid))
                        print("product: " + str(order.product.name))
                print("--------------------------------------")
                return
        print("client with id " + str(id) + " not found.....try again!!")
        
