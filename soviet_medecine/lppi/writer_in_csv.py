# encoding: utf-8
# Запись переменной в csv-файл

import csv



def smart_encode(text):
    if isinstance(text, basestring):
        text = text.encode('utf-8')
    return text

def write_in_csv(outfile, bibliorecords, years):
    first_str = [
            'number', 'title', 'local_title', 'title_data', 'organization', 'first_year',
            'place', 'additional_data', 'heading', 'period', 'source', 'editiontype'
    ]
    for year in years:
        first_str.append('price ' + year)
        first_str.append('edition ' + year)

    NODATA = None
    writer = csv.writer(outfile)

    writer.writerow(first_str)

    for brecord in bibliorecords:
        row = []
        row.append(brecord.number)
        row.append(smart_encode(brecord.title))# Есть все названия
        row.append(smart_encode(brecord.local_title)) # Все позиции заполнены
        row.append(smart_encode(brecord.title_data))
        row.append(smart_encode(brecord.organization))
        row.append(smart_encode(brecord.first_year))
        row.append(smart_encode(brecord.place))
        row.append(smart_encode(brecord.additional_data))
        row.append(smart_encode(brecord.heading))
        row.append(smart_encode(brecord.period))
        row.append(smart_encode(brecord.source))
        row.append(smart_encode(brecord.editiontype))
        for year in years:
            keys = brecord.issues.keys()
            if year in keys:
                issue = brecord.issues[year]
                if issue.price:
                    row.append(smart_encode(issue.price))
                else:
                    row.append(NODATA)
                if issue.edition:
                    row.append(smart_encode(issue.edition))
                else:
                    row.append(NODATA)
            else:
                row.append(NODATA)
                row.append(NODATA)

        writer.writerow(row)
    return outfile
