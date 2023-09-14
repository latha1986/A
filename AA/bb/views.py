from django.shortcuts import render,redirect
from bb.forms import EF
def emp(request):
    if request.method=="POST":
        form=EF(request.POST)
        if form.is_valid():
            employee_instance=form.save()
            return redirect("sucess_page")
    else:
        form=EF()
    return render(request,'index.html',{'form':form})
def success_view(request):
    return render(request,'success.html')


