import math

mashpeeCoords = {
    'Start/hill1' : [(41.648241, -70.49048), (41.648250, -70.490588)], 
    'hill1/hill2' : [(41.648029, -70.490570), (41.648043, -70.490652)],
    'hill2/Freeroll' : [(41.647669, -70.490903), (41.647608, -70.490860)], 
    'Freeroll/hill3' : [(41.647983, -70.492365), (41.647993, -70.492280)],
    'hill3/hill4' : [(41.648451, -70.492420), (41.648439, -70.492324)],
    'hill4/hill5' : [(41.648809, -70.491978), (41.648749, -70.491954)],
    'hill5/Finish' : [(41.648943, -70.491339), (41.648863, -70.491305)]
}

class Coords:

    def __init__(self, dict):
        self.coordsDict = dict
        self.orderedList = [key for key in self.coordsDict]

    # get the value of the lon when given the split line and lat
    def getVal(self, split, x):
        x0 = self.coordsDict[split][0][0]
        y0 = self.coordsDict[split][0][1]
        x1 = self.coordsDict[split][1][0]
        y1 = self.coordsDict[split][1][1]
        print(split)
        return (y1 - y0) / (x1 - x0) * (x - x0) + y0
    
    @staticmethod
    def getDist(point0, point1):
        x0 = point0[0]
        y0 = point0[1]
        x1 = point1[0]
        y1 = point1[1]
        return math.sqrt((x0-x1) ** 2 + (y0-y1) ** 2) 

    # distance from the split line to the point
    def getDoubleDist(self, lat, lon, split):
        point1 = self.coordsDict[split][0]
        point2 = self.coordsDict[split][1]

        #1st point
        point1Dist = self.getDist(point1, (lat, lon))
    
        #2nd point
        point2Dist = self.getDist(point2, (lat, lon))

        return point1Dist, point2Dist

mashpeeCoords = Coords(mashpeeCoords)
# print(mashpeeCoords)