from django.shortcuts import render
from googleapiclient.discovery import build
from django.contrib.auth.decorators import login_required

@login_required
def search_videos(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        youtube = build('youtube', 'v3', developerKey='AIzaSyCMDuU3lbod62Vc0ftjYuAXsij3rxjVTOw')
        search_response = youtube.search().list(
            q=query,
            part='snippet',
            type='video',
            maxResults=10
        ).execute()
        videos = search_response['items']
        return render(request, 'search_results.html', {'videos': videos})
    
    return render(request, 'search_form.html')

