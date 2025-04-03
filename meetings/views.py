from django.shortcuts import render

def meenting_view(request):
    if request.method=='GET':
        return render(request, 'meentings.html')
