from django.views.decorators.http import require_safe
from django.shortcuts import render


@require_safe
def index(request):
    return render(request, "home.jinja")
