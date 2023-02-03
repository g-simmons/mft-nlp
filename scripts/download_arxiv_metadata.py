import arxiv
import yaml

def get_paper_metadata(arxiv_id):
    search = arxiv.Search(id_list=[arxiv_id])
    results = list(search.results())
    if len(results) > 0:
        paper = results[0]
        print(paper)
        data = {
            'title': paper.title,
            'authors': [author.name  for author in paper.authors],
            'abstract': paper.summary,
            'published': paper.published,
        }
        return yaml.dump(data, default_flow_style=False)
    else:
        print("No results found for arXiv ID: {}".format(arxiv_id))
        return None

arxiv_id = input("Enter an arXiv ID: ")
print(get_paper_metadata(arxiv_id))
