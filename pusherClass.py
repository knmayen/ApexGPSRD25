class Pusher:
    def __init__(self, name, ag, w, m):
        self.name = name
        if ag == 1:
            self.ag = True
        else:
            self.ag = False

        if w == 1:
            self.w = True
        else:
            self.w = False

        if m == 1:
            self.m = True
        else:
            self.m = False
        
        self.times = {
            'hill1' : dict(),
            'hill2' : dict(),
            'Freeroll' : dict(),
            'hill3' : dict(),
            "hill4" : dict(),
            'hill5' : dict(),
        }
    
    def __repr__(self):
        return f'{self.name} pushes for {self.ag}, {self.w}, {self.m}'
    
Hannah = Pusher('hannah', 1, 1, 0)
print(Hannah)