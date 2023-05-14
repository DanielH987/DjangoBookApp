from .models import Book
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.views.generic.edit import FormView
from .forms import BookIdForm

# Create your views here.
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookFormView(FormView):
    template_name = 'book_form.html'
    form_class = BookIdForm
    success_url = '/books/'

    def form_valid(self, form):
        book_id = form.cleaned_data['book_id']
        return redirect('book-detail', pk=book_id)

class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class HomeView(APIView):
    def get(self, request):
        return render(request, 'base.html')