items = 0
total = 0
def main():
    global items, total
    num = input("Enter the number of items you have bought \nor press q to quit : ")
    if num!= 'q':
        items = items + int(num)
        print(f" Your total number of items is {items}")

        while(items!=0):
            print(f"Give the price of the {items} item\n")
            price = int(input("Here : "))

            total = total + price
            print(f"Your total price is {total}")
            items = items - 1
    else:
        print(f"Thank you for coming your total price is {total}")
main()