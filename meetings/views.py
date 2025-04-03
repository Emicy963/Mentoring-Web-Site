from django.shortcuts import render

def meeting_view(request):
    if request.method=='GET':
        return render(request, 'meentings.html')
