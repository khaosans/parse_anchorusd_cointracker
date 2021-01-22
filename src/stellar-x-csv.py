import csv
import maya


def to_utc_timestamp(timestamp):
    dt = maya.parse(timestamp).datetime()
    return dt.strftime("%Y-%m-%d %H:%M:%S")


transaction = ['Sell', 'Buy']


def translate(datestamp, transaction1, token, amount, tp_xlm):
    switcher = {
        'Buy': [str(amount), token, str(tp_xlm), 'XLM', '', '', ''],
        'Sell': [str(tp_xlm), 'XLM', str(amount), token, '', '', '']
    }

    return [to_utc_timestamp(datestamp)] + switcher[transaction1]


def parse_csv(file_name='stellarx-trade-history-2020-12-31T18_31_27-08_00.csv'):
    with open(file_name, "r", newline='') as stellarFile:
        csv_reader = csv.reader(stellarFile, delimiter=',')
        next(csv_reader)
        row_header = ['Date', 'Received Quantity', 'Received Currency', 'Sent Quantity', 'Sent Currency', 'Fee Amount',
                     'Fee Currency', 'Tag']
        with open('output.csv', 'w', newline='') as csvWritefile:
            csvwriter = csv.writer(csvWritefile, delimiter=',')
            csvwriter.writerow(row_header)
            for row in csv_reader:
                output = translate(row[0], row[1], row[2], row[4], row[7])
                csvwriter.writerow(output)


parse_csv()
