class Item ():
    def __init__(self, Quality):
        self.initial_quality = Quality
        self.Quality = Quality
        
    def show_quality(self):
        return(self.Quality)
    
    def show_initial_quality(self):
        return(self.initial_quality)
    
    def reset_quality(self):
        self.Quality = self.initial_quality

    
class Normal(Item):
    def __init__(self,Quality,SellIn):
        super().__init__(Quality)
        self.SellIn = SellIn
        self._item_degradation = 1

    def show_sellin(self):
        return(self.SellIn)

    def update_quality(self,days):
        if self.Quality > 0 or self.Quality < 50:
            if days < self.SellIn:
                self.Quality -= days * self._item_degradation
            else:
                self.Quality -= self.SellIn * self._item_degradation + self._item_degradation * 2 * (days - self.SellIn)
        self.quality_limit()          

    def quality_limit(self):
        if self.Quality < 0:
            self.Quality = 0
        elif self.Quality > 50:
            self.Quality = 50
        


class BrieAñejado(Item):
    def __init__(self,Quality):super().__init__(Quality)

    def update_quality(self, days):
        if self.Quality < 50:
            self.Quality +=days
        if self.Quality > 50:
            self.Quality = 50

class Sulfuras(Item):
    def __init__(self,Quality):
        self.Quality = 80
        super().__init__(self.Quality) 
        

class ConjuredItem(Normal):
    def __init__(self, Quality, SellIn):
        super().__init__(Quality, SellIn)
        self._item_degradation = 2
        
class BackstagePasses(Item):
    def __init__(self,Quality,SellIn):
        self.initial_quality = Quality
        self.Quality = Quality
        self.SellIn = SellIn
            
    def show_sellin(self):
        return self.object.show_sellIn()
    
    def update_quality(self, days):
        if self.SellIn - days <= 10 and self.SellIn - days > 3:
            self.Quality +=2
        elif self.SellIn - days <= 3 and self.SellIn - days > 0:
            self.Quality +=5
        elif self.SellIn - days < 0:
            self.Quality = 0
            






