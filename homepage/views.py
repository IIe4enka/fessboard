from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from .models import *
from .forms import *


def createCompany(request):
    form = CompanyForm(request.POST or None)
    if request.method == 'POST':
        form.save()
        messages.success(request, "Form saved successfully!")
        return HttpResponseRedirect('/company-hub/')
    else:
        form = CompanyForm()
    return render(request, 'index.html', {'form': form})


def updateCompany(request, pk):
    company = Company.objects.get(company_id=pk)
    form = CompanyForm(instance=company)

    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/company-hub/')

    context = {'form': form, 'company': company}
    return render(request, 'index.html', context)


def deleteCompany(request, pk):
    company = Company.objects.get(company_id=pk)
    context = {'item': company}
    if request.method == 'POST':
        company.delete()
        return HttpResponseRedirect('/company-hub/')
    return render(request, 'delete.html', context)


def companyHub(request):
    context = {'Company': Company.objects.all()}
    return render(request, 'company_hub.html', context)


def student_view(request):
    form = StudentsForm(request.POST or None)
    if request.method == 'POST':
        form.save()
        messages.success(request, "Form saved successfully!")
        return HttpResponseRedirect('/')
    else:
        form = StudentsForm()
    return render(request, 'index.html', {'form': form})


def project_view(request):
    form = ProjectForm(request.POST or None)
    if request.method == 'POST':
        form.save()
        messages.success(request, "Form saved successfully!")
        return HttpResponseRedirect('/')
    else:
        form = ProjectForm()
    return render(request, 'index.html', {'form': form})


def homepage(request):
    return render(request, 'main.html')


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        formset = forms.formset_factory(StudentForm, formset=StudentFormSet, extra=0, can_delete=True)
        formset = formset(request.POST, prefix='students')
        if form.is_valid() and formset.is_valid():
            project = form.save()
            for student_form in formset:
                student = student_form.cleaned_data['student']
                group_number = student_form.cleaned_data['group_number']
                item = Amogus(project=project, student=student, group=group_number)
                item.save()
            return redirect('/')

    else:
        form = ProjectForm()
        formset = StudentFormSet()
    return render(request, 'add_project.html', {'form': form, 'formset': formset})
