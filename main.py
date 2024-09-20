from products import Products, Games


def new_product():
    try:
        newProduct = Products(0)
    except ValueError as v:
        print(v)
    return newProduct


def main():
    new_product()
    gameItem = Games(int(input("Enter product ID: ")))
    print(gameItem.get_item())


if __name__ == "__main__":
    main()