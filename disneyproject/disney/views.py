from django.shortcuts import render,redirect,get_object_or_404
from .models import Name,Disney
from .forms import NameForm
# Create your views here.
def post(request):
    if request.method=="POST":
        form=NameForm(request.POST)
        if form.is_valid():
            name=form.save(commit=False)
            name.save()
            return redirect('show')
    else:
        form=NameForm()
        return render(request,'show.html',{'form':form})

def show(request):
    name=Name.objects.order_by('-id').first()
    disney=Disney.objects.order_by("?").first()
    return render(request,'result.html',{'disney':disney,'name':name})