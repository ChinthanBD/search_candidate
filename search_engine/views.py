from django.shortcuts import render
from .search import search_candidates
from django.http import JsonResponse


def candidate_search(request):
    query = request.GET.get('query', '')
    results = search_candidates(query) if query else []
    response_data = {
        'results' : [{'id': candidate.id, 'name': candidate.name} for candidate in results]
    }
    return JsonResponse(response_data)