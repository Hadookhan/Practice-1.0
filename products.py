import stock

class Products:

    basket = []

    def __init__(self, itemID):
        self.__itemID = itemID
    
    def get_item(self):
        itemID = self.__itemID
        for game in stock.games:
            if itemID == stock.games[game]:
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

class Games(Products):
    def __init__(self, itemID):
        super().__init__(itemID)
        self.stock = len(stock.games)

    def get_item(self):
        return super().get_item()
    
    def add_item(self, item):
        return super().add_item(item)
    
    def rem_item(self, item):
        return super().rem_item(item)