import pandas as pd
import openpyxl, os
from openpyxl import load_workbook
from openpyxl import Workbook


contact_prev = pd.read_excel('C:/Users/lego0/Downloads/삼성발주_상혁님(20일).xlsx')			# contact 메일 발송한 엑셀파일 (비고작성 후)
admin = pd.read_excel('C:/Users/lego0/Downloads/주문확인(20일).xlsx')						# 16시에 admin에서 추출한 엑셀파일 (비고작성 전)
contact = contact_prev[9:]														# admin 주문목록 최상단과 일치시키도록 contact_prev 일부를 수정(20일에는 [9:]슬라이싱하면 됐었음..)


# len(admin) < len(contact) 인지 먼저 확인!

def Check_IssueList():
	contact_list = contact[['매장명', '품목명', '주문량']].values.tolist()
	admin_list = admin[['매장명', '품목명', '주문량']].values.tolist()
	for i in admin_list:
		for j in contact_list:
			if i == j:
				contact_list.remove(j)
				break
	return 	print(*contact_list, sep='\n')							# contact와 admin의 데이터 비교하여 불일치하는 목록만 프린트



left_join_null['변경매장명'].values.tolist()
K = []
for i in left_join_null['변경매장명'].values.tolist():
	if len(i) > 3:
		k = i[:3]
		K.append(k)


def Check_IssueList():
	admin_list = admin2[['삼성코드', '매입가합']].values.tolist()
	doremi_list = doremi[['삼성코드', '매입가합']].values.tolist()
	for i in doremi_list:
		for j in admin_list:
			if abs(i-j) < 700:
				admin_list.remove(j)
				break
	return 	print(*admin_list, sep='\n')



