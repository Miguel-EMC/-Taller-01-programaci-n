import json
import sys
from collections import defaultdict

def calculate_h_index(citations):
    citations.sort(reverse=True)
    h_index = 0
    for i, citation_count in enumerate(citations, start=1):
        if citation_count >= i:
            h_index = i
    return h_index

input_data = sys.stdin.read().strip().split('\n')
N = int(input_data[0])
    
author_info = defaultdict(list)

for i in range(1, N + 1):
    article_data = json.loads(input_data[i])
    authors = article_data.get('authors', {}).get('authors', [])
    citation_count = article_data.get('citing_paper_count', 0)
        
    for author in authors:
        author_name = author.get('full_name', 'Unknown')
        author_info[author_name].append(citation_count)
    
authors_h_index = []

for author, citations in author_info.items():
    h_index = calculate_h_index(citations)
    authors_h_index.append((author, h_index))
    
authors_h_index.sort(key=lambda x: (-x[1], x[0]))
    
for author, h_index in authors_h_index:
    print(f"{author} {h_index}")