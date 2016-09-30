from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth.models import User
from registration.models import RegistrationProfile
from .forms import ContactForm,ProfileForm,DomainForm
from .models import Profile,Domain

def home(request):
    title = "Home"
    if request.user.is_authenticated():
        domain_list = []
        list = Domain.objects.filter(username = request.user).values()
        if list and not list[0]['domain'] == None:            
            domain_str = list[0]['domain'][1:-1]
            list = domain_str.split(", ")
            for i in list:
                domain_list.append(i[2:-1])
            print domain_list
        length = len(domain_list)
        if request.method == "POST":
            pre_field=request.POST['value']
            # data_list=[]
            # if length != 0:
            #     data = request.user.domain
            #     data = str(data)[1:-1]
            #     data_list=data.split(",")
            #     for i in range(len(data_list)):
            #         t=3
            #         if i==0:
            #             t=2
            #         data_list[i]=data_list[i][t:len(data_list[i])-1]
            # pre_field=str(pre_field)
            if pre_field in domain_list:
                domain_list.remove(pre_field)
            else:
                domain_list.append(pre_field)
            if len(domain_list) != 0 :
                # for i in range(len(data_list)) :
                #     data_list[i] = unicode(data_list[i],"utf-8")
                Domain.objects.filter(username=request.user).update(domain=domain_list)
        #     user=request.user
        #     domain=user.domain
        #     form=DomainForm(instance=domain)
        # else:
        user=request.user
        domain=user.domain
        form = DomainForm(instance = domain)
        context = {
            'list':  domain_list,
            'form':  form,
            'title': title,
            }
    else:
        context = {
            'title': title,
        }        
    return render(request,'home.html',context)

def check(request):
    if request.method == 'POST':
        return render(request,'check.html',{})

def contact(request):
    title = "Contact"
    form = ContactForm(None)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Customer queries"
            from_email = "shubham199541@gmail.com"
            to_email = "shubham.agrawal1906@gmail.com"
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']
            body = "Name: "+name+"\n"+"From: "+email+"\n"+"Meassage: "+message
            send_mail(subject,body,from_email,[to_email],fail_silently=True)
            print body
    context = {
        'form': form,
        'title': title,
    }   
    return render(request,'contact.html',context)

def about(request):
    title = "About"
    return render(request,'about.html',{'title': title})

@login_required
def profile(request):
    title="Profile"
    #print Profile.objects.all().filter(username = request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST,instance=request.user.profile)
        if form.is_valid():
            form.save()
    else:
        user = request.user
        profile = user.profile
        form = ProfileForm(instance = profile)
    context = {
        'title':title,
        'form':form,
        } 
    return render(request,"profile.html",context)

@login_required
def setting(request):
    title = "Setting"
    context = {
        'title': title,
    }
    return render(request,'setting.html',context)

@login_required
def domain(request):
    title = "Domain"
    title = request.GET.get('title')
    domain_list = []
    list = Domain.objects.filter(username = request.user).values()    
    if list and not list[0]['domain'] == None:
        domain_str = list[0]['domain'][1:-1]
        list = domain_str.split(", ")
        for i in list:
            domain_list.append(i[2:-1])
    details_list = []
    details_list = Profile.objects.all().filter(firstname__icontains="shubham").values()
    paginator = Paginator(details_list, 1)
    page = request.GET.get('page')
    try:
        details = paginator.page(page)
    except PageNotAnInteger:
        details = paginator.page(1)
    except EmptyPage:
        details = paginator.page(paginator.num_pages)
    context = {
        'details': details,
        'list': domain_list,
        'title': title,
    }
    return render(request,'domain.html',context)