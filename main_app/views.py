from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import ImageHistory
from .forms import ImageUploadForm
from .ai_caption import generate_caption

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def upload_image(request):
    caption = None
    current_image = None
    
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img_instance = form.save(commit=False)
            img_instance.user = request.user
            img_instance.save()
            
            # Generate AI Caption
            full_path = img_instance.image.path
            caption = generate_caption(full_path)
            
            # Update DB
            img_instance.caption = caption
            img_instance.save()
            current_image = img_instance
    else:
        form = ImageUploadForm()

    history = ImageHistory.objects.filter(user=request.user).order_by('-created_at')[:5]

    return render(request, 'upload.html', {
        'form': form, 
        'caption': caption, 
        'current_image': current_image, 
        'history': history
    })
