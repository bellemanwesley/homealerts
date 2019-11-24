
import requests
import schedule
import time
from twilio.rest import Client

def apartment_puller():
	url = 'https://www.equityapartments.com/los-angeles/marina-del-rey/marina-41-apartments##unit-availability-tile'
	r = requests.get(url)
	url_info = r.text
	url_array = url_info.split("<div class=\"col-xs-4 specs\">")
	del(url_array[0])
	del(url_array[len(url_array)-1])
	for i in range(len(url_array)):
		temp_array = []
		temp_array.append(url_array[i][34+23:35+28])
		j2 = url_array[i].index("Bed <b>/</b>")
		temp_array.append(url_array[i][j2-2:j2+3])
		temp_array.append(url_array[i][j2+13:j2+19])
		j3 = url_array[i].index("sq.ft.</span>")
		temp_array.append(url_array[i][j3-5:j3+6])
		j4 = url_array[i].index("<span>Floor")
		temp_array.append(url_array[i][j4+6:j4+13])
		j5 = url_array[i].index("Available")
		temp_array.append(url_array[i][j5:j5+20])
		url_array[i]=temp_array
	for i in reversed(range(len(url_array))):
		if int(url_array[i][1][0]) !=2:
			del(url_array[i])
		elif int(url_array[i][0][1:2]+url_array[i][0][3:6]) > 4000:
			del(url_array[i])
		#elif url_array[i][3][0] == '>':
			#del(url_array[i])
		#elif int(url_array[i][3][0:4]) < 1200:
			#del(url_array[i])
	return(url_array)

def send_message(the_body):
	account_sid = 'AC75a39591d14401a882c79fbc8f7f5ebf'
	auth_token = my_auth_toke #pull from secure storage
	client = Client(account_sid, auth_token)

	message = client.messages.create(
    	from_='whatsapp:+14155238886',
        body=the_body,
        to='whatsapp:+15088732402'
    )

	account_sid = 'AC75a39591d14401a882c79fbc8f7f5ebf'
	auth_token = my_auth_token #pull from secure storage
	client = Client(account_sid, auth_token)

	message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=the_body,
        to='whatsapp:+15088318920'
    )

def job():
    send_message("I'm working...")

schedule.every(30).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)



