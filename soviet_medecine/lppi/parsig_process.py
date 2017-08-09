# encoding: utf-8
%load_ext autoreload
%autoreload 2
%pwd
%cd /home/asya/repo/soviet_medecine/lppi

import coverage
import test_parse_issues
from parser_lppi import parse
from writer_in_csv import write_in_csv
from tests_wtcsv import write_in_csv
from parser_lppi import parse_blocks

! coverage erase
! coverage run test_parse_issues.py

coverage.stop()
! coverage report
! coverage html


editiontype = u'журнал'
start_block_id = 1631
source = u'Летопись печатных и периодических изданий СССР. 1950 - 1955'
years = ('1950', '1951', '1952', '1953', '1954')
txt_path = 'text_files/lppi_1950_1954/lppi_1950_1954_all/lppi_1950_1954_all.txt'

a = parse(txt_path, start_block_id, source, editiontype, years)
for brecord in a:
    #print brecord.number, brecord.title
    #print brecord.number, brecord.local_title
    #print brecord.number, brecord.title_data
    #print brecord.number, brecord.organization
    #print brecord.number, brecord.first_year
    #print brecord.number, brecord.place
    #print brecord.number, brecord.additional_data
    #print brecord.number, brecord.heading
    #print brecord.number, brecord.period
    print brecord.number, u''.join([u'{0}: {1.price}, {1.edition} '.format(year, issue) for year, issue in brecord.issues.items()])
    print '---'
    #print brecord.number, brecord.source
    print brecord.number, brecord.editiontype

parsed_path = 'parsed/lppi_1950_1954/lppi_1950_1954_all/lppi_1950_1954_all.csv'
outfile = open(parsed_path, 'w')
write_in_csv(outfile, a, years)
outfile.close()


print u'\u0442. 2'

'''2685.	Научные труды (Иркут, гос. мед. ин-т). Иркутск.
    Вып. 129 1976. 600 экз. 1р.; вып. 131 © 1976. 500 экз. 80 к.; вып. 132 1976.
     700 экз. 1 р. 20 к.; вып. 137 1977. 600 экз. 60 к.; вып. 138
     ((Вопросы неотложной абдоминальной и сосудистой хирургии вып. 2)
      1977. 600 экз. 90 к.; вып. 139 1977. 800 экз. 1 р. 90 к.; вып. 140 1977. 500 экз. 60 к.
      Вып. 12® ч. 1 — 1975.'''

'''2099. Сборник трудов (Тбил. гос. мед. нн-т). Тбилиси. — Рез. на груз. яз.
Загл. также на груз, яз.: Шромата кре-були.
Т. 26 1976. 5 р. 35 к.; т. 27 1977. 7 р. 36 к. — 500 экз.
Т. 25 — 1974 (Труды).'''


'''2702.	Труды Воронежского государственного медицинского института. Воронеж. (Воронеж, отд-ние Всесоюз. о-ва анатомов, гистологов и эмбриолого®).
Т. 96 1976. 600 экз.; т. 97 © 1976. 1.000 экз. — Ц. 60 к.
Т. 95 — 1975.'''

''' 2701.	Труды (В'олгогр. гос. мед. ин-т). Волгоград.
Т. 27 вып. 5 © 1977. 500 экз. 43 к.; т. 29
вып. 1 © 1977. 1.000 экз. 45 к.; т. 29 вып. 3 1976. 500 экз. Б. ц.; т. 30 вып. 3 1977. 800
экз. 127 вып 4, т. 128 вып. 2 — 1975.'''

'''643.	Азербайджанский медицинский журнал (Азэрбачан тибб журналы). Баку. (М-во здравоохранения АзССР). © с )№ 7
1973.	— На азерб. и рус. яз.
Изд. с 1925. — Ежемес.
1971. 9.175 — 9.290 экз.; 1972. 9.030 — 9 400 экз.; 1973. 9.580 — 9.780 экз.; 1974. 9.220 — 9.600 экз.; 1975. 9.130 — 9.300 экз.
—	Ц. 30 к. — С указ, к каждому году.'''


def debug_parse_blocks():
    data = open(txt_path).read().decode('utf-8')
    exp = parse_blocks(data, start_block_id)

    for e in exp:
        print e['number']
        #print e['editiontype']
        print e['text'][:1024]
        print '---'

debug_parse_blocks()
