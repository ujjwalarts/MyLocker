from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Document, SharedDocument
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

#Upload Document Page
@login_required
def upload_page(request):
    if request.method == 'POST':
        title = request.POST.get('title')  
        file = request.FILES.get('file')  

        if title and file:
            document = Document(
                title=title,
                file=file,
                user=request.user
            )
            document.save()
            messages.success(request, 'Document uploaded successfully!')
            return redirect('documents') 
        else:
            messages.error(request, 'Error uploading document. Please ensure all fields are filled.')

    return render(request, 'upload.html')

# Homepage
def home(request):
    return render(request, 'home.html')

# Document List Page
@login_required
def document_list_page(request):
    documents = Document.objects.filter(user=request.user)
    return render(request, 'documents.html', {'documents': documents})

# Document Access Page
def access_page(request):
    return render(request, 'access.html')

# Signup view
def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Signup successful! You can now log in.")
        return redirect('login')
    
    return render(request, 'signup.html')

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')
    
    return render(request, 'login.html')

# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('/')

@login_required
def verify_document(request, pk):
    document = get_object_or_404(Document, pk=pk, user=request.user)
    # add logic for verification from api
    document.verified = True
    document.save()
    messages.success(request, f"Document '{document.title}' has been verified successfully!")
    return redirect('documents')

from django.http import FileResponse, Http404
from mimetypes import guess_type

@login_required
def view_document(request, pk):
    document = get_object_or_404(Document, pk=pk, user=request.user)
    try:
        file = document.file.open()
        mime_type, _ = guess_type(document.file.name)

        return FileResponse(file, content_type=mime_type)
    except FileNotFoundError:
        raise Http404("Document not found.")
