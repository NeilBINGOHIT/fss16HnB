import sys

def trainer(file):
    y = 0
    n = 0
    with open(file, 'r') as f:
        for line in f.readlines():
            if line.startswith('%') or line.startswith('@') or line.startswith('\n') or line.startswith('\r'):
                continue;
            else:
                elements = line.split(',')
                
                if elements[-1].strip() == 'true':
                    y += 1
                elif elements[-1].strip() == 'false':
                    n += 1
                else:
                    continue

    if y>n :
        return '1:true'
    else :
        return '2:false'


def tester(file, trainRes):
    predRes = "\t=== Predictions on test data ===\n" + "\tinst#\tactual\tpredicted\terror prediction\n"
    i = 0
    with open(file, 'r') as f:
        for line in f.readlines():
            if line.startswith('%') or line.startswith('@') or line.startswith('\n') or line.startswith('\r'):
                continue;
            else:
                elements = line.split(',')
                if elements[-1].strip() == trainRes[2:]:
                    i += 1
                    predRes += '\t' + str(i) + '\t' + trainRes + '\t' + trainRes + '\t\t' + '1\n'
                else:
                    i += 1
                    if trainRes[0] == '1':
                        predRes += '\t' + str(i) + '\t2:' + elements[-1].strip() + '\t' + trainRes + '\t\t' + '0\n'
                    else:
                        predRes += '\t' + str(i) + '\t1:' + elements[-1].strip() + '\t' + trainRes + '\t\t' + '0\n'
    
    print predRes
    # return predRes



tester(sys.argv[2], trainer(sys.argv[1]))
