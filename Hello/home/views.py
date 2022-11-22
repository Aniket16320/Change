from django.shortcuts import render,HttpResponseRedirect
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    data = Contact.objects.all()
    if request.method== 'GET':
        st = request.GET.get('searchname')
        if st!=None:
            data =  Contact.objects.filter(name__icontains=st)
    # for a in data:
    #    print(a.name)
    Contact_data = {
        'ContactData':data
    }
    return render(request, 'index.html', Contact_data)
def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')
    
def contact(request):
    if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone') 
      desc = request.POST.get('desc') 
      contact = Contact(name=name, email=email, phone=phone,desc=desc)
      contact.save()
      return HttpResponseRedirect('/')
    return render(request, 'contact.html')
   

def  delete_data(request, id):
    if request.method == "POST":
        pi= Contact.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def update_data(request, id):
    user = Contact.objects.get(id=id)
    user.save()
    return render(request, 'update.html', {'user':user})

# def edit(request, id):
#     user= Contact.objects.get(id=id)
#     form = Contact(request.POST, instance=user)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect('/')
#     return render(request,'update.html',{'user':user} )







