from products import Products, Games
import stock

def show_stock():
    for items in stock.items:
        print(items)

def new_product():
    try:
        newProduct = Products(0)
        show_stock()
    except ValueError as v:
        print(v)
    return newProduct


def main():
    new_product()
    gameItem = Games(int(input("Enter product ID: ")))
    print(gameItem.get_item('games'))


if __name__ == "__main__":
    main()