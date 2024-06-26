import requests
import pandas as pd
import argparse

def get_query(query, max_results = None):
    url = f'http://export.arxiv.org/api/query?search_query={query}'
    if max_results:
        url += f'&max_results={max_results}'
    res = requests.get(url)
    return res

def main(args):
    dates = pd.date_range(start=args['datefrom'], end=args['dateto'], freq='ME')
    res = []
    for date in dates:
        submittedDate = f"[{date.strftime('%Y%m%d%H%M')} TO {(date + pd.DateOffset(months=1)).strftime('%Y%m%d%H%M')}]"
        arxivs = get_query(' AND '.join([args['query'], f'submittedDate:{submittedDate}']), args.get('n'))
        res.append((date, arxivs.text))
    print(*res, sep = '\n')
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--datefrom', type=str)
    parser.add_argument('--dateto', type=str)
    parser.add_argument('--query', type=str)
    parser.add_argument('--n', type=int, required=False)

    args = vars(parser.parse_args())
    main(args)