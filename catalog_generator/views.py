from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from .models import Book
from .forms import BookForm
import csv
from django.shortcuts import get_object_or_404
from django.urls import reverse

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    books = Book.objects.all()
    return render(request, 'user_profile.html', {'form': form, 'books': books})


def generate_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="book_catalog.csv"'

    writer = csv.writer(response)
    writer.writerow(['Book ID', 'Title', 'Author', 'Publication Year'])

    books = Book.objects.all()
    for book in books:
        writer.writerow([book.id, book.title, book.author, book.year])

    return response

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    return render(request, 'confirm_delete.html', {'book': book})

def generate_pdf(request):
    response = FileResponse(generate_pdf_file(), as_attachment=True, filename='book_catalog.pdf')
    return response

def generate_pdf_file():
    from io import BytesIO

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    books = Book.objects.all()
    p.drawString(100, 750, "Book Catalog")

    y = 700
    for book in books:
        p.drawString(100, y, f"Book ID: {book.id}")
        p.drawString(100, y-20, f"Title: {book.title}")
        p.drawString(100, y - 40, f"Author: {book.author}")
        p.drawString(100, y - 60, f"Published Year: {book.year}")
        y -= 120

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})