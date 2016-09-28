import sys
import rows, Syms, Nums

class Table:
    def __init__(self, csvFile):
        self.csv = rows.csv(csvFile)
        self.cols = []
        self.rows = []
        self.headers = []

    def addRow(self):
        ##add the headers
        self.headers = self.csv.next()
        self.rows.append(self.csv.next())
        ##check the datatype of the first row
        i = 0
        for value in self.rows[0]:
            if isinstance(value, int) or isinstance(value, float):
                self.cols.append(Nums.Num())
                self.cols[i].add(value)
            else:
                self.cols.append(Syms.Sym())
                self.cols[i].add(value)
            i += 1
        ##add the following rows
        for nextRows in self.csv:
            self.rows.append(nextRows)
            i = 0
            for value in nextRows:
                self.cols[i].add(value)
                i += 1

    def printFormat(self):
        i = 0
        for col in self.cols:
            print '{:15s}'.format(self.headers[i]) + col.show()
            i += 1

    UNKNOWN = "?"
    def distance(self,r1,r2,f=2):
        d,n = 0, 10**-32
        for col in self.cols:
            x, y  = r1[col.pos], r2[col.pos]
            if x is UNKNOWN and y is UNKNOWN:
                continue
            if x is UNKNOWN: x=col.my.furthest(y)
            if y is UNKNOWN: y=col.my.furthest(x)
            n    += 1
            inc   = col.dist(x,y)**f
            d    += inc
        return (d**(1/f)) / (n**(1/f))

    

if __name__ == '__main__':
    file = 'weather.csv'
    table = Table(file)
    table.addRow()
    table.printFormat()
