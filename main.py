from fastapi import FastAPI, Query
import json
from typing import List, Dict
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Diretório contendo os essays
essay_dir = "essays/"
documents = []
titles = []

for filename in os.listdir(essay_dir):
    if filename.endswith(".txt"):
        with open(os.path.join(essay_dir, filename), 'r', encoding='utf-8') as file:
            documents.append(file.read())
            titles.append(filename.replace('.txt', ''))

# Vetorização TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)

def search_tfidf(query, top_n=10):
    query_vec = vectorizer.transform([query])
    cosine_similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    
    # Filtragem para manter apenas relevância > 0.095 de acordo com testes de validação
    relevant_indices = np.where(cosine_similarities > 0.095)[0]
    
    # Ordenação dos documentos por relevância (similaridade)
    sorted_indices = relevant_indices[np.argsort(-cosine_similarities[relevant_indices])[:top_n]]
    
    results = []
    for idx in sorted_indices:
        results.append({
            'title': titles[idx],
            'content': documents[idx][:500],
            'relevance': cosine_similarities[idx]
        })
    
    return results


app = FastAPI()

@app.get("/query")
def get_query(query: str = Query(...)) -> dict:
    results = search_tfidf(query)
    return {
        'results': results,
        'message': 'OK' if results else 'No results found'
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)
