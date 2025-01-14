class Pusher:

    # allGender = set()
    # womens = set()
    # mens = set()

    def __init__(self, name, ag, w, m):
        self.name = name
        self.ag = ag
        self.w = w
        self.m = m
        
        self.times = {
            'hill1' : dict(),
            'hill2' : dict(),
            'Freeroll' : dict(),
            'hill3' : dict(),
            "hill4" : dict(),
            'hill5' : dict(),
        }

        self.bestTimes = {
            'hill1' : (None, None),
            'hill2' : (None, None),
            'Freeroll' : (None, None),
            'hill3' : (None, None),
            "hill4" : (None, None),
            'hill5' : (None, None)
        }

        self.avgTimes = {
            'hill1' : None,
            'hill2' : None,
            'Freeroll' : None,
            'hill3' : None,
            "hill4" : None,
            'hill5' : None
        }
        print(self.bestTimes, self.avgTimes)
    
    def __repr__(self):
        return f'{self.name} pushes for {self.ag}, {self.w}, {self.m}'
    
    


