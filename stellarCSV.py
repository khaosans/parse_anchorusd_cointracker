import maya
import csv

def toUTCtimestamp(timestamp):
    dt = maya.parse(timestamp).datetime()
    return (dt.strftime("%Y-%m-%d %H:%M:%S"))

transaction = ['Sell', 'Buy']

def translate(Datestamp, transaction, Token, Amount, TPXLM):
    switcher: Dict[str, str] = {
        'Buy': [str(Amount), Token, str(TPXLM),'XLM','','',''],
        'Sell': [str(TPXLM),'XLM',str(Amount),Token,'','','']
    }

    return [toUTCtimestamp(Datestamp)] + switcher[transaction]


with open('stellarx-trade-history-2020-12-31T18_31_27-08_00.csv', "r", newline='') as stellarFile:
    csvreader = csv.reader(stellarFile, delimiter=',')
    next(csvreader)
    rowHeader = ['Date','Received Quantity','Received Currency','Sent Quantity','Sent Currency','Fee Amount','Fee Currency','Tag']
    with open('output.csv', 'w', newline='') as csvWritefile:
        csvwriter = csv.writer(csvWritefile, delimiter=',')
        csvwriter.writerow(rowHeader)
        for row in csvreader:                                
            output=translate(row[0], row[1], row[2], row[4], row[7])
            csvwriter.writerow(output)