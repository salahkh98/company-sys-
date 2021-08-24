from order import Order
from produc import Product
from person import Client
from person import Employee


class Data:
    employees = []
    products = []
    orders = []
    clients = []


    employee1 = Employee(1 , "ahmad" , "0569235621" , "male" , 3500 , "7 hours")
    employee2 = Employee(2 , "israa" , "0586728778" , "female" , 2000 , "7 hours")
    employee3 = Employee(3, "amer" , "0559104514" , "male" , 5000 , "7 hours")

    clint1 = Client(1 , "zain" , "0599236626" , "male" , "zain@gmail.com")
    clint2 = Client(2 , "alaa" , "055167722" , "male" , "alaa@gmail.com")
    clint3 = Client(3 , "ghada" , "0586478876" , "female" , "ghada@gmail.com")
    clint4 = Client(3 , "dina" , "05519755115" , "female" , "dina@gmail.com")


    product1 = Product(1 , "ps4" , 1499.5)
    product2 = Product(2 , "xbox one" , 1000)
    product3 = Product(3 , "headsets(JBL)" , 500)
    product4 = Product(4 , "keyboard RGB" , 300)
    product5 = Product(5 , "gaming mouse" , 160.4)



    order1 = Order(1 , "18/8/2021" , True , clint1 , product1)
    order2 = Order(2 , "17/8/2021" , False , clint2 , product2)
    order3 = Order(3 , "15/8/2021" , True , clint3 , product5)
    order4 = Order(4 , "13/8/2021" , False , clint4 , product4)
    order5 = Order(5 , "1/8/2021" , False , clint1 , product3)


    employees.append(employee1)
    employees.append(employee2)
    employees.append(employee3)

    clients.append(clint1)
    clients.append(clint2)
    clients.append(clint3)
    clients.append(clint4)


    products.append(product1)
    products.append(product2)
    products.append(product3)
    products.append(product4)
    products.append(product5)


    orders.append(order1)
    orders.append(order2)
    orders.append(order3)
    orders.append(order4)
    orders.append(order5)



