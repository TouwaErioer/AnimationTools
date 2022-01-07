class Ass(object):

    def __init__(self, line: str):
        res = line.split(",")
        self.layer = res[0]
        self.start = res[1]
        self.end = res[2]
        self.style = res[3]
        self.actor = res[4]
        self.margin_l = res[5]
        self.margin_r = res[6]
        self.margin_v = res[7]
        self.effect = res[8]
        index = line.find(res[9])
        self.text = line[index:]

    def toText(self):
        return ','.join(list(vars(self).values()))

    def setStart(self, start):
        self.start = start

    def setEnd(self, end):
        self.end = end

    def setText(self, text):
        self.text = text
