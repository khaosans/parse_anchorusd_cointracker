from datetime import datetime
from typing import Dict


def get_date(time_stamp: str) -> str:
    strp_time: datetime = datetime.strptime(time_stamp, '%Y-%m-%d %H:%M:%S')
    utc_from_timestamp = datetime.fromtimestamp(strp_time.timestamp())
    return str(datetime.strptime(str(utc_from_timestamp), '%Y-%m-%d %H:%M:%S'))


transactions = ['bank_deposit', 'bank_withdrawal', 'blockchain_deposit', 'blockchain_withdrawal', 'interest_earnings',
                'trade_buy', 'trade_sell']


def translate(date: str, transaction: str, currency: str, amount: str, account: str, base_currency,
              base_amount) -> str:
    switcher: Dict[str, str] = {
        "bank_deposit": ',{0},{1},,,,'.format(amount, currency),
        'bank_withdrawal': ',{0},{1},,,,'.format(amount, currency),
        'blockchain_deposit': ',{0},{1},,,,'.format(amount, currency),
        'blockchain_withdrawal': ',{0},{1},,,,'.format(amount, currency),
        'interest_earnings': ',{0},{1},,,,'.format(amount, currency),
        'trade_buy': ',{0},{1},{2},{3},,,'.format(amount, currency, base_amount, base_currency),
        'trade_sell': ',{0},{1},{2},{3},,,'.format(base_amount, base_currency, amount, currency),
    }

    return get_date(date) + switcher[transaction] + ',{0}'.format(account)


with open('sample/cointracker_csv_import_v4 (3).csv', 'r', newline='') as cointracker:
    with open('inputs/anchorusd_transactions.csv', 'r', newline='') as anchorcsv:
        with open('output/translated.csv', 'w+') as newFile:
            anchorRead: str = anchorcsv.readline()
            output = [
                'Date,Received Quantity,Received Currency,Sent Quantity,Sent Currency,Fee Amount,Fee Currency,Tag\n']
            for row in anchorcsv:
                items = row.split(',')

                output += translate(items[0].replace(" UTC", ""), items[1], items[2], items[3], items[8], items[6],
                                    items[7])
            newFile.writelines(output)
        newFile.close()

    anchorcsv.close()
cointracker.close()
