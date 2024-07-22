from .models import Candidate

def search_candidates(query):
    query_words = set(query.split())
    
    candidates = Candidate.objects.all()
    
    exact_matches = []
    partial_matches = []
    
    for candidate in candidates:
        candidate_words = set(candidate.name.split())
        
        if candidate_words == query_words:
            exact_matches.append(candidate)
        elif candidate_words & query_words:
            overlap_count = len(candidate_words & query_words)
            partial_matches.append((candidate, overlap_count))
            
    partial_matches.sort(key=lambda x: x[1], reverse=True)
    partial_matches = [candidate for candidate, _ in partial_matches]
    
    sorted_candidates = exact_matches + partial_matches
    
    return sorted_candidates