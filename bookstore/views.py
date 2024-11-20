from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.mixins import PassRequestMixin
from .models import User, Book, Chat, DeleteRequest, Feedback
from django.contrib import messages
from django.db.models import Sum
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
# from .forms import ChatForm, BookForm, UserForm
from . import models
import operator
import itertools
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, logout
from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def login_form(request):
	return render(request, 'bookstore/login.html')

def logoutView(request):
	logout(request)
	return redirect('home')

def loginView(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			if user.is_admin or user.is_superuser:
				return redirect('dashboard')
			elif user.is_librarian:
				return redirect('librarian')
			else:
			    return redirect('publisher')
		else:
		    messages.info(request, "Invalid username or password")
		    return redirect('home')
		
def logoutView(request):
	logout(request)
	return redirect('home')

def register_form(request):
	return render(request, 'bookstore/register.html')


def registerView(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password = make_password(password)

		a = User(username=username, email=email, password=password)
		a.save()
		messages.success(request, 'Compte cree avec succes')
		return redirect('home')
	else:
	    messages.error(request, 'Inscription echoue')
	    return redirect('regform')
		








def publisher(request):
	return redirect('publisher/home.html')


def uabook_form(request):
	return render(request, 'publisher/add_book.html')

def uabook(request):
	if request.method == 'POST':
		title = request.POST['title']
		author = request.POST['author']
		year = request.POST['year']
		publisher = request.POST['publisher']
		desc = request.POST['desc']
		cover = request.FILES['cover']
		pdf = request.FILES['pdf']
		current_user = request.user
		user_id = current_user.id
		username = current_user.username

		a = Book(title=title, author=author, year=year, publisher=publisher, 
			desc=desc, cover=cover, pdf=pdf, uploaded_by=username, user_id=user_id)
		a.save()
		messages.success(request, 'Le memoire a ete telecharger avec succes')
		return redirect('publisher')
	else:
	    messages.error(request, "Le memoire n'a pas ete telecharger avec succes")
	    return redirect('uabook_form')	
	

class UBookListView(ListView):
	model = Book
	template_name = 'publisher/book_list.html'
	context_object_name = 'books'
	paginate_by = 4

	def get_queryset(self) :
		return Book.objects.order_by('-id')








def librarian(request) :
	return render(request, 'librarian/home.html')


def dashboard(request):
	book = Book.objects.all().count()
	user = User.objects.all().count()

	context = {'book':book, 'user':user}

	return render(request, 'dashboard/home.html', context)


def aabook_form(request):
	return render(request, 'dashboard/add_book.html')

def aabook(request):
	if request.method == 'POST':
		title = request.POST['title']
		author = request.POST['author']
		departement = request.POST['departement']
		filiere = request.POST['filiere']
		encadrant = request.POST['encadrant']
		year = request.POST['annee']
		current_user = request.user
		user_id = current_user.id
		username = current_user.username

		a = Book(title=title, author=author, departement=departement, filiere=filiere,encadrant =encadrant,year = year,
			 uploaded_by=username, user_id=user_id)
		a.save()
		messages.success(request, 'Book was uploaded successfully')
		return redirect('albook')
	else:
	    messages.error(request, 'Book was not uploaded successfully')
	    return redirect('aabook_form')
	

class ABookListView(LoginRequiredMixin,ListView):
	model = Book
	template_name = 'dashboard/book_list.html'
	context_object_name = 'books'
	paginate_by = 3

	def get_queryset(self):
		return Book.objects.order_by('-id')
		


