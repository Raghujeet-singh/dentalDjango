from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method =="POST":
		#do stuff
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		#send mail
		send_mail(
		    message_name, 
		    message,
		    message_email,
		    ['viratcpr01@gmail.com'],
		    fail_silently=False,
		    )

		return render(request, 'contact.html', {'message_name': message_name})

	else:
		
	    return render(request, 'contact.html', {})