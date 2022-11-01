import pandas as pd
import openpyxl, os
from openpyxl import load_workbook
from openpyxl import Workbook                                   # pip install openpyxl --upgrade --pre 


def extract_foodist():
 admin = pd.read_excel('C:/Users/soons/Downloads/주문_청구.xlsx')
 admin['매입가합'] = admin['매입가합'].replace(',','', regex=True).astype(float)              # 매입가합 일치하지 않는 매장들만 추출
 erp = pd.read_excel('C:/Users/soons/Downloads/Sheet1.xlsx')
 for i in admin['매입가합']:
  if i not in erp['입고총액'].values:
   print(admin[admin.매입가합 == i][[' 매장 ', '매입가합', '판매가합']])

extract_foodist()
os.remove('C:/Users/soons/Downloads/주문_청구.xlsx')
os.remove('C:/Users/soons/Downloads/Sheet1.xlsx')