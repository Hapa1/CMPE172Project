from django.shortcuts import render

def salaries_new(request):
    if request.method == "POST":
        form = SalariesForm(request.POST)
        if form.is_valid():
            salary = form.save(commit=False)
            salary.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #else:
    #    form = SalariesForm()
    #return render(request, 'blog/set_new.html', {'form': form})

# Create your views here.
