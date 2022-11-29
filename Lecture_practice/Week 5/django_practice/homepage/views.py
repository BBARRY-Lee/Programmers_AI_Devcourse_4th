from django.shortcuts import HttpResponse, render
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def index(request):
    #return HttpResponse("<h1>Hello World!</h1>")
    # render : 데이터를 바탕으로 완성한다는 의미에 가까움 # {} -> data
    # number = 50
    # name = "Jiyun"
    nums = [1, 2, 3, 4, 5]
    return render(request, 'index.html', {"my_list" : nums } )

def coffee_view(request):
    coffee_all = Coffee.objects.all() # .get(), filter()로 데이터 일부만 가져올 수도 있음
    # 만약, request가 POST라면 POST를 바탕으로 Form을 완성하고,
    # Form이 유효하면 저장
    if request.method == "POST":
        form = CoffeeForm(request.POST) # 완성된 Form

        if form.is_valid(): # 값이 유효하면,
            form.save() # Form 내용을 Model에 저장
    
    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list": coffee_all, "coffee_form" : form})

