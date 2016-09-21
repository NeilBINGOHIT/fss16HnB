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
        ##check first data row
        i = 0
        for value in self.rows[0]:
            if isinstance(value, int) or isinstance(value, float):
                self.cols.append(Nums.Num())
                self.cols[i].add(value)
            else:
                self.cols.append(Syms.Sym())
                self.cols[i].add(value)
            i += 1
        
        for nextRows in self.csv:
            self.rows.append(nextRows)
            i = 0
            for value in nextRows:
                self.cols[i].add(value)
                i += 1
        

    # def printFormat(self):
    #     for col in self.cols:
    #         # print self.headers
    #         col.show()





if __name__ == '__main__':
    file = 'weather.csv'
    table = Table(file)
    table.addRow()
    table.printFormat()
