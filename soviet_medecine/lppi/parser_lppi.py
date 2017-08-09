# encoding: utf-8
import attr

@attr.s
class Issue(object):
    edition = attr.ib(default=None)
    price = attr.ib(default=None)

    @property
    def str_edition(self):
        return '{0:.0f}'.format(self.edition)

    @property
    def str_price(self):
        return '{0:.2f}'.format(self.price)

@attr.s
class BiblioRecord(object):
    number = attr.ib(default=None)
    title = attr.ib(default=None)
    local_title = attr.ib(default=None)
    title_data = attr.ib(default=None)
    organization = attr.ib(default=None)
    first_year = attr.ib(default=None)
    place = attr.ib(default=None)
    additional_data = attr.ib(default=None)
    heading = attr.ib(default=None)
    #price = attr.ib(default=None)
    period = attr.ib(default=None)
    #edition = attr.ib(default=None)
    source = attr.ib(default=None)
    editiontype = attr.ib(default=None)
    issues = attr.ib(default=None)

    def __repr__(self):
        return 'BiblioRecord("{}")'.format(self.title.encode('utf-8'))


import re
from decimal import *
import math

BRECORDTYPE1 = ur'[0-9]+\.[^/]*/[^—]*—'
RE_BRECORDTYPE1 = re.compile(BRECORDTYPE1)

IZD_S = ur'[и|И]зд\.?[ \n\t]?с[ \n\t]?[а-я]*[ \n\t\.]?(?P<first_year>1[0-9][0-9][0-9])'
RE_IZD_S = re.compile(IZD_S)

PERIOD_STR = (
    ur'(?P<monthly>(Еже|еже|еже-|Еже-|Двух|Двух-|двух|двух-)мес)|(?P<trimestrial>((Еже|еже|)кварт)|Кварт)|'
    ur'(?P<irregular>(8 раз в год)|(2 раза в год)|(3 раза в год)|([1]* раз в год)|(2 раза в мес.))'
    )
PERIOD_REG = re.compile(PERIOD_STR)

YEAR_P = ur'(?P<year>(19[0-9][0-9] ?— ?19[0-9][0-9])|(19[0-9][0-9]))'
PRICE_P1 = ur'(([0-9]? ?[рк]?\.? ?[0-9]+ ?[рк]*[\.,]?)+ ?[—] ?([0-9]* *[рк]*\.? *[0-9]+ ?[рк][\.,]*)+ ?)'
PRICE_P2 = ur'([0-9]* *[рк]*\.? *[0-9]+ ?[рк][\.,]*))'
PRICE_P3 = ur'(Б\.[ \t\n]?ц\.)'
PRICE_P = ur'(?P<price>(' + PRICE_P1 + ur'|' + PRICE_P2 + '|' + PRICE_P3 + ur')'
EDITION_P = ur'(?P<edition>[0-9]*\.?[0-9]*\.?[0-9]+[ \t\n]?[—-]?[ \n\t]?[0-9]*\.?[0-9]*\.?[0-9]+[ \t\n]?экз\.)'

YEAR_ED = (
    YEAR_P + ur'[\.,-]?[ \t\n]?'
    u'(' + PRICE_P + '[ \t\n]*' + ur'|' + EDITION_P + '[ \t\n]*' + ')+'
)
RE_YEAR_ED = re.compile(YEAR_ED)
ISSN_ED = (
    ur'(?P<issn>ИССН[ \t\n]?[0-9]*[ \t\n]?[—-][ \t\n]?[0-9]*Х?[ \t\n\]\.,:]*) ?'
    ur'(?P<edition>[0-9]*\.?[0-9]*\.?[0-9]*[ \t\n]?[—-]?[ \n\t]?[0-9]*\.?[0-9]*\.?[0-9]+[\t\n ]?экз\.)'
    )
RE_ISSN_ED = re.compile(ISSN_ED)

ED = ur'(?P<edition>([0-9]*\.?[0-9]*\.?[0-9]*[ \t\n]?[—-]?[ \n\t]?[0-9]*\.?[0-9]*\.?[0-9]+[\t ]?экз\.))'
RE_ED = re.compile(ED)

BEG_YEAR_OF_BOOK = 1986

YEAR_INTERVAL = ur'(?P<years>19[0-9][0-9][ \t\n]?—[ \t\n]?19[0-9][0-9])[\.,-]?[ \t\n]*'
RE_Y_I = re.compile(YEAR_INTERVAL)


YEAR_STR = ur'1[7-9][0-9][0-9]'
RE_YEAR = re.compile(YEAR_STR)

YEAR_PRICE = (
    ur'(?P<year>19[0-9][0-9])[ \t\n.,]*'
    ur'(?P<price>[0-9]+[ \t\n]*[рк]*[\.]*[ \t\n]?[0-9]*[ \t\n]*[рк][\.,]?)'
    )
RE_YEAR_PRICE = re.compile(YEAR_PRICE)
ISSN_PRICE = (
    ur'(?P<issn>ИССН[ \t\n]?[0-9]*[ \t\n]?[—-][ \t\n]?[0-9]*Х?[ \t\n\.,:]?) ?'
    ur'(?P<price>[0-9]+[ \t\n]*[рк]*[\.]?[ \t\n]?[0-9]*[ \t\n]*[рк][\.,]?)'
    )
RE_ISSN_PRICE = re.compile(ISSN_PRICE)
PRICE_STR = ur'(?P<price>[0-9]+[ \t\n]*[рк]*[\.]*[ \t\n]?[0-9]*[ \t\n]*[рк][\.,]?)'
RE_PRICE = re.compile(PRICE_STR)

VYP = (
    ur'(?P<vypusk>(([Вв]ып)|([Тт]))[\.,][ \t\n]*[0-9]*[\.,])[ \t\n]*'
    ur'(?P<year>19[0-9][0-9])[ \t\n.,;]*'
    )
RE_VYP = re.compile(VYP)
VYP_ED = (
    ur'\((?P<vypusk>(([Вв]ып)|[Тт])[\.,][ \t\n]*[0-9]*[\.,]?[ \t\n])'
    ur'(?P<edition>[0-9]*\.?[0-9]*\.?[0-9]*[ \t\n]?[—-]?[ \n\t]?[0-9]*\.?[0-9]*\.?[0-9]+[\t\n ]?экз\.)\)'
    )
RE_VYP_ED = re.compile(VYP_ED)
VYP_PRICE = (
    ur'\((?P<vypusk>(([Вв]ып)|[Тт])[\.,][ \t\n]*[0-9]*[\.,]?[ \t\n])'
    ur'(?P<price>[0-9]+[ \t\n]*[рк]*[\.]*[ \t\n]?[0-9]*[ \t\n]*[рк][\.,]?)'
    )
RE_VYP_PRICE = re.compile(VYP_PRICE)
Y_PRICE_VAR = (
    ur'\((?P<year>(19[0-9][0-9] — 19[0-9][0-9])|(19[0-9][0-9]))[\.,-]?[ \t\n]*'
    ur'(?P<price>[0-9]+[ \t\n]*[рк]*[\.]*[ \t\n]?[0-9]*[ \t\n]*[рк][\.,]?)\)'
    )
RE_Y_PRICE_VAR = re.compile(Y_PRICE_VAR)

RUB = ur'(?P<rub>[0-9]*)[ \t\n]*р[., \t\n]*'
KOP = ur'(?P<kop>[0-9][0-9])[ \t\n]*к[., \t\n]*'
RE_RUB = re.compile(RUB)
RE_KOP = re.compile(KOP)

BESPL = ur'(?P<bespl>([Б|б]еспл)|([Б|б][.,][ \t\n]?ц)[.,][ \t\n]?)'
RE_BESPL = re.compile(BESPL)

NODATA = None
PARCIGLACUNA = None

ENDOFBLOCK = ur'.*(?P<sm>См\.[ \t]?(?P<block_id>[0-9]*)\.?$)'
RE_ENDOFBLOCK = re.compile(ENDOFBLOCK)

CENA_TYPE2 = (
    ur'([ \t\n]*—?[ \t\n]*Ц\.[ \t\n]*)'
    ur'(?P<price>[0-9]+[ \t\n]*[рк]*[\.]*[ \t\n]?[0-9]*[ \t\n]*[рк][\.,]?)'
    )
RE_CENA_TYPE2 = re.compile(CENA_TYPE2)

ED_TYPE2 = (
    ur'19[0-9][0-9][,\.]?[ \t\n]*'
    ur'(?P<price>[0-9]?[ \t\n]*[рк]?[,\.]?[ \t\n]*[0-9]+[ \t\n]*[рк]+[\.,])?[ \t\n]*'
    ur'(?P<edition>[—\-][ \n\t]?[0-9]*\.?[0-9]+[ \t\n]?экз\.[ \t\n]*)'
    )
RE_ED_TYPE2 = re.compile(ED_TYPE2)

ED_PRICE_T3 = (
    ur'(?P<edition>[ \n\t]?[0-9]*\.?[0-9]+[ \t\n]?экз[\.,][ \t\n]*)?'
    ur'(?P<price>[0-9]?[ \t\n]*[рк]?[,\.]?[ \t\n]*[0-9]+[ \t\n]*[рк]+[\.,])'
    )
RE_ED_PRICE_T3 = re.compile(ED_PRICE_T3)

JUR_TYPE = u"ЖУРНАЛЫ"
SBR_TYPE = u"ТРУДЫ"
BUL_TYPE = u"БЮЛЛЕТЕНИ"

NAZV_ORG = ur'((Известия)|(Доклады)|(Сборник (научных)? ((работ)|(трудов)))|([т|Т]руды)|(Ученые записки)|(Научные работы студентов))[ \t\n](?P<organization>[а-я А-я№0-9,\-—\t\n]+)\.'
RE_NAZV_ORG = re.compile(NAZV_ORG)

START_VYP = ur'((((Вып)|([т|Т])|([с|С]б))\.)|(№))[ \t\n\[]*1[— \.\]]*(?P<year>19[0-9][0-9])'
RE_START_VYP = re.compile(START_VYP)

def clean_str(text):
    text = text.replace('\n', '').strip()
    text = text.replace('\t', '').strip()
    return text


def parse_blocks(data, block_id):
    blocks = []
    buff = []
    editiontype = NODATA

    for line in data.split('\n'):
        line = line.strip()
        smmatch = RE_ENDOFBLOCK.match(line)

        if (line.strip().startswith(str(block_id)) or smmatch) and buff:
            blocks.append({'text': '\n'.join(buff), 'number': block_id - 1})
            block_id += 1
            buff = []
        if smmatch:
            blocks.append({'text': smmatch.group('block_id') + '.' + line, 'number': smmatch.group('block_id')})
            buff = []
        elif (line == JUR_TYPE) or (line == SBR_TYPE) or (line == BUL_TYPE):
            editiontype = line
            blocks.append({'text': '\n'.join(buff), 'number': block_id - 1})
            block_id += 1
            buff = []
            blocks.append({'text': line, 'number': None, 'editiontype': editiontype})
        else:
            buff.append(line)

    # обработка буфер для последнего блока
    blocks.append({'text': '\n'.join(buff), 'number': block_id - 1})


    return blocks

def parse_period(block):
    m = PERIOD_REG.search(clean_str(block['text']))
    if m:
        period = max(m.group(u'monthly'), m.group('trimestrial'), m.group('irregular'))
    else:
        period = NODATA
    return period

def parse_firstyear(block, dashpos, second_dashpos):
    first_year = RE_YEAR.search(block['text'][dashpos + 1:second_dashpos])
    if first_year:
        return first_year.group(0)
    else:
        return NODATA

def float_data(text):
    if text == '':
        data = 0
    else:
        data = float(text)
    return data

def edition_mean(edition, text_block):
    #return 767676.0
    edition = edition.replace('-', u'—')
    dashedition = edition.find(u'—')
    if (dashedition > 1) and (not RE_ED_TYPE2.search(text_block)):
        edition = edition.replace(u'экз.', '').strip()
        edition = edition.replace(' ', '')
        edition = edition.replace('.', '')
        edition = edition.split(u'—')
        edition1 = clean_str(edition[0].replace(u'—', ''))
        edition2 = clean_str(edition[1].replace(u'—', ''))
        edition = round((float_data(edition1.replace('.', '').strip()) + float_data(edition2.replace('.', '').strip())) / 2)
    else:
        edition = edition.replace(u'экз.', '').strip()
        edition = edition.replace(' ', '')
        edition = edition.replace('.', '')
        edition = edition.replace(',', '')
        #print edition
        edition = clean_str(edition.replace(u'—', ''))
        edition = edition_float(edition)
    return edition

def edition_float(edition):
    edition = edition.replace(u'экз.', '').strip()
    edition = edition.replace(' ', '')
    edition = edition.replace('.', '')
    #print edition
    edition = clean_str(edition.replace(u'—', ''))
    edition = float(edition)
    return edition


def price_float(price):
    #print price
    #print RE_RUB.search(price)
    if RE_RUB.search(price):
        rub = RE_RUB.search(price).group('rub')
    else:
        rub = 0
    if RE_KOP.search(price):
        kop = RE_KOP.search(price).group('kop')
    else:
        kop = 0
    #print 'рубли:', rub, 'копейки:', kop
    price = (float(rub) * 100) + float(kop)
    price = round(price)
    return price

def price_mean(price):
    if price:
        dashprice = price.find(u'—')
        if dashprice > 0:
            price = price.split(u'—')
            if not RE_RUB.search(price[0]) and not RE_KOP.search(price[0]):
                price2 = price[1].strip()
                price1 = (price[0].strip(), price2[-3:])
                price1 = ''.join(price1)
                price = (price_float(price1) + price_float(price2)) / 2
            else:
                price1 = price[0].strip()
                price2 = price[1].strip()
                price = (price_float(price1) + price_float(price2)) / 2
        elif price == u'Б. ц.':
            price = 0
        else:
            price = price_float(price)
    return price

def year_interval(year):
    year = year.split(u'—')
    i = int(year[0])
    years_list = []
    while i <= int(year[-1]):
        years_list.append(str(i))
        i = i + 1
    return years_list

def average_for_year(text_block, year):
    sumed, sumpr, lened, lenpr = 0, 0, 0, 0
    for exem in RE_YEAR_ED.finditer(text_block):
        for curr_year in year_interval(exem.group('year')):
            if curr_year == year:
                if exem.group('price'):
                    pr = price_mean(exem.group('price'))
                    sumpr += pr
                    lenpr += 1
                if exem.group('edition'):
                    ed = edition_mean(exem.group('edition'), text_block)
                    sumed += ed
                    lened += 1
    return sumed, sumpr, lened, lenpr


def parse_issues(block, years, editiontype):
    issn = block['text'].find(u'ИССН')
    if block['text'].endswith('.'):
        text_block = clean_str(block['text'])
    else:
        point = block['text'].rfind('.\n')
        text_block = clean_str(block['text'][:point + 3])
    issues = {}
    issn_ed = RE_ISSN_ED.search(text_block)
    if issn_ed:
        issn_ed = issn_ed.group('edition')
    issn_price = RE_ISSN_PRICE.search(text_block)
    if issn_price:
        issn_price = issn_price.group('price')
    price_re = RE_PRICE.search(text_block)
    if price_re:
        price_re = price_re.group('price')
    vyp_year = {}
    for item in RE_VYP.finditer(text_block):
        vypusk = clean_str(item.group('vypusk').lower())
        vyp_year[vypusk] = item.group('year')
    edit = RE_ED.search(text_block)
    if edit:
        edit = edit.group('edition')
    vyp_ed = {}
    for item in RE_VYP_ED.finditer(text_block):
        vypusk = clean_str(item.group('vypusk').lower())
        vyp_ed[vypusk] = item.group('edition')
    #print block['number'], vyp_ed
    vyp_price = {}
    for item in RE_VYP_PRICE.finditer(text_block):
        vypusk = clean_str(item.group('vypusk').lower())
        vyp_price[vypusk] = item.group('price')
    #print block['number'], vyp_price
    issn_block = text_block[issn:]
    y_i_find = RE_Y_I.search(issn_block)
    y_price_var = RE_Y_PRICE_VAR.search(text_block)
    bespl = RE_BESPL.search(text_block)
    cena_type2 = RE_CENA_TYPE2.search(text_block)
    ed_type2 = RE_ED_TYPE2.search(text_block)
    type3 = RE_ED_PRICE_T3.search(text_block)
    #print '<<<'
    #print block['number']
    #print '---'
    #print block['text']

    for item in RE_YEAR_ED.finditer(text_block):
        #print block['number'], item.group('year')
        for year in year_interval(item.group('year')):
            if year in years:
                #print block['number'], item.group('price')
                sumed, sumpr, lened, lenpr = average_for_year(text_block, year)
                #if block['number'] == 2781:
                    #print sumed, sumpr, lened, lenpr
                if lened == 0:
                    edition = None
                else:
                    edition = round(sumed / lened) # Пиздец, все. не могу ничо
                if lenpr == 0:
                    price = None
                else:
                    price = round(sumpr / lenpr)
                #print edition, price
                issues[year] = Issue(edition=edition, price=price)
                 # 3

    for item in RE_YEAR_PRICE.finditer(text_block):
        year = clean_str(item.group('year'))
        price = clean_str(item.group('price'))
        if year in years:
            if year in issues:
                if not issues[year].price:
                    issues[year].price = price
            else:
                issues[year] = Issue(price=price)
    #print edition, price
    for year in issues:
        if year in years:
            if not issues[year].edition:
                issues[year].edition = issn_ed
            if not issues[year].edition:
                issues[year].edition = edit
            if not issues[year].price:
                issues[year].price = issn_price
            if not issues[year].price:
                issues[year].price = price_re

    if not issues:
        for item in vyp_year.values():
            year = item
            if year in years:
                issues[year] = Issue(price=issn_price, edition=edit)
                if not issues[year].price:
                    issues[year].price = price_re
    if vyp_ed:
        #print block['number']
        for vyp, ed in vyp_ed.items():
            year = vyp_year[vyp]
            if year in years:
                issues[year].edition = ed

    if vyp_price:
        #print block['number']
        for vyp, price in vyp_price.items():
            year = vyp_year[vyp]
            if year in years:
                issues[year].price = price

    if y_i_find:
        y_i = y_i_find.group('years').split(u'—')
        i = int(y_i[0]) - 1
        years_list = []
        while i < int(y_i[-1]):
            i = i + 1
            years_list.append(str(i))
        for year in years_list:
            if year in years:
                if year not in issues:
                    issues[year] = Issue()
                if not issues[year].price:
                    issues[year].price = issn_price
                if not issues[year].edition:
                    issues[year].edition = edit
    if y_price_var:
        for item in RE_Y_PRICE_VAR.finditer(text_block):
            for year in year_interval(item.group('year')):
                price = item.group('price')
                if year in years:
                    if not issues[year].price:
                        issues[year].price = price

    if (not RE_BRECORDTYPE1.search(block['text'])):
        if not issues:
            for year in years:
                issues[year] = Issue(edition=0, price=0)
        if cena_type2:
            for year in issues.keys():
                price = cena_type2.group('price')
                price = price_float(price)
                issues[year].price = price
        if ed_type2:
            for year in issues.keys():
                edition = ed_type2.group('edition')
                edition = edition_mean(edition, text_block)
                issues[year].edition = edition
        for year in years:
            if (editiontype == JUR_TYPE) and (not issues[year].price) and (not issues[year].edition):
                #print text_block
                price = type3.group('price')
                price = price_float(price)
                issues[year].price = price
                if type3.group('edition'):
                    edition = type3.group('edition')
                    edition = edition_mean(edition, text_block)
                    issues[year].edition = edition


    #print edition, price
    for year in issues.keys():
        if isinstance(issues[year].edition, basestring):
            ed = edition_mean(issues[year].edition, text_block)
            issues[year].edition = ed
        if isinstance(issues[year].price, basestring):
            pr = price_mean(issues[year].price)
            issues[year].price = pr

    if bespl:
        for year in issues.keys():
            if not issues[year].price:
                price = 0
                issues[year].price = price

    return issues


def parse_data_block(block, heading, source, editiontype, years):
    brecord = BiblioRecord()
    title_start = len(str(block['number'])) + 1
    smmatch = RE_ENDOFBLOCK.match(block['text'])
    dashpos = block['text'].find(u'—')
    issn = block['text'].find(u'ИССН')
    slash = block['text'].find(u'/')
    #print block['number']
    brecord.editiontype = editiontype

    if smmatch:
        if slash > - 1:
            brecord.title = clean_str(block ['text'][title_start:dashpos - 2])
        else:
            first_point = block['text'].find('.', title_start)
            brecord.title = clean_str(block['text'][title_start:first_point])
        brecord.local_title = smmatch.group('sm')
        brecord.title_data = smmatch.group('sm')
        brecord.organization = smmatch.group('sm')
        brecord.first_year = smmatch.group('sm')
        brecord.place = smmatch.group('sm')
        brecord.additional_data = smmatch.group('sm')
        #brecord.price = smmatch.group('sm')
        brecord.period = smmatch.group('sm')
        #brecord.edition = {}
        brecord.issues = {}

    if RE_BRECORDTYPE1.search(block['text']):
        colonpos = block['text'].find(':')
        slashpos = block['text'].find('/')
        second_dashpos = block['text'].find(u'—', dashpos + 1)
        third_dashpos = block['text'].find(u'—', second_dashpos + 1)
        comma = block['text'].find(',', third_dashpos)
        enddatapos = slashpos if slashpos != -1 else dashpos
        second_colonpos = block['text'].find(':', issn)
        numberpos = block['text'].find(u'№', second_colonpos)
        journ = block['text'].find(u'журн.')

        brecord.title = clean_str(block['text'][title_start: min(filter(lambda x:x>0, (colonpos, dashpos, slashpos)))])
        titles = brecord.title.split('=')
        if len(titles) > 1:
            brecord.local_title = clean_str(titles[1])
            brecord.title = clean_str(titles[0])
        else:
            brecord.local_title = NODATA

        brecord.title_data = clean_str(block['text'][colonpos + 1:enddatapos])
        if len(brecord.title_data) < 1:
            brecord.title_data = NODATA
        brecord.organization = clean_str(block['text'][slashpos:dashpos])
        if len(brecord.organization) == 0:
            brecord.organization = clean_str(block['text'][journ + 5:dashpos])
        if len(brecord.organization) == 0:
            brecord.organization = PARCIGLACUNA

        brecord.first_year = parse_firstyear(block, dashpos, second_dashpos)
        brecord.place = clean_str(block['text'][third_dashpos:comma])
        brecord.additional_data = clean_str(block['text'][comma + 1:issn])
        brecord.issues = parse_issues(block, years)

    if (not RE_BRECORDTYPE1.search(block['text'])) & (not smmatch):
        first_point = block['text'].find('.', title_start)
        first_bracket = block['text'].find(u'(')
        second_bracket = block['text'].find(u')', first_bracket)
        organ = block['text'].find(u'Орган ')
        izd = block['text'].find(u'Изд. ')
        nazv_org = RE_NAZV_ORG.search(block['text'])

        brecord.title = clean_str(block['text'][title_start:first_point])
        fb_title = brecord.title.find(u'(')
        sb_title = brecord.title.find(u')')
        if fb_title > -1:
            brecord.local_title = brecord.title[fb_title + 1:sb_title]
            brecord.title = brecord.title[:fb_title]
            first_bracket = block['text'].find(u'(', sb_title)
            second_bracket = block['text'].find(u')', first_bracket)
        else:
            brecord.local_title = NODATA
        brecord.title_data = NODATA
        if first_bracket > - 1:
            brecord.organization = clean_str(block['text'][first_bracket + 1:second_bracket])
        elif nazv_org:
            brecord.organization = nazv_org.group('organization')
        if organ > - 1:
            brecord.organization = clean_str(block['text'][organ:izd])

        izd_s_year = RE_IZD_S.search(block['text'])
        start_vyp = RE_START_VYP.search(block['text'])
        if izd_s_year:
            brecord.first_year = izd_s_year.group('first_year')
        elif start_vyp:
            brecord.first_year = start_vyp.group('year')
        else:
            brecord.first_year = NODATA
        brecord.place = NODATA #временная мера. Потом буду парсить по-другому
        brecord.additional_data = NODATA
        brecord.issues = parse_issues(block, years, editiontype)


    brecord.number = block['number']
    brecord.heading = heading
    #brecord.price = clean_str(parse_price(block))
    brecord.period = parse_period(block)
    #brecord.edition = parse_edition(block)
    brecord.source = source

    #print block['number']
    return brecord

def parse(path, block_id, source, editiontype, years):
    data = open(path).read().decode('utf-8')
    brecords = []

    blocks = parse_blocks(data, block_id)

    for block in blocks:
        # 1 Состоящий только из заголовка
        '''﻿37. ЗДРАВООХРАНЕНИЕ. МЕДИЦИНСКИЕ НАУКИ
Общие вопросы. Организация здравоохранения. Медицинская промышленность. Медицинская техника. Гигиена и санитария'''
        # 2 Библиографическая запись
        '''1027.	Азербайджанский медицинский жур-
нал = АзлрбхНчан тибб журналы: Ежемес. науч.-практ. журн. / М-во здравоохранения АзССР. — 1925 —	. — Баку, 1986 —	.
Азерб. и рус. яз., рез. на англ. яз.
ИССН 0005 — 2523:50 к. №.
1986. 6.475 — 6.560 экз.; 1987. 5.632 — 7.293 экз.; 1988. 7.316 — 7.395 экз.; 1989. 5.937 — 6.669 экз.; 1990. 6.127 — 6.178 экз.
—	Указ. к каждому году.'''
        # 3 Ссылка на другую библиографическую запись
        '''Вопросы вирусологии, — М. — См. 522.'''
        # 4 Библиографическая запись с заголовком
        '''1089.	Экспериментальная и клиническая медицина: / АН АрмССР. — 1961 —	. —
Ереван: Изд-во АН АрмССР, 1986 —
Двухмес. — Изд. с 1961 (год выхода журн. «Известия АН АрмССР»). — Парал. загл. на арм. яз.: Порцараракан ев клиникакан бжшку-тюн. — Рез. на англ, и арм. яз. — 3 а г л.: 1985 — 1988 Журнал экспериментальной и клинической медицины, ИССН 0514 — 7484.
ИССН [0235 — 9154]: 90 к. №.
1986. 980 экз.; 1987. 854 экз.; 1988. 770 экз.; 1989. 810 экз.; 1990. 720 экз. — Указ. к каждому году.
П р и л.: Кровообращение (см. 1120).
Медико-биологические дисциплины'''

        # 5 Старый тип библиографической записи
        '''2683.	Материалы теоретической и клинической медицины. Сб. работ аспирантов и ординаторов. Томск, Изд-во Том. ун-та. (Том. мед. .ин-т). ©
Вып. 6 1976. 1.000 экз. 78 к.
Вып. 5 — 1975.'''

        smmatch = RE_ENDOFBLOCK.match(block['text'])
        if block['text'].strip().endswith('.') or block['text'].strip().endswith('.")'):
            if smmatch:
                brecord = parse_data_block(block, heading, source, editiontype, years)
                brecords.append(brecord) # type 3
            else:
                brecord = parse_data_block(block, heading, source, editiontype, years)
                brecords.append(brecord) # type 2
            #убрать лишнюю проверку
        else:
            if block['text'].startswith(str(block['number'])):
                brecord = parse_data_block(block, heading, source, editiontype, years)
                brecords.append(brecord)
                end_block = block['text'].rfind('.\n')
                heading = clean_str(block['text'][end_block + 1:])
            elif 'editiontype' not in block:
                heading = clean_str(block['text'])

            if block.get('editiontype'):
                editiontype = block['editiontype']
             # type 1
            # В заголовок попадают все встречающиеся рубрикации, включая "Медицина". "37.Медицина..." удалю на следующем этапе
            # end_block = block['text'].rfind('.\n')
            # if end_block != -1:
            #     heading = clean_str(block['text'][end_block + 1:])
            # else:
            #     heading = clean_str(block['text'].split('\n')[2])



    return brecords
