from django.contrib.auth import authenticate, alogin, alogout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime

from .models import Bus, Book

# Views
def findBus(request):
    msg = {}
    if request.method == 'POST':
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        date = datetime.strptime(request.POST.get('date'),"%Y-%m-%d").date()
        year = date.strftime("%Y")
        month = date.strftime("%m")
        day = date.strftime("%d")
        bus_list = Bus.objects.filter(source=source, destination=destination, date__year=year, date__month=month, date__day=day)
        if bus_list:
            return render(request, 'list.html', locals())
        else:
            msg["error"] = "No available Bus Schedule for entered Route and Date"
            return render(request, 'findbus.html', {'msg': msg})
    else:
        return render(request, 'findbus.html')
        

@login_required(login_url='login_user')
def list(request):
    return render(request, 'list.html')

@login_required(login_url='login_user')
def booking(request):
    msg = {}
    if request.method == 'POST':
        bus_id = request.POST.get('busid')
        no_of_seats = request.POST.get('noofseats')
        nos = no_of_seats
        bus = Bus.objects.get(bus_id=bus_id)
        if bus:
            if bus.rem_seats > int(no_of_seats):
                first_name = request.user.first_name
                last_name = request.user.last_name
                email = request.user.email
                booking_id = bus.bus_id
                bus_name = bus.bus_name
                source = bus.source
                destination = bus.destination
                no_of_seats = int(no_of_seats)
                cost = int(no_of_seats) * bus.cost
                date = bus.date
                time = bus.time
                rem_seats = bus.rem_seats - int(nos)
                Bus.objects.filter(bus_id=bus_id).update(rem_seats=rem_seats)
                book = Book.objects.create(first_name=first_name, last_name=last_name, email=email, booking_id=booking_id, bus_name=bus_name, source=source, destination=destination, no_of_seats=no_of_seats, cost=cost, date=date, time=time, status='BOOKED')
                book_list = Book.objects.filter(email=email)
                return render(request, 'booklist.html', locals())
            else:
                msg["error"] = "Sorry select fewer number of seats"
                return render(request, 'findbus.html', {'msg': msg})
        else:
            msg["error"] = "Invalid Bus Name"
            return render(request, 'findbus.html', {'msg': msg})
    else:
        return render(request, 'findbus.html')

@login_required(login_url='login_user')
def booklist(request):
    email = request.user.email
    book_list = Book.objects.filter(email=email)
    return render(request, 'booklist.html', locals())

@login_required(login_url='login_user')
def cancel(request):
    msg = {}
    if request.method == 'POST':
        booking_id = request.POST.get('bookingid')

        try:
            book = Book.objects.get(booking_id=booking_id)
            bus = Bus.objects.get(bus_id=book.booking_id)
            rem_seats = bus.rem_seats + book.no_of_seats
            Bus.objects.filter(bus_id=book.booking_id).update(rem_seats=rem_seats)
            Book.objects.filter(booking_id=booking_id).update(status='CANCELLED')
            # Book.objects.filter(booking_id=booking_id).update(no_of_seats=0)
            email = request.user.email
            book_list = Book.objects.filter(email=email)
            return render(request, 'booklist.html', locals())
        except Book.DoesNotExist:
            msg['error'] = "Sorry you have not booked that bus"
            return render(request, 'booklist.html', locals(), {'msg': msg})
