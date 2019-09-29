from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_
from .models import *
import math, random
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
# Create your views here.
import http.client
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny


from rest_framework.authtoken.models import Token

from datetime import timedelta
from django.utils import timezone
from email.mime.text import MIMEText
from django.template import loader

import dateutil.parser
# class HelloView(APIView):
#     permission_classes = (IsAuthenticated,)             # <-- And here

#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)

def test(request):
	if request.method=='POST':
		get=request.POST['emails']

		try:

		
			u=User.objects.get(email=get)

		except Exception as er:
			return HttpResponse('wrong user')
		
		#u=User.objects.get(email=get)
		
		try:
			Token.objects.get(user_id=u.pk)
			return HttpResponse('Email has been already send')
		except Exception as e:
			print(e)
		
		s=Token.objects.get_or_create(user=u)
		#print(s.key)


		d=Token.objects.get(user_id=u.pk)


			#token.delete()


		# message = 'This is my test message'
		html_message = """<html>
						<head>
							<title></title>
						</head>
						<body>
							<h1>Hello {0}</h1>
							<a href="http://127.0.0.1:8000/change-password/{1}">'http://127.0.0.1:8000/change-password/{2}'</a>
						</body>
						</html>""".format(u.first_name,d.key,s[0])


		# send_mail('password-reset', settings.DEFAULT_FROM_EMAIL, 'gamingzonedhruv@gmail.com',[u.email],fail_silently=True,html_message=html_message)


		subject, from_email, to = 'password_reset', settings.DEFAULT_FROM_EMAIL,u.email
		#text_content = 'This is an important message.'
		html_content = '<p>This is an <strong>important</strong> message.</p>'
		msg = EmailMultiAlternatives(subject, html_message, from_email, [to])
		msg.attach_alternative(html_message, "text/html")
		msg.send()
		
		
		return HttpResponse("""<p>
						We've emailed you instructions for setting your password, if an account exists with the email you entered.
					    You should receive them shortly.
					 </p>
					 <p>
					    If you don't receive an email, please make sure you've entered the address you registered with,
					    and check your spam folder.
					 </p>""")
		

	return render(request,'otp.html')

def home(request):
	return render(request,'cousre/home_page.html')

def login_page(request):
	if request.method =='POST':

		us=request.POST['username']
		pas=request.POST['password']
		user = authenticate(request, username=us,password=pas)
		if user is not None:
			login_(request, user)
			print(user)
			return redirect("/")
		else:
			print(user)
			return HttpResponse("wrong login")
	return render(request,'index.html')

def register(request):
	if request.method == 'POST':
		u = request.POST['user']
		e = request.POST['email']
		p = request.POST['password']
		f = request.POST['first']
		phones = request.POST['phone']

		User.objects.create_user(username=u,email=e,password=p,first_name=f)
		a=User.objects.get(username=u)
		Token.objects.get_or_create(user=a)

		user_extend.objects.create(users=a,phone_no=phones)

		return HttpResponse('successfully Registered')
  
	return render(request, 'TRegistraion.html',{})


# def sendSMS(request):


# 	if request.method =='POST':
# 		numbers=request.POST['mobile']

		

# 		#get=user_extend.objects.get(phone_no=numbers)
# 		#f=str(get.users.id)



# 		try:

# 			if user_extend.objects.get(phone_no=numbers):
# 				digits = "0123456789"
# 				otps = ""
# 				a=user_extend.objects.get(phone_no=numbers)
# 				f=str(a.users.id)
# 				for i in range(4) : 
# 					otps += digits[math.floor(random.random() * 10)]

# 				a.otp=otps
# 				a.save()


# 				conn = http.client.HTTPSConnection("api.msg91.com")

# 				payload = '''{
# 				  "sender": "ABCDEF",
# 				  "route": "4",
# 				  "country": "91",
# 				  "sms": [
# 					{
# 					  "message": " %s ",
# 					  "to": [
						
# 						"%s"
# 					  ]
# 					}
# 				  ]
# 				}''' % (otps,numbers)

# 				headers = {
# 					'authkey': "290578AMI5qFkn5d5d50dc",
# 					'content-type': "application/json"
# 					}

# 				conn.request("POST", "/api/v2/sendsms?country=91", payload, headers)

# 				res = conn.getresponse()
# 				data = res.read()

# 				print(data.decode("utf-8"))
# 				print(otps)
# 				return redirect('/otp/'+f,{})

				

# 		except ObjectDoesNotExist:
# 			return HttpResponse('wrong number')
				
# 	return render(request,'otp.html')



# def verify_otp(request,pk):
# 	get_data=get_object_or_404(user_extend,pk=pk)
# 	f=str(get_data.users.id)
# 	if request.method =='POST':
# 		otp_code=request.POST['otpcode']

# 		get_new=int(otp_code)

# 		get=get_data.otp

# 		if get==get_new:
# 			return redirect('/change-password/'+f)
# 		else:
# 			return HttpResponse('wrong')



# 	return render(request,'otp_verify.html',{'get_data':get_data})



def changePassword(request,token):
	
	#g=get_object_or_404(Token,key=token.key)
	#print(token)
	try:

		if Token.objects.get(key=token):

			print('OMG')
			f=Token.objects.get(key=token)
			get_data=User.objects.get(id=f.user_id)
			
	except Exception as e:
		return HttpResponse('wrong token')



	

	
	if request.method =='POST':
		get_password=request.POST['csf']

		get_data.set_password(get_password)
		get_data.save()
		#print(get_data)
		f.delete()

		return HttpResponse('password successfully changed')

	# try:

	# 	#s=Token.objects.get(user_id=1)
	# 	

	# except ObjectDoesNotExist:
	# 	return HttpResponse('you got wrong token')


	
	
	return render(request,'change_password.html',{})


def contact_page(request):
	if request.method =='POST':
		f=request.POST['first-name']
		l=request.POST['last-name']
		p=request.POST['phone']
		m=request.POST['message']
		e = request.POST['email']

		try:

			if feedback.objects.get(name=f):
				return HttpResponse('you have already submitted')

				

		except Exception as ss:
			print(ss)

		feedback.objects.create(name=f,last=l,email=e,phone=p,message=m)
			
		return HttpResponse('<h1>FeedBack is submitted</h1>')
	return render(request,'contact.html',{})