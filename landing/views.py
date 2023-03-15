from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect

# Create your views here.
class Index(View):
    def get(self,request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/global')
        return render(request,'landing/index.html')
