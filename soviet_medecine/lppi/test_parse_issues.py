# encoding: utf-8
%load_ext autoreload
%autoreload 2

# %pwd
# %cd soviet_medecine/lppi
import unittest
from parser_lppi import parse_issues

class TestParcerIssue(unittest.TestCase):

    def test_issues_1(self): # год. тираж, тираж - тираж, одна цена для всех лет
        block = {'number': 1030, 'text': u'''1030.	Вопросы медицинской химии: Двух-
мес. науч.-теорет. журн. / АМН СССР. — 1955 —	. — М.: Медицина, 1986 —
Рез. на англ. яз.
ИССН 0042 — 8809: 1 р. 30 к. №.
1986. 1.531 экз.; 1987. 1.564 экз.; 1988. 1.577 экз.; 1989. 1.542 экз.; 1990. 1.471 — 1.536 экз. — Указ. к каждому году.'''}
        issn = block['text'].find(u'ИССН')
        years = ('1986', '1987', '1988', '1989', '1990')
        issues = parse_issues(block, years, issn)
        keys = issues.keys()
        self.assertEqual(set(keys), set(['1986', '1987', '1988', '1989', '1990']))
        self.assertEqual(issues['1986'].edition, 1531.)
        self.assertEqual(issues['1986'].price, 130.)
        self.assertEqual(issues['1987'].edition, 1564.)
        self.assertEqual(issues['1987'].price, 130.)
        self.assertEqual(issues['1988'].edition, 1577.)
        self.assertEqual(issues['1988'].price, 130.)
        self.assertEqual(issues['1989'].edition, 1542.)
        self.assertEqual(issues['1989'].price, 130.)
        self.assertEqual(issues['1990'].edition, 1504.)
        self.assertEqual(issues['1990'].price, 130.)

    def test_issues_2(self): # год. ценаб тираж, один год
        block = {'number': 1456, 'text': u'''1456.	Борьба с силикозом: Сб. ст. / Ин-т горн, дела им. А А Скочинского. Центр, междувед. комис. по борьбе с пневмоконио-зом. — Т. 1 (1953) — Т. 12 (1986). — М.: Наука, 1986.

Прекр. на т. 12.

[ИССН 0202—5167].

Т. 12. 1986. 2 р. 80 к., 1.200 экз.

Т. 11 (1982).'''}
        issn = block['text'].find(u'ИССН')
        years = ('1986', '1987', '1988', '1989', '1990')
        issues = parse_issues(block, years, issn)
        keys = issues.keys()
        self.assertEqual(set(keys), set(['1986']))
        self.assertEqual(issues['1986'].edition, 1200.)
        self.assertEqual(issues['1986'].price, 280.)

    def test_issues_3(self): # год. цена, тираж, все года
        block = {'number': 1458, 'text': u'''1458.	Врачебно-трудовая экспертиза и

реабилитация инвалидов: Респ. межвед. сб. / М-во соц. обеспечения УССР. Днепропетр. НИИ восстановления и экспертизы трудоспособности инвалидов. — [Вып. 1] (1967) —	. — Киев: Здоров'я, 1986 —
ИССН 0234—6656.

Вып. 18. 1986. 1 р. 30 к., 1.000 экз.; Вып.

19.	1987. 1 р. 20 к., 1.000 экз.; Вып. 20. 1988. 1 р. 80 к., 1.800 экз.; Вып. 21. 1989. 1 р. 70 к., 1.750 экз.; Вып. 22. 1990. 1 р. 60 к.,

2.000	экз.

Вып. 17 (1985).'''}
        issn = block['text'].find(u'ИССН')
        years = ('1986', '1987', '1988', '1989', '1990')
        issues = parse_issues(block, years, issn)
        keys = issues.keys()
        self.assertEqual(set(keys), set(['1986', '1987', '1988', '1989', '1990']))
        self.assertEqual(issues['1986'].edition, 1000.)
        self.assertEqual(issues['1986'].price, 130.)
        self.assertEqual(issues['1987'].edition, 1000.)
        self.assertEqual(issues['1987'].price, 120.)
        self.assertEqual(issues['1988'].edition, 1800.)
        self.assertEqual(issues['1988'].price, 180.)
        self.assertEqual(issues['1989'].edition, 1750.)
        self.assertEqual(issues['1989'].price, 170.)
        self.assertEqual(issues['1990'].edition, 2000.)
        self.assertEqual(issues['1990'].price, 160.)

    def test_issues_4(self): # год. цена, тираж один на все года с изменениями
        block = {'number': 1459, 'text': u'''1459.	Гигиена населенных мест: Респ.

межвед. сб. / М-во здравоохранения УССР. Киев. НИИ общ. и коммун, гигиены. — [Вып. 1] (1956) —	. — Киев: Здоров'я,

1986 —

ИССН 0135—2091, 1.000 экз. (вып. 29. 2.000	экз.)

Вып. 25. 1986. 1 р. 20 к.; Вып. 26. 1987. 1 р. 20 к.; Вып. 27. 1988. 1 р. 80 к.; Вып. 28.

1989.	1 р. 80 к.; Вып. 29. 1990. 1 р. 60 к.

Вып. 24 (1985).'''}
        issn = block['text'].find(u'ИССН')
        years = ('1986', '1987', '1988', '1989', '1990')
        issues = parse_issues(block, years, issn)
        keys = issues.keys()
        self.assertEqual(set(keys), set(['1986', '1987', '1988', '1989', '1990']))
        self.assertEqual(issues['1986'].edition, 1000.)
        self.assertEqual(issues['1986'].price, 120.)
        self.assertEqual(issues['1987'].edition, 1000.)
        self.assertEqual(issues['1987'].price, 120.)
        self.assertEqual(issues['1988'].edition, 1000.)
        self.assertEqual(issues['1988'].price, 180.)
        self.assertEqual(issues['1989'].edition, 1000.)
        self.assertEqual(issues['1989'].price, 180.)
        self.assertEqual(issues['1990'].edition, 2000.)
        self.assertEqual(issues['1990'].price, 160.)

    def test_issues_5(self): # год. цена и тираж на все года
        block = {'number': 1460, 'text': u'''1460.	Гигиена применения, токсикология пестицидов и полимерных материалов: Сб.

науч. тр. / ВНИИ гигиены и токсикологии пестицидов, полимеров и пласт, масс. — [Вып. 1] (1959) — вып. 19 (1989). — Киев, 1985—1989.

Прекр. на вып. 19.

ИССН 0234—5439: 1 р. 50 к., 1.000 экз.

Вып. 15. 1985; Вып. 16. 1986; Вып. 17. 1987; Вып. 18. 1988; Вып. 19. 1989.

Вып. 14 (1984).'''}
        issn = block['text'].find(u'ИССН')
        years = ('1986', '1987', '1988', '1989', '1990')
        issues = parse_issues(block, years, issn)
        keys = issues.keys()
        self.assertEqual(set(keys), set(['1986', '1987', '1988', '1989']))
        self.assertEqual(issues['1986'].edition, 1000.)
        self.assertEqual(issues['1986'].price, 150.)
        self.assertEqual(issues['1987'].edition, 1000.)
        self.assertEqual(issues['1987'].price, 150.)
        self.assertEqual(issues['1988'].edition, 1000.)
        self.assertEqual(issues['1988'].price, 150.)
        self.assertEqual(issues['1989'].edition, 1000.)
        self.assertEqual(issues['1989'].price, 150.)

    def test_issues_6(self): # несколько томов в год. Средния цена и тираж
        block = {'number': 1468, 'text': u'''1468.	Научные труды / Новосиб. мед. ин-т.

—	Т. 1 (1931) —	. — Новосибирск, 1986

ИССН 0374—9959.

Т. 123. 1986. 55 к., 1.000 экз.; Т. 124. 1986. 1 р. 30 к., 1.000 экз.; Т. 125. 1986. 80 к., 1.000 экз.; Т. 126. 1987. 95 к., 1.000 экз.; Т. 127.

1987.	90 к., 500 экз.; Т. 128. 1987. 85 к., 1.000 экз.; Т. 129. 1988. 50 к., 500 экз.; Т. 130. 1988. 1 р., 1.000 экз.; Т. 131. 1988. 65 к., 900 экз.; Т. 132. 1988. 75 к., 1.000 экз.; Т. 133. 1989. 0 к., 1.100 экз.; Т. 135. 1989. 60 к., 550 экз.

Т. 122 (1985).'''}
        issn = block['text'].find(u'ИССН')
        years = ('1986', '1987', '1988', '1989', '1990')
        issues = parse_issues(block, years, issn)
        keys = issues.keys()
        self.assertEqual(set(keys), set(['1986', '1987', '1988', '1989']))
        self.assertEqual(issues['1986'].edition, 1000.)
        self.assertEqual(issues['1986'].price, 88.)
        self.assertEqual(issues['1987'].edition, 833.)
        self.assertEqual(issues['1987'].price, 90.)
        self.assertEqual(issues['1988'].edition, 850.)
        self.assertEqual(issues['1988'].price, 73.)
        self.assertEqual(issues['1989'].edition, 825.)
        self.assertEqual(issues['1989'].price, 30.)

    def test_issues_7(self): # год. диапазон цен, тираж
        block = {'number': 2536, 'text': u'''2536. Бюллетень Сибирского отделения
Академии медицинских наук СССР. — 1981 —     . — Новосибирск, 1986 —
   Ежекварт. (1986—1989 двухмес.)
   ИССН 0207—6322.
   1986.  80 к., 500 экз.; 1987. 80 к., 500—1.100 экз.; 1988. 60—80 к., 1.100 экз.; 1989. 80 к. — 2 р. 40 к., 800—1.100 экз.; 1990. 2р. 20к.— 2 р. 40 к., 500—800 экз.'''}
        issn = block['text'].find(u'ИССН')
        years = ('1986', '1987', '1988', '1989', '1990')
        issues = parse_issues(block, years, issn)
        keys = issues.keys()
        self.assertEqual(set(keys), set(['1986', '1987', '1988', '1989', '1990']))
        self.assertEqual(issues['1986'].edition, 500.)
        self.assertEqual(issues['1986'].price, 80.)
        self.assertEqual(issues['1987'].edition, 800.)
        self.assertEqual(issues['1987'].price, 80.)
        self.assertEqual(issues['1988'].edition, 1100.)
        self.assertEqual(issues['1988'].price, 70.)
        self.assertEqual(issues['1989'].edition, 950.)
        self.assertEqual(issues['1989'].price, 160.)
        self.assertEqual(issues['1990'].edition, 650.)
        self.assertEqual(issues['1990'].price, 230.)

    def test_issues_8(self): # год. диапазон цен, тираж
        block = {'number': 2584, 'text': u''' 2584.    Экономика медицинской промышленности: Обзор, информ. / М-во мед. пром-сти СССР. НПО «Медбиоэкономика». ВНИИ систем упр., экон. исслед. и НТИ.
—   1990 —     . — М., 1990 —
   Ежекварт.
   [ИССН 0236—4387].
   1990. 48 к.—2 р. 16 к., 250—510 экз.
                         Медико-биологические дисциплины'''}
        issn = block['text'].find(u'ИССН')
        years = ('1986', '1987', '1988', '1989', '1990')
        issues = parse_issues(block, years, issn)
        print issues
        keys = issues.keys()
        self.assertEqual(set(keys), set(['1990']))
        self.assertEqual(issues['1990'].edition, 380.)
        self.assertEqual(issues['1990'].price, 132.)

    def test_issues_9(self): # год. диапазон цен, тираж
        block = {'number': 2514, 'text': u'''2514.	Гигиена: Экспресс-информация /
ВНИИ мед. и мед.-техн. информ. — 1973 —	. — М., 1981 —
Ежемес. — Загл.: 1980 — 1984 Экспресс-информация. — Загл. серии: 1980— 1984 Гигиена окружающей среды, ИССН 0202—4608.
ИССН 0234—3029: 20 к. вып. (1981— 1983 15 к.)
1981. 1.732—1.810 экз.; 1982. 1.735—1.940 экз.;	1983.	1.690 экз.;	1984.	1.614 экз.;
1985. 1.528 экз. — Указ, к каждому году.'''}
        issn = block['text'].find(u'ИССН')
        years = ('1981', '1982', '1983', '1984', '1985')
        issues = parse_issues(block, years, issn)
        keys = issues.keys()
        self.assertEqual(set(keys), set(['1981', '1982', '1983', '1984', '1985']))
        self.assertEqual(issues['1981'].edition, 1771.)
        self.assertEqual(issues['1981'].price, 15.)
        self.assertEqual(issues['1982'].edition, 1838.)
        self.assertEqual(issues['1982'].price, 15.)
        self.assertEqual(issues['1983'].edition, 1690.)
        self.assertEqual(issues['1983'].price, 15.)
        self.assertEqual(issues['1984'].edition, 1614.)
        self.assertEqual(issues['1984'].price, 20.)
        self.assertEqual(issues['1985'].edition, 1528.)
        self.assertEqual(issues['1985'].price, 20.)

    def test_issues_10(self): # год. диапазон цен, тираж
        block = {'number': 2516, 'text': u'''2516.	Инструкции, аннотации и другие
материалы по применению медицинских средств / М-во здравоохранения СССР, Гл. аптеч. упр. — 1970 —	. — М.:
Всесоюз. информ. бюро, 1981 —
ИССН 0134—7152	1.000 экз. (1981. 30.000 экз.)
1981 Вып. 1 — 6. Беспл.; 1982 Вып. 1 — 8. Б. ц.; 1983 Вып. 1—4. Беспл.; 1984 Вып. 1—4. Б. ц.; 1985 Вып. 1—4. Беспл.
Вып. 2 — 1980.'''}
        issn = block['text'].find(u'ИССН')
        years = ('1981', '1982', '1983', '1984', '1985')
        issues = parse_issues(block, years, issn)
        keys = issues.keys()
        self.assertEqual(set(keys), set(['1981', '1982', '1983', '1984', '1985']))
        self.assertEqual(issues['1981'].edition, 30000.)
        self.assertEqual(issues['1981'].price, 0.)
        self.assertEqual(issues['1982'].edition, 1000.)
        self.assertEqual(issues['1982'].price, 0.)
        self.assertEqual(issues['1983'].edition, 1000.)
        self.assertEqual(issues['1983'].price, 0.)
        self.assertEqual(issues['1984'].edition, 1000.)
        self.assertEqual(issues['1984'].price, 0.)
        self.assertEqual(issues['1985'].edition, 1000.)
        self.assertEqual(issues['1985'].price, 0.)

    def test_issues_11(self): # год. диапазон цен, тираж
        block = {'number': 1612, 'text': u'''1612. Охрана здоровья детей и подрост-
ков: Респ. междувед. сб. / М-во здравоохранения УССР, Харьк. НИИ охраны здоровья детей и подростков им. И. К. Крупской. — Вып. 1 1970 —       . — Киев: Здо-
ров’я, 1981 —
   ИССН 0369—8041: 1 р. 40 к. вып. (вып. 13. 1 р. 30 к.)     1.000 экз. (вып. 15. 965
экз.)
   Вып. 12. 1981; вып. 13. 1982; вып. 14. 1983; вып. 15. 1984; вып. 16. 1985.
   Вып. 11 — 1980.'''}
        issn = block['text'].find(u'ИССН')
        years = ('1981', '1982', '1983', '1984', '1985')
        issues = parse_issues(block, years, issn)
        keys = issues.keys()
        self.assertEqual(set(keys), set(['1981', '1982', '1983', '1984', '1985']))
        self.assertEqual(issues['1981'].edition, 1000.)
        self.assertEqual(issues['1981'].price, 140.)
        self.assertEqual(issues['1982'].edition, 1000.)
        self.assertEqual(issues['1982'].price, 130.)
        self.assertEqual(issues['1983'].edition, 1000.)
        self.assertEqual(issues['1983'].price, 140.)
        self.assertEqual(issues['1984'].edition, 965.)
        self.assertEqual(issues['1984'].price, 140.)
        self.assertEqual(issues['1985'].edition, 1000.)
        self.assertEqual(issues['1985'].price, 140.)

#unittest.main(argv=['ignored', '-v', 'TestParcerIssue'], exit=False)
unittest.main(argv=['ignored', '-v',], exit=False)
