from django.shortcuts import render

# Create your views here.
def home(request):
    # data = 'Gajendra kumar dave'
    context = {'home':'active'}
    return render(request,'core/home.html',context) ;
