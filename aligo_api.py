import requests, json

send_url = 'https://apis.aligo.in/send/'

#sms_data={'key': 'ea6cnw5637iwhcc06fgl2e7msc52ouys', #api key
#        'userid': 'orderplus', # 알리고 사이트 아이디
#        'sender': '0264041020', # 발신번호
#        'receiver': '01032853649', # 수신번호 (,활용하여 1000명까지 추가 가능)
#        'msg': '박순성 TEST', #문자 내용 
#        'msg_type' : 'SMS'}, #메세지 타입 (SMS, LMS)
#        #'title' : 'title', #메세지 제목 (장문에 적용)
#        #'destination' : '01000000000|홍길동',}


sms_data = {'key': 'ea6cnw5637iwhcc06fgl2e7msc52ouys', 'userid': 'orderplus', 'sender': '0264041020', 'receiver': '01032853649', 'msg': '박순성 TEST'}

send_response = requests.post(send_url, data=sms_data)
print(send_response.json())