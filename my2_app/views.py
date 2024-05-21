from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render,redirect
from .models import Book
from .forms import AuthorForm,BookForm
# Create your views here.

# def createBook(request):
#     books = Book.objects.all()
#
#     if request.method=='POST':
# 
#         title=request.POST.get('title')
#         price=request.POST.get('price')
#
#         book=Book(title=title,price=price)   #----first title stands for from the model and second one stands for the views.py name=title
#         book.save()
#
#     return render(request,'book.html',{'books':books})


def listBook(request):
    books=Book.objects.all()
    paginator =Paginator(books,4)
    page_number=request.GET.get('page')

    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'list.html',{'books':books,'page':page})


def detailsView(request,book_id):
    book=Book.objects.get(id=book_id)

    return render(request,'detailsview.html',{'book':book})



def updateBook(request,book_id):

    book=Book.objects.get(id=book_id)

    if request.method=='POST':
        form=BookForm(request.POST,request.FILES,instance=book)

        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form=BookForm(instance=book)

    return render(request,'update.html',{'form':form})

    # book=Book.objects.get(id=book_id)
    #
    # if request.method=='POST':
    #
    #     title=request.POST.get('title')
    #     price=request.POST.get('price')
    #
    #     book.title=title
    #     book.price=price
    #
    #     book.save()
    #
    #     return redirect('/')
    #
    # return render(request,'update.html',{'book':book})


def deleteView(request,book_id):

    book=Book.objects.get(id=book_id)

    if request.method=='POST':
        book.delete()

        return redirect('/')

    return render(request,'deleteview.html',{'book':book})

def createBook(request):
    books=Book.objects.all()

    if request.method=="POST":
        form=BookForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
        return redirect('/')

    else:
        form =BookForm()

    return render(request,'book.html',{'form':form,'books':books})

def create_Author(request):

    if request.method=='POST':
        form=AuthorForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')

    else:
        form=AuthorForm()

    return render(request,'author.html',{'form':form})

def index(request):
    return render(request,'base.html')


def search_Book(request):
    query=None
    books=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query))
    else:
        books=[]

    context={'books':books,'query':query}

    return render(request,'search.html',context)
