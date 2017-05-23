from Bio import Entrez

def search(query):
    Entrez.email = 'f00b48005@ntu.edu.tw'
    handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax='50',
                            retmode='xml', 
                            term=query)
    results = Entrez.read(handle)
    return results

def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'f00b48005@ntu.edu.tw'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results


if __name__ == '__main__':
    results = search('(“genome-wide association” OR “Genomewide Association” OR “Genome wide Association” )and ((“response” and “drug”) or (“drug” and “level”) or (“ drug” and “plasma”) or (“pharmacogenomic”) or ( “treatment” and “drug”) ) ')
    id_list = results['IdList']
    print(len(id_list))
    papers = fetch_details(id_list)
    print('Title\tPMID\tAuthor\tJournal\tDate\tAbstract\tLink')
    for data in papers['PubmedArticle']:
        record = data['MedlineCitation']
        pmid = record['PMID']
        fauth_name = record['Article']['AuthorList'][0]['ForeName'] + " " + \
                     record['Article']['AuthorList'][0]['LastName']
        article_date = ""
        if len(record['Article']['ArticleDate']) > 0:
            date = record['Article']['ArticleDate']
            article_date = date[0]['Year'] + date[0]['Month'] + date[0]['Day']
        journal = record['Article']['Journal']['ISOAbbreviation']
        link = "https://www.ncbi.nlm.nih.gov/pubmed/" + pmid
        study = record['Article']['ArticleTitle']
        abstract = ""
        if 'Abstract' in record['Article']:
            abstract = record['Article']['Abstract']['AbstractText'][0]
        print('%s\t%s\t%s\t%s\t%s\t%s\t%s' % (study, pmid, fauth_name, journal, article_date, abstract, link))
    # Pretty print the first paper in full
    # import json
    # print(json.dumps(papers, indent=1, separators=(',', ':')))
