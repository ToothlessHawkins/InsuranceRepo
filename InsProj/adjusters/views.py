from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

"""IMPORT W/E YOU NEED TO GET USERNAME"""

from .models import Adjuster
# from .forms import productForm

# display a page that shows adjuster name, as well as details about the case they are currently working
def home(request):
    adjuster_details = Adjuster.objects.get(pk=user.username)
    return render(request, 'adjusters/home.html', {'adjuster_details': adjuster_details})

# def case_feedback(request, e_num):
#     employee = get_object_or_404(Employee, number=e_num)
#     job_list = Job.objects.filter(employee__number=e_num)
#     print(job_list)
#     return render(request, 'employees/details.html', {'employee': employee, 'job_list': job_list})