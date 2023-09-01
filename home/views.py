# from django.shortcuts import render,HttpResponse, redirect
from home.models import Task
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from .forms import TaskForm



@login_required 
def home(request):
    if request.method == 'POST':
     form = TaskForm(request.POST, request.FILES)
     print("Is form valid?", form.is_valid())
     if form.is_valid():
            # Data is valid, proceed with saving
            form.save()  # Save the submitted task to the database
            return redirect('list')  # Redirect to a task list view
    else:
        form = TaskForm()  # Create an empty form for GET requests

    return render(request, 'index.html', {'form': form})


# def home(request):
#     context = {'success': False}

#     if request.method == "POST":
#         title = request.POST['title']
#         desc = request.POST['desc']
#         print(title, desc)
#         ins = Task(taskTitle=title, taskDesc=desc)
#         ins.save()
#         context = {'success': True}

#     return render(request, 'index.html', context)


@login_required
def task(request):
    allTasks=Task.objects.all()
    # print(allTasks)
    # for item in allTasks:
    #     print(item.taskDesc)
    context={'tasks':allTasks}

    return render(request,'list.html',context)



def Login(request):
    return render(request,'login.html')


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def handlesignup(request):
    # context={'success':False}
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('login')

        if not username.isalnum():
            messages.error(request, "Username must be letters and numbers")
            return redirect('login')

        if pass1 != pass2:
            messages.error(request, "Passwords don't match")
            return redirect('login')

        # Correct the typo here, it should be "messages.error" instead of "messages.erro"
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        # context={'success':True}


        messages.success(request, "Your account has been created")
        return redirect('login')
        # return redirect('login', context)


    else:
        return HttpResponse("404 Error")
  

from django.contrib import messages

def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")  # Add success message
            return redirect('home')  # Redirect to home page
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    else:
        return HttpResponse("404 Error")


def handlelogout(request):
    logout(request)
    messages.success(request, "successfully Logged out")
    return redirect('login')



    # return HttpResponse('handlelogout')
 
