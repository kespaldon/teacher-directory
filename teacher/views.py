from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponseRedirect
from django.shortcuts import render

from listing.forms import ListingUploadForm
from listing.models import Teacher
from listing.utils.csv import process_import


def index(request):
    teachers = Teacher.objects.all()
    # teachers = serializers.serialize('json', queryset)
    context = dict(
        teachers=teachers
    )

    return render(request, 'index.html', context)


@login_required
def import_data(request):
    context = {}
    if request.method == 'GET':
        context['form'] = ListingUploadForm()
    else:
        form = ListingUploadForm(request.POST, request.FILES)
        if form.is_valid():
            success, count = process_import(request.FILES['file'])
            if success:
                messages.success(
                    request,
                    f'Uploaded successfully. {count} uploaded'
                )
            else:
                messages.error(
                    request,
                    f'Error in upload, {count} uploaded'
                )
            return HttpResponseRedirect('/')

    return render(request, 'import.html', context)
