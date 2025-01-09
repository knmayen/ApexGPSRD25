class Pusher:

    # allGender = set()
    # womens = set()
    # mens = set()

    def __init__(self, name, ag, w, m):
        self.name = name
        if ag == 1:
            self.ag = 1
        else:
            self.ag = 0

        if w == 1:
            self.w = 1
        else:
            self.w = 0

        if m == 1:
            self.m = 1
        else:
            self.m = 0
        
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
