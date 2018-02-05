from multiprocessing import pool
import bs4 as bs
import random
import requests
import string

#generating random url

def random_url():
    start = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
    url = ''.join(['http://',start,'.com'])
    return url


#handling link

def handle_link(url,link):
    if link.startwith('/'):
        return ''.join([url,link])
    else:
        return link

def get_link(url):
    try:
        res = requests.get(url)
        soup = bs.BeautifulSoup(res.text, 'lxml')
        body = soup.body
        links = [link.get('href') for link in body.find_all('a')]
        links = [handle_link(url,link) for link in links]
        links = [str(link.encode('ascii')) for link in links]
        return links
    except TimeoutError as e:
        print(e)
        print('Got a TypeError, probably got a None that we tried to iterate over')
        return []
    except IndexError as e:
        print(e)
        print('We probably did not find any useful links')
        return []
    except AttributeError as e:
        print(e)
        print('Likely got None links, so we are throwing this')
    except Exception as e:
        print(str(e))


def main():
    how_many = 50
    p = pool(processes=how_many)
    parse_us = [random_url() for _ in range(how_many)]
    data = p.map(get_link ([link for link in parse_us]))
    data = [url for url_list in data for url in url_list]
    p.close()

    with open('links.txt', 'w') as f:
        f.write(str(data))


if __name__ == '__main__':
    main()


