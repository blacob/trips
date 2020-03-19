import fileinput
import sys

class Driver:

    def __init__(self, name):
        self.name = name
        self.miles = 0
        self.time = 0
        self.avgspeed = -1

    def __repr__(self):
        if self.miles > 0:
            cleanmiles = int(round(self.miles, 0))
            cleanspeed = int(round(self.avgspeed))
            return "{}: {} miles @ {} mph".format(self.name, cleanmiles, cleanspeed)
        else:
            return "{}: 0 miles".format(self.name)

    def addTrip(self, start, end, dist):
        startHr, startMin = start.split(':')
        endHr, endMin = end.split(':')
        startHr = float(startHr)
        startMin = float(startMin)
        endHr = float(endHr)
        endMin = float(endMin)
        dist = float(dist)
        elapsed = (endHr - startHr) + (endMin - startMin) / 60
        speed = dist / elapsed
        if speed < 5 or speed > 100:
            return

        if self.avgspeed < 0:
            self.avgspeed = speed
        else:
            self.avgspeed = (self.time * self.avgspeed + elapsed * speed) / (self.time + elapsed)

        self.miles += dist
        self.time += elapsed


    def getMiles(self):
        return self.miles

    def getTime(self):
        return self.time

    def getAvgSpeed(self):
        return self.avgspeed


def main():
    lines = []
    name = sys.argv[1]
    for line in fileinput.input():
        cleaned = line.replace('\n', '')
        lines.append(cleaned)

    driverMap = {}
    for command in lines:
        tokenized = command.split()
        cmdtype = tokenized[0]
        name = tokenized[1]
        if cmdtype == 'Driver':
            freshDriver = Driver(name)
            driverMap[name] = freshDriver

        elif cmdtype == 'Trip':
            curDriver = driverMap.get(name)
            curDriver.addTrip(tokenized[2], tokenized[3], tokenized[4])

        else:
            return "Invalid Input"

    driverList = list(driverMap.values())
    driverList.sort(reverse = True, key = lambda d: d.getMiles())
    toret = ""
    f = open("output.txt", "w")
    for driver in driverList:
        print(driver)
        toret += str(driver) + "\n"
    f.write(toret)
    f.close()

if __name__== "__main__":
    main()
