from django.shortcuts import render
from django.core.mail import send_mail




def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		#do_stuff
		message_name = request.POST['message-name'] 
		message_email = request.POST['message-email'] 
		message = request.POST['message'] 

		#Send Email
		send_mail(
			message_name, #subject
			message, #message
			message_email, #from_email
			['ahror.valiev@gmail.com'], #to email
			fail_silently=False, 
			)
		
		return render(request, 'contact.html', {'message_name': message_name })

	else:
		#return the page
	    return render(request, 'contact.html', {})


def service(request):
	return render(request, 'service.html')

def about(request):
	return render(request, 'about.html')



def appointment(request):
	if request.method == "POST":
		#do_stuff
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_date = request.POST['your-time']
		your_message = request.POST['your-message']

		send_mail(
			your_message, #subject
			your_name, #message
			your_email, #from_email
			['ahror.valiev@gmail.com'], #to email
			fail_silently=False
			)


		     
		
		
		
		return render(request, 'appointment.html', {
	
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
			'your_schedule': your_schedule,
			'your_time': your_date,
			'your_message': your_message,

			})

	else:
		#return the page
	    return render(request, '', {})



def book(request):
	return render(request, 'book.html')