from django.shortcuts import render, redirect
from emptyspace.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import requests


def welcome(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pnumber = request.POST['pnumber']
        mes1 = 'Hi' + ' ' + 'Team' + ',' \
                '\n I am interested to join with you to make my life better than now' \
                '\n please see my details below' \
                '\nMy first name : ' + firstname + ' ' + \
                '\nMy last name : ' + lastname + ' ' +  \
                '\nMy email address : ' + email + ' ' + \
                '\nMy phone number : ' + pnumber + ' ' \
                '\n Thank you '
        subject = 'Welcome to Murugan Yoga Center'
        message = 'Hi' + ' ' + firstname + ' ' + lastname + ',' \
                  '\nHope you are enjoying your life. Make your life much more ' \
                  'better than now. \nTake a look at me. we will get back to you ' \
                  'with in short period of time ' \
                   '\n Thank you ' \
                    '\nTeam - Murugan Yoga Center'
        recepient = str(email)
        send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        send_mail('Your app was accessed by me',
                   mes1, EMAIL_HOST_USER,[EMAIL_HOST_USER], fail_silently=False)
        return render(request, 'welcome.html', {'name': lastname})
    else:
        kname = 'Sir'
        return render(request, 'welcome.html', {'name': kname})

