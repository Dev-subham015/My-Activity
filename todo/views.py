from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Todo
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
  if request.method == "POST":
    if not request.user.is_authenticated:
      messages.error(request, "You must be logged in to submit a todo.")
      return redirect("/")
    title = request.POST.get("title")
    description = request.POST.get("description")
    todos = Todo.objects.create(title=title,user=request.user,description=description)
    todos.save()
  todos = Todo.objects.filter(user=request.user) if request.user.is_authenticated else []
  context ={
    "todos":todos,
  }
  return render(request,"index.html",context)




@login_required
def delete_view(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if request.method == "POST":
        todo.delete()
        return redirect("/")  # Redirect to index after deletion
    return render(request, "index.html")





  
  
def signup(request):
  if request.method == "POST":
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    try:
      if User.objects.filter(username=username).first():
        messages.error(request,"username already ecists!")
        return redirect("/signup")
      if User.objects.filter(email=email).first():
        messages.error(request,"Email already ecists!")
        return redirect("/signup")
    
      user = User(username=username,email=email)
      user.set_password(password)
      user.save()
      messages.success(request,"Succesfully signup! please login to your account.")
      return redirect("/login")
    except Exception as e:
      print(e)
  return render(request,"signup.html")
  
  
  
  
  
def login_view(request):
  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = User.objects.filter(username=username).first()
    if user is None:
      messages.error(request,"email is not exists!")
      return redirect("/login")
    user = authenticate(username=username,password=password)
    if user is None:
      messages.error(request,"password is incorrect!")
      return redirect("/login")
    else:
      login(request,user)
      messages.success(request,"Succesfully login!")
      return redirect("/")
  return render(request,"login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')















@login_required
def update_todo(request, id):
    todos = get_object_or_404(Todo, id=id, user=request.user)
    
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        
        # Update the todo object
        todos.title = title
        todos.description = description
        todos.save()
        
        messages.success(request, "Todo updated successfully!")
        return redirect("/")  # Redirect to the index page after update
    
    context = {
        "todos": todos,
    }
    
    return render(request, "update_todo.html", context)
