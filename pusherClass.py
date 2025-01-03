class Pusher:

    allGender = set()
    womens = set()
    mens = set()

    def __init__(self, name, ag, w, m):
        self.name = name
        if ag == 1:
            self.ag = True
            Pusher.allGender.add(name)
        else:
            self.ag = False

        if w == 1:
            self.w = True
            Pusher.womens.add(name)
        else:
            self.w = False

        if m == 1:
            self.m = True
            Pusher.mens.add(name)
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

allPushers = dict()