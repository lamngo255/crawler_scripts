import threading
from queue import Queue
from domain import get_domain_name
from spider import Spider


NUM_SPIDERS = 10
HOMEPAGE = 'https://twitter.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
Spider(DOMAIN_NAME, HOMEPAGE)
q = Queue()


# crawl the next url
def work():
    while True:
        url = q.get()
        Spider.crawl_page(threading.currentThread().name, url)
        q.task_done()


# Create spider threads (will be terminated when main exits)
def create_spiders():
    for x in range(NUM_SPIDERS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Each queued link is a new job
def create_jobs():
    for link in Spider.queue:
        q.put(link)
    q.join()
    crawl()


# Check if there are items in queue, if so crawl it
def crawl():
    if len(Spider.queue) > 0:
        print(str(len(Spider.queue)) + " links in the queue")
        create_jobs()

create_spiders()
crawl()
