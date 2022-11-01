import pandas as pd


admin = pd.read_excel('C:/Users/lego0/Downloads/주문_청구.xlsx')
store = []

for i in admin[' 매장 ']:
	store_instance = i.split(':')[1].split()[0]
	store.append(store_instance)


sid = []
for i in admin[' 매장 ']:
	sid_candidate = i.split(':')[0]
	if len(sid_candidate) > 5:
		sid.append(sid_candidate.split(']')[-1])
	else:
		sid.append(sid_candidate)


store_list=[]
for i in admin['사업자번호']:
	if i not in account['사업자번호'].values:
		print(admin[admin.사업자번호 == i][[' 매장 ']])


#---------------------------------------------------------------------

#pandas 열 추출
import pandas as pd
import openpyxl, os
from openpyxl import load_workbook
from openpyxl import Workbook


admin = pd.read_excel('C:/Users/lego0/Downloads/매장_결제_내역.xlsx')
data = admin.drop_duplicates(['sid'], keep = 'first')[['sid', '앱 표시 문구', '잔액(마일리지+현금)']]
data_mask = data['잔액(마일리지+현금)'] > 0

data[data_mask]
data[data_mask]['잔액(마일리지+현금)'].sum()



# left join 및 엑셀파일로 저장
pd.merge(cj, admin, how='left', on='변경매장명').to_excel('left_join.xlsx')




for i in range(admin['sid'].shape[0]):
	if ']' in admin['sid'].loc[i]:
		admin['sid2'] = str(admin['sid'].loc[i]).split(']')[1]
	else:
		admin['sid2'] = str(admin['sid'].loc[i])


for i in erp.판매가합:
	if i not in admin.판매가합.values:
		print(erp[erp.판매가합 == i][['사업장코드', '판매가합']])