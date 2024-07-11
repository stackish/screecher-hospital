from django.shortcuts import render,reverse,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from App.models import Patient
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from App.models import Patient




#=================  FRONTEND ============== #
# Create your views here.

#function to render the homepage
def frontend(request):
    template_name = "App/frontend.html"
    return render(request,template_name)





# ==========================================
#                    BACKEND
# ==========================================
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="login")
def backend(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_patient_list = Patient.objects.filter(
            Q(name__icontains=q) | Q(email__icontains=q) | Q(phone=q) | Q(age=q) | Q(gender=q) | Q(note=q)
        ).order_by('-created_at')

    else:
        all_patient_list = Patient.objects.all().order_by('-created_at')

    paginator = Paginator(all_patient_list, 5)
    page = request.GET.get('page')
    all_patient = paginator.get_page(page)
    template_name = "App/backend.html"
    context ={"patients":all_patient}
    return render(request,template_name,context)

#Function to insert patient
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="login")
def add_patient(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('age') and request.POST.get('gender') or request.POST.get('note'):
            patient = Patient()
            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')
            patient.save()
            messages.success(request,"Patient added successfully!")
            return HttpResponseRedirect(reverse('backend'))
    template_name ="App/add.html"
    return render(request,template_name)



#Function to delete patient

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="login")
def delete_patient(request,patient_id):
    patient = Patient.objects.get(id = patient_id)
    patient.delete()
    messages.success(request,"Patient removed successfully!!")
    return HttpResponseRedirect(reverse("backend"))


#function to access the patient individually
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url ="login")
def patient(request,patient_id):
    patient = Patient.objects.get(id = patient_id)
    if patient != None:
        template_name ="App/edit.html"
        context = {"patient":patient}
        return render(request,template_name,context)




#function to edit the patient 
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="login")
def edit_patient(request,patient_id):
    if request.method == "POST":
        patient = Patient.objects.get(id = request.POST.get('id'))
        if patient != None:
            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')
            patient.save()
            messages.success(request,"Patient updated successfully!!")
            return HttpResponseRedirect(reverse('backend'))
            




