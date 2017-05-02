from django.http import QueryDict
from django.template import loader
from django.forms.models import modelform_factory
from django.http import HttpResponse, JsonResponse
from .models import Film, FilmForm

def index(request):
	template = loader.get_template('./index.html')
	return HttpResponse(template.render({}, request))

def data(request, id):
	#get all data
	if request.method == 'GET':
		films = Film.objects.all();
		data = [{
			'id' : item.pk, 'votes': item.votes,
			'title': item.title, 'year': item.year,
			'rating': item.rating, 'rank': item.rank
		} for item in films]
		return JsonResponse(data, safe = False)

	#insert
	if request.method == 'POST':
		modelform = modelform_factory(Film, FilmForm)
		form = modelform(request.POST)
		if form.is_valid():
			obj = form.save()
			return JsonResponse({ 'id':obj.pk })
		else:
			return JsonResponse({ 'status':"error" })

	#update
	elif request.method == 'PUT':
		modelform = modelform_factory(Film, FilmForm)
		film = Film.objects.get(pk=id)
		form = modelform(QueryDict(request.body), instance=film)
		if form.is_valid():
			form.save()
			return JsonResponse({ })
		else:
			return JsonResponse({ 'status':"error" })


	#delete
	elif request.method == 'DELETE':
		Film.objects.get(pk=id).delete()
		return JsonResponse({ })
