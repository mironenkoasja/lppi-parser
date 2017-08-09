# Тест парсера и записи в csv файл

import unittest
import difflib
import csv
from parser_lppi import parse
from writer_in_csv import write_in_csv

class TestParcerCsvOut(unittest.TestCase):
    
    def test_1986_1990_jurn(self):
        source = u'Летопись печатных и периодических изданий СССР. Журналы. 1986 - 1990'
        editiontype = u'журнал'
        start_block_id = 1027
        years = ('1986', '1987', '1988', '1989', '1990')
        first_str = (
        'number', 'title', 'local_title', 'title_data', 'organization', 'first_year',
        'place', 'additional_data', 'heading', 'period', 'source', 'editiontype'
        'price 1986','edition 1986',  'price 1987', 'edition 1987',  'price 1988', 'edition 1988', 'price 1989',
        'edition 1989','price 1990','edition 1990' 
        )
        txt_path = 'text_files/lppi_1986_1990/lppi_1986_1990_jurn/lppi_jurn_1986_1990.txt'
        test_path = 'testing/lppi_1986_1990/lppi_1986_1990_jurn/lppi_1986_1990_jurn_test.csv'
        parsed_path = 'parsed/lppi_1986_1990/lppi_1986_1990_jurn/lppi_1986_1990_jurn.csv'
        bibliorecords = parse(txt_path, start_block_id, source, editiontype, years)       
        with open(test_path, 'w') as outfile_new:
            write_in_csv(outfile_new, bibliorecords, years, first_str)
        with open(parsed_path, 'r') as outfile_old:
            with open(test_path, 'r') as outfile_new:
                list_1 = outfile_new.readlines()
                list_2 = outfile_old.readlines()
        diff = difflib.unified_diff(list_1, list_2, lineterm='')
        #print '\n'.join(list(diff))
        self.assertFalse('\n'.join(list(diff)))
        
    def test_1981_1985_jurn(self):
        editiontype = u'журнал'
        start_block_id = 914
        source = u'Летопись печатных и периодических изданий СССР. Журналы. 1981 - 1985'
        years = ('1981', '1982', '1983', '1984', '1985')
        first_str = (
        'number', 'title', 'local_title', 'title_data', 'organization', 'first_year',
        'place', 'additional_data', 'heading', 'period', 'source', 'editiontype'
        'price 1981','edition 1981',  'price 1982', 'edition 1982',  'price 1983', 'edition 1983', 'price 1984',
        'edition 1984','price 1985','edition 1985' 
        )
        txt_path = 'text_files/lppi_1981_1985/lppi_1981_1985_jurn/lppi_1981_1985_jurn.txt'
        test_path = 'testing/lppi_1981_1985/lppi_1981_1985_jurn/lppi_1981_1985_jurn_test.csv'
        parsed_path = 'parsed/lppi_1981_1985/lppi_1981_1985_jurn/lppi_1981_1985_jurn.csv'
        bibliorecords = parse(txt_path, start_block_id, source, editiontype, years)       
        with open(test_path, 'w') as outfile_new:
            write_in_csv(outfile_new, bibliorecords, years, first_str)
        with open(parsed_path, 'r') as outfile_old:
            with open(test_path, 'r') as outfile_new:
                list_1 = outfile_new.readlines()
                list_2 = outfile_old.readlines()
        diff = difflib.unified_diff(list_1, list_2, lineterm='')
        #print '\n'.join(list(diff))
        self.assertFalse('\n'.join(list(diff)))
        
    def test_1986_1990_sbr(self):
        editiontype = u'сборник'
        start_block_id = 1455
        source = u'Летопись печатных и периодических изданий СССР. Сборники. 1986 - 1990'
        years = ('1986', '1987', '1988', '1989', '1990')
        first_str = (
        'number', 'title', 'local_title', 'title_data', 'organization', 'first_year',
        'place', 'additional_data', 'heading', 'period', 'source', 'editiontype'
        'price 1986','edition 1986',  'price 1987', 'edition 1987',  'price 1988', 'edition 1988', 'price 1989',
        'edition 1989','price 1990','edition 1990' 
        )
        txt_path = 'text_files/lppi_1986_1990/lppi_1986_1990_sbr/lppi_1986_1990_sbr.txt'
        test_path = 'testing/lppi_1986_1990/lppi_1986_1990_sbr/lppi_1986_1990_sbr_test.csv'
        parsed_path = 'parsed/lppi_1986_1990/lppi_1986_1990_sbr/lppi_1986_1990_sbr.csv'
        bibliorecords = parse(txt_path, start_block_id, source, editiontype, years)       
        with open(test_path, 'w') as outfile_new:
            write_in_csv(outfile_new, bibliorecords, years, first_str)
        with open(parsed_path, 'r') as outfile_old:
            with open(test_path, 'r') as outfile_new:
                list_1 = outfile_new.readlines()
                list_2 = outfile_old.readlines()
        diff = difflib.unified_diff(list_1, list_2, lineterm='')
        #print '\n'.join(list(diff))
        self.assertFalse('\n'.join(list(diff)))
        
    def test_1981_1985_sbr(self):
        editiontype = u'сборник'
        start_block_id = 1594
        source = u'Летопись печатных и периодических изданий СССР. Сборники. 1981 - 1985'
        years = ('1981', '1982', '1983', '1984', '1985')
        first_str = (
        'number', 'title', 'local_title', 'title_data', 'organization', 'first_year',
        'place', 'additional_data', 'heading', 'period', 'source', 'editiontype'
        'price 1981','edition 1981',  'price 1982', 'edition 1982',  'price 1983', 'edition 1983', 'price 1984',
        'edition 1984','price 1985','edition 1985' 
        )
        txt_path = 'text_files/lppi_1981_1985/lppi_1981_1985_sbr/lppi_1981_1985_sbr.txt'
        test_path = 'testing/lppi_1981_1985/lppi_1981_1985_sbr/lppi_1981_1985_sbr_test.csv'
        parsed_path = 'parsed/lppi_1981_1985/lppi_1981_1985_sbr/lppi_1981_1985_sbr.csv'
        bibliorecords = parse(txt_path, start_block_id, source, editiontype, years)       
        with open(test_path, 'w') as outfile_new:
            write_in_csv(outfile_new, bibliorecords, years, first_str)
        with open(parsed_path, 'r') as outfile_old:
            with open(test_path, 'r') as outfile_new:
                list_1 = outfile_new.readlines()
                list_2 = outfile_old.readlines()
        diff = difflib.unified_diff(list_1, list_2, lineterm='')
        #print '\n'.join(list(diff))
        self.assertFalse('\n'.join(list(diff)))
        
    def test_1986_1990_bul(self):
        editiontype = u'бюллетень'
        start_block_id = 2535
        source = u'Летопись печатных и периодических изданий СССР. Бюллетени. 1986 - 1990'
        years = ('1986', '1987', '1988', '1989', '1990')
        first_str = (
        'number', 'title', 'local_title', 'title_data', 'organization', 'first_year',
        'place', 'additional_data', 'heading', 'period', 'source', 'editiontype'
        'price 1986','edition 1986',  'price 1987', 'edition 1987',  'price 1988', 'edition 1988', 'price 1989',
        'edition 1989','price 1990','edition 1990' 
        )
        txt_path = 'text_files/lppi_1986_1990/lppi_1986_1990_bul/lppi_1986_1990_bul.txt'
        test_path = 'testing/lppi_1986_1990/lppi_1986_1990_bul/lppi_1986_1990_bul_test.csv'
        parsed_path = 'parsed/lppi_1986_1990/lppi_1986_1990_bul/lppi_1986_1990_bul.csv'
        bibliorecords = parse(txt_path, start_block_id, source, editiontype, years)       
        with open(test_path, 'w') as outfile_new:
            write_in_csv(outfile_new, bibliorecords, years, first_str)
        with open(parsed_path, 'r') as outfile_old:
            with open(test_path, 'r') as outfile_new:
                list_1 = outfile_new.readlines()
                list_2 = outfile_old.readlines()
        diff = difflib.unified_diff(list_1, list_2, lineterm='')
        #print '\n'.join(list(diff))
        self.assertFalse('\n'.join(list(diff)))         
    
    def test_1981_1985_bul(self):
        editiontype = u'бюллетень'
        start_block_id = 2511
        source = u'Летопись печатных и периодических изданий СССР. Бюллетени. 1981 - 1985'
        years = ('1981', '1982', '1983', '1984', '1985')
        first_str = (
        'number', 'title', 'local_title', 'title_data', 'organization', 'first_year',
        'place', 'additional_data', 'heading', 'period', 'source', 'editiontype'
        'price 1981','edition 1981',  'price 1982', 'edition 1982',  'price 1983', 'edition 1983', 'price 1984',
        'edition 1984','price 1985','edition 1985' 
        )
        txt_path = 'text_files/lppi_1981_1985/lppi_1981_1985_bul/lppi_1981_1985_bul.txt'
        test_path = 'testing/lppi_1981_1985/lppi_1981_1985_bul/lppi_1981_1985_bul_test.csv'
        parsed_path = 'parsed/lppi_1981_1985/lppi_1981_1985_bul/lppi_1981_1985_bul.csv'
        bibliorecords = parse(txt_path, start_block_id, source, editiontype, years)       
        with open(test_path, 'w') as outfile_new:
            write_in_csv(outfile_new, bibliorecords, years, first_str)
        with open(parsed_path, 'r') as outfile_old:
            with open(test_path, 'r') as outfile_new:
                list_1 = outfile_new.readlines()
                list_2 = outfile_old.readlines()
        diff = difflib.unified_diff(list_1, list_2, lineterm='')
        #print '\n'.join(list(diff))
        self.assertFalse('\n'.join(list(diff)))      
    
        
  