from django.http import HttpRequest
from django.shortcuts import render,redirect,get_object_or_404
from accounts.models import Book
from django.contrib.auth.decorators import login_required




def home(request:HttpRequest)->None:
    all_books = Book.objects.all()
    return render(request,"index.html",{"books":all_books})


@login_required(login_url='login')
def add_book(request:HttpRequest)->None:
    if request.method == "POST":
        book_name = request.POST['book_name']
        book_desc = request.POST['book_desc']
        book_image = request.FILES['book_image']
        if book_name and book_desc and book_image:
            Book.objects.create(
                book_name=book_name,
                book_desc=book_desc,
                book_image=book_image
            )
            return redirect("home")
        
    return render(request,"book/add_book.html")



@login_required(login_url='login')
def edit_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == "POST":
        book_name = request.POST.get('book_name')
        book_desc = request.POST.get('book_desc')
        book_image = request.FILES.get('book_image')  

        book.book_name = book_name
        book.book_desc = book_desc

        if book_image:
            book.book_image = book_image   

        book.save()
        return redirect('home')

    return render(request, 'book/edit_book.html', {'book': book})



@login_required(login_url='login')
def delete_book(request:HttpRequest,pk:int)->None:
    book = get_object_or_404(Book,id=pk)
    if request.method == "POST":
        book.delete()
        return redirect("home")
    return render(request, 'book/delete_book.html', {'book': book})


