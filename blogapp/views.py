from django.shortcuts import render
from blogapp.forms import FormFill
from blogapp.models import Post
# Create your views here.
def homepage(request):
    name = Post.objects.order_by('date_published')
    dict = {'name':name}
    return render(request, 'blogapp/home.html', context = dict)



def formpage(request):

    forms = FormFill()

    if request.method == 'POST':
        form = FormFill(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'blogapp/form.html', {'forms':forms})
