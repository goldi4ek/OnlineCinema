from django.shortcuts import render
from .models import Video

# Create your views here.
def index(request):
    video = Video.objects.all()
    return render(request, 'index.html', {"video": video})

def video_info(request, pk):
    context = {
        "video": Video.objects.get(pk=pk)
    }
    return render(request, 'video_page.html', context)