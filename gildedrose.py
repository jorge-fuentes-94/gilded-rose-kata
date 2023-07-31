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
        self.initial_SellIn = SellIn
        self._item_degradation = 1

    def show_sellin(self):
        return(self.SellIn)

    def update_quality(self,days):
        if self.Quality > 0 or self.Quality < 50:
            if days < self.SellIn:
                self.Quality -=            
        elif self.Quality < 0:
            self.Quality = 0
        elif self.Quality > 50:
            self.Quality = 50


#class BrieAñejado(Item):
#    def __init__(self,Quality):super().__init__(Quality)

#    def update_quality(self, days):
#        if self.Quality < 50:
#            self.Quality +=days
#        if self.Quality > 50:
#            self.Quality = 50

#class Sulfuras(Item):
#    def __init__(self,Quality):
#        self.Quality = 80
#        super().__init__(self.Quality) 
        
#class BackstagePasses(BrieAñejado):
#    def __init__(self,Quality,SellIn):
#        self.SellIn = SellIn
#        self.object = Normal(Quality,SellIn)
#        super().__init__(Quality)
        
    
#    def show_sellin(self):
#        return self.object.show_sellin()
    
#    def UpdateQuality(self, days):
#        self.SellIn -= days
#        if self.SellIn <=10 and self.SellIn >3:
#            self.Quality += (days+2*days)
#        if self.SellIn <=3:
#            self.Quality += (days+3*days)
#        if self.SellIn <= 0:
#            self.Quality = 0
#        else:
#            super().update_quality(days)




#class ConjuredItem(Normal):
#    def __init__(self, Quality, SellIn):
#        super().__init__(Quality, SellIn)
#        self._item_degradation = 2






