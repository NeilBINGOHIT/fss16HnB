import arff
import csv

class ARFFtoCSV: 
    def __init__(self, file):
        self.file = file
    
    def converter(self):
        dataset = arff.load(open(self.file, 'rb'))
        data = dataset[u'data']
        attrs = dataset[u'attributes']
        csvHead = map(lambda x: x[0], attrs)

        if isinstance(data, list):
            # remove the unicode symbols
            for i in range(len(data)):
                if isinstance(data[i][-1], unicode):
                    data[i][-1] = str(data[i][-1])
            for n, i in enumerate(csvHead):
                if isinstance(i, unicode):
                    csvHead[n] = str(csvHead[n]) 
            data.insert(0, csvHead)
        
        output = self.file[:-4]+'csv'
        with open(output,'wb') as f:
            wr = csv.writer(f, quoting=csv.QUOTE_NONE)
            wr.writerows(data)


newObj = ARFFtoCSV('data/ar1.arff')
newObj.converter()

