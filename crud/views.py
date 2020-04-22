from django.shortcuts import render,redirect
from crud.forms import EmployeeForm
from crud.models import Employee
import re
def emp(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        employees = Employee.objects.all()
        dict=[]
        for employee in employees:
            dict.append(employee.eid)

        if form.is_valid() and form.data['eid'] in dict:
            return render(request,"eid.html",{'form':form})
        if form.is_valid() and len(form.data['econtact'])==10 and re.search(regex,form.data['eemail'])!=None:
            try:
                form.save()
                return redirect("/show")
            except:
                pass
        else:
            return render(request,"error.html",{'form':form})
    else:
        form=EmployeeForm()
    return render(request,"index.html",{'form':form})

def show(request):
    employees= Employee.objects.all()
    return render(request,"show.html",{'employees':employees})

def edit(request,id):
    employee =Employee.objects.get(id=id)
    return render(request,"edit.html",{'employee':employee})

def update(request,id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,"edit.html",{'employee':employee})

def delete(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")