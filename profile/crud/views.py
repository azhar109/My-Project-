from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models.apply import Apply
from .models.professor import Professor
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password, check_password


class Index(View):
    def get(self, request):
        professor = Professor.objects.all()
        user_id = request.session.get('user_id')
        context= {
            'professor':professor,
            'user':user_id
        }
        return render(request, 'index.html', context)


class About(View):
    def get(self, request):
        return render(request, 'about.html')


class Apply1(View):
    def get(self, request):
        return render(request, 'apply.html')

    def post(self, request):
        if request.method == 'POST':
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            country = request.POST.get('country')
            city = request.POST.get('city')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            campus = request.POST.get('campus')
            previousEducation = request.POST.get('previousEducation')
            extracurricularActivities = request.POST.get('extracurricularActivities')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            apply = Apply(firstname=firstname, lastname=lastname, country=country,
                                   city=city, email=email,
                                   phone=phone, campus=campus, previousEducation=previousEducation,
                                   extracurricularActivities=extracurricularActivities,
                                   password=password,
                                   confirm_password = confirm_password)
            error_message = None
            value ={
                'firstname':firstname,
                'lastname':lastname,
                'country':country,
                'city':city,
                'email':email,
                'phone':phone,
                'campus':campus,
                'previousEducation':previousEducation,
                'extracurricularActivities':extracurricularActivities,
                'error':error_message,
            }
            error_message = self.validation(apply)
            if not error_message:
                apply.password = make_password(apply.password)
                apply.confirm_password = make_password(apply.confirm_password)
                apply.save()
                return redirect('login')
        values = dict(error = error_message, value = value)
        return render(request, 'apply.html', values)

    def validation(self, apply):
        error_message = None
        if not apply.firstname:
            error_message = "Enter First Name"
        elif not apply.lastname:
            error_message = "Enter Last name"
        elif not apply.country:
            error_message = "Enter the Country"
        elif not apply.city:
            error_message = "Please Enter the City"
        elif not apply.email:
            error_message = "Enter the Valide Email"
        elif apply.email_check():
            error_message = "Email Already Exits"
        elif apply.check_phone():
            error_message = "This phone number already exists"
        elif not apply.phone:
            error_message = "Enter Phone the Number"
        elif not apply.campus:
            error_message = "Enter the Campus"
        elif not apply.previousEducation:
            error_message = "Write down previous education"
        elif not apply.password:
            error_message = "Enter the password"
        elif len(apply.password)<=5:
            error_message = "your password is very short"
        elif apply.password  != apply.confirm_password:
            error_message = "your password not match"
        return error_message


#login page
class Loginform(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        if request.method == 'POST':
            login_email = request.POST.get('email')
            login_password = request.POST.get('password')
            user = Apply.objects.filter(email=login_email).first()
            if user and check_password(login_password, user.password):
                # Log the user in (You might need to adjust this part based on your user model)
                request.session['user_id'] = user.id
                return redirect('home')
            else:
                login_error_message = "Invalid email or password"
        else:
            login_error_message = None
        return render(request, 'login.html', {'error':login_error_message})


def logout(request):
    request.session.clear()
    return redirect('home')

