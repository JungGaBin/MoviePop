from django.shortcuts import render, redirect

from .forms import PredictForm
from .models import Predict
import movie_serve


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = PredictForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.num_viewers = movie_serve.predict(obj.rating, obj.distributor)
            obj.save()

            return redirect('/')

    form = PredictForm()
    predicts = Predict.objects.order_by("-id")
    ctx = {'form': form, 'predicts': predicts}
    return render(request, 'predicts/index.html', ctx)
