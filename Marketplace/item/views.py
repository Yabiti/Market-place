from django.shortcuts import render, get_object_or_404

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(item, pk=pk)