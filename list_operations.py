import random

def list_operations():
    lst = []

    len_lst = int(input("Input a number to define lenght of the list: "))
    for i in range(1,len_lst + 1):
        element = random.randint(1,10)
        lst.append(element)
    print(lst)

    while True:
        operation = str(input("Input name of the opperation you want to execute or type exit to quit: "))
        if operation == 'exit':
            exit()
        if operation == 'insert':
            position = int(input("Posintion: "))
            value = int(input("Value: "))
            lst.insert(position, value)
            print(lst)
        if operation == 'print':
            print(lst)
        if operation == 'remove':
            el_rem = int(input("Element to remove: "))
            lst.remove(el_rem)
            print(lst)
        if operation == 'append':
            app = int(input("Element to append: "))
            lst.append(app)
            print(lst)
        if operation == 'sort':
            lst.sort()
            print(lst)
        if operation == 'pop':
            pop = int(input("Elepent to pop: "))
            lst.pop(pop)
            print(lst)
        if operation == 'reverse':
            lst.reverse()
            print(lst)

if __name__ == '__main__':
    list_operations()