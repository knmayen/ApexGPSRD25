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
            'Hill1' : [],
            'Hill2' : [],
            'Freeroll' : [],
            'Hill3' : [],
            "Hill4" : [],
            'Hill5' : [],
        }
    
    def __repr__(self):
        return f'{self.name} pushes for {self.ag}, {self.w}, {self.m}'
    
Hannah = Pusher('hannah', 1, 1, 0)
print(Hannah)