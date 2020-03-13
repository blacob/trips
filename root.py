import fileinput
import math

class Driver:

    def __init__(self, name):
        self.name = name
        self.miles = 0
        self.avgspeed = -1

    def __repr__(self):
        if self.miles > 0:
            return "{}: {} miles @ {} mph".format(self.name, math.floor(self.miles), math.floor(self.avgspeed))
        else:
            return "{}: 0 miles".format(self.name)

    def addTrip(self, start, end, dist):
        startHr, startMin = start.split(':')
        endHr, endMin = end.split(':')
        elapsed = (endHr - startHr) + (endMin - startMin) / 60
        speed = dist / elapsed

        if speed < 5 or speed > 100:
            return

        if self.avgspeed < 0:
            self.avgspeed = speed
        else:
            self.avgspeed = (self.miles * self.avgspeed + dist * speed) / (self.miles + dist)

        self.miles += dist




def main():
    lines = []
    for line in fileinput.input():
        cleaned = line.replace('\n', '') ## REVIEW: problem if any field is allowed to have \n
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

    driverList = driverMap.values()
    driverList.sort(reverse = True, key = lambda d: d.miles)
    for driver in driverList:
        print(driver)

if __name__== "__main__":
    main()
