import stock

class Products:

    basket = []

    def __init__(self, itemID):
        self.__itemID = itemID
    
    def get_item(self,item_type):
        itemID = self.__itemID
        for game in stock.items[item_type]:
            if itemID == stock.items[item_type][game]:
                return game
        raise Exception("Please specify a game ID")
    
    def add_item(self,item):
        basket = Products.basket
        if item in basket:
            raise Exception("This item is already in your basket")
        basket.append(item)

    def rem_item(self,item):
        basket = Products.basket
        if item in basket:
            basket.remove(item)
        else:
            raise Exception("This item is not in your basket")
    
    def clear_basket(self):
        return Products.basket.clear()
    
    def show_products(self):
        itemList = {}
        for item in stock.items:
            itemList[item] = stock.items[item]
        return itemList

class Games(Products):
    def __init__(self, itemID):
        super().__init__(itemID)
        self.stock = len(stock.items['games'])

    def get_item(self,item_type):
        for items in stock.items:
            if items == 'games':
                item_type = items
                return super().get_item(item_type)
    
    def add_item(self, item):
        return super().add_item(item)
    
    def rem_item(self, item):
        return super().rem_item(item)