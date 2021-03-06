from django.shortcuts import render, redirect

import datetime
from .models import Predict
# from .forms import PredictForm
# from bs4 import BeautifulSoup
# import requests
# import urllib


# Create your views here.
def index(request):
    # OLD MODELS
    #
    # if request.method == 'POST':
    #     form = PredictForm(request.POST)
    #     if form.is_valid():
    #         obj = form.save(commit=False)
    #         obj = update(obj)
    #         obj.audience_num = movie_serve.predict(obj.rating_before, obj.rating_after, obj.num_news, obj.distributor)
    #         obj.save()
    #
    #         return redirect('/')
    #
    # form = PredictForm()

    today = datetime.date.today()
    now_predicts = Predict.objects.filter(closed=0).filter(release_day__lt=today)
    for p in now_predicts:
        p.audience_num = format(p.audience_num, ',')

    before_predicts = Predict.objects.filter(closed=0).filter(release_day__gt=today)
    for p in before_predicts:
        p.audience_num = format(p.audience_num, ',')

    end_predicts = Predict.objects.filter(closed=1)
    for p in end_predicts:
        p.audience_num = format(p.audience_num, ',')
        p.audience_num_real = format(p.audience_num_real, ',')

    ctx = {'now_predicts': now_predicts, 'before_predicts': before_predicts, 'end_predicts': end_predicts}
    return render(request, 'predicts/index.html', ctx)


def serve(request, predict_id):
    from new_models import Serve

    obj = Predict.objects.get(id=predict_id)
    obj.audience_num = Serve.SMOreg(obj)
    obj.audience_class = Serve.SimpleLogistic(obj)
    obj.save()

    return redirect("/")

# OLD MODELS
#
# def update(obj):
#     r = requests.get(obj.url.replace('basic', 'point'))
#     soup = BeautifulSoup(r.text)
#
#     print(soup.select(".h_movie a")[0].text)
#     obj.title = soup.select(".h_movie a")[0].text
#
#     obj.image_url = soup.select(".poster img")[0]['src']
#
#     # 개봉 전 평점
#     try:
#         rating_before = ""
#         for e in soup.find(id="beforePointArea").find(class_="star_score").find_all("em"):
#             rating_before += e.text
#         obj.rating_before = rating_before
#     except:
#         obj.rating_before = 5.0
#
#     # 개봉 후 평점
#     try:
#         rating_after = ""
#         for e in soup.find(id="netizen_point_tab_inner").find(class_="star_score").find_all("em"):
#             rating_after += e.text
#         obj.rating_after = rating_after
#     except:
#         obj.rating_after = obj.rating_before
#
#     r = requests.get("https://search.naver.com/search.naver?where=news&query=영화+" + urllib.parse.quote(
#         obj.title))
#     soup = BeautifulSoup(r.text)
#
#     # 뉴스 기사 수
#     try:
#         obj.num_news = soup.select(".all_my")[0].text[7:-1].replace(',', '')
#     except:
#         pass
#
#     return obj
