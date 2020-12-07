from datetime import datetime

datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')


def get_date(date: str):
    date_time_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S %')


with open('files/to_cointracker.csv', 'r', newline='') as cointracker:
    with open('files/anchorusd_transactions (1).csv', 'r', newline='') as anchorcsv:
        with open("files/translated.csv", 'w+') as newFile:
            anchorRead: str = anchorcsv.readline()
            newFile.write(anchorRead)
            for row in anchorcsv:
                content = row
                print(get_date(content.replace('UTC', '')))

        newFile.close()

    anchorcsv.close()
cointracker.close()
