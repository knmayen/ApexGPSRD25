
mashpeeCoords = {
    'Start/Hill1' : [(41.648243, -70.490599), (41.648245, -70.490457)], 
    'Hill 1/Hill2' : [(41.647737, -70.490927), (41.647587, -70.490777)],
    'Hill 2/Freeroll' : [(41.647526, -70.491502), (41.647354, -70.491443)], 
    'Freeroll/Hill 3' : [(41.648311, -70.492276), (41.648314, -70.492441)],
    'Hill 3/Hill 4' : [(41.648709, -70.492235), (41.648606, -70.492134)],
    'Hill 4/Hill 5' : [(41.648888, -70.491750), (41.648754, -70.491712)],
    'Hill 5/Finish' : [(41.648972, -70.491382), (41.648803, -70.491341)]
}

class Coords:

    def __init__(self, dict):
        self.coorsDict = dict
        self.orderedList = [key for key in self.coorsDict]
        self.getBounds()
        # create the lines
        # for key in dict:
        #     getLine(dict[key])

    def getVal(self, split, x):
        x0 = self.coorsDict[split][0][0]
        y0 = self.coorsDict[split][0][1]
        x1 = self.coorsDict[split][1][0]
        y1 = self.coorsDict[split][1][1]

        return (y1 - y0) / (x1 - x0) * (x - x0)
    
    def getBounds(self):
        # .000001 deg latitude = 1 ft
        # .000001 deg longitude = .8 ft
        # bounding box is 3ft on the extension of each line
        self.bounds = dict()
        for key in self.coorsDict:
            boxPoints = []
            dirs = [((-1, 1), (1, 1)), ((1, -1), (-1, -1))]
            deltaLat = .000003
            deltaLon = .0000038
            for i in range(len(dirs)):
                lat = self.coorsDict[key][i][0]
                lon = self.coorsDict[key][i][1]
                newLat1 = lat + deltaLat * dirs[i][0][0]
                newLon1 = lon + deltaLon * dirs[i][0][1]
                newLat2 = lat + deltaLat * dirs[i][1][0]
                newLon2 = lon + deltaLon * dirs[i][1][1]
                boxPoints.extend([(newLat1, newLon1), (newLat2, newLon2)])
            self.bounds[key] = boxPoints
        print(self.bounds)


mashpeeCoords = Coords(mashpeeCoords)
# print(mashpeeCoords)

