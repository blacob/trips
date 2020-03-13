import fileinput

class Driver():

    def __init__(self, name):
        self.name = name
        self.miles = 0
        self.avgspeed = -1

    def __repr__(self):
        if self.miles > 0:
            return "{}: {} miles @ {} mph".format(self.name, self.miles, self.avgspeed)
        else:
            return "{}: 0 miles".format(self.name)

    def addtrip(self, dist, start, end):
        startHr, startMin = start.split(':')
        endHr, endMin = end.split(':')
        elapsed = (endHr - startHr) + (endMin - startMin) / 60
        speed = dist / elapsed

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

    print(lines)

if __name__== "__main__":
    main()
