import arxiv 
def search_papers(query, max_results=5):
    """
    Search ArXiv for scientific papers using a search query
    """

    client=arxiv.Client()

    search=arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    papers=[]
    for result in client.results(search):
        paper={
            "title": result.title,
            "authors":[author.name for author in result.authors],
            "published":result.published.strftime("%Y-%m-%d"),
            "abstract":result.summary,
            "url":result.entry_id,
            "pdf_url":result.pdf_url,
            "category":result.primary_category
        }
        papers.append(paper)
    return papers

if __name__=="__main__":
    results=search_papers("machine learning", max_results=5)
    for i, paper in enumerate(results,start=1):
        print(f"\nPaper {i}")
        print("-"*50)

        print("Title:",paper["title"])
        print("Authors:",",".join(paper["authors"]))
        print("Published:",paper["published"])
        print("Category:", paper["category"])
        print("URL:", paper["url"])
        print("Abstract:", paper["abstract"][:500], "...")