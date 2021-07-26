class LoadBalancer:

    url_set = set()

    def __init__(self, capacity):
        if capacity > 0:
            self.capacity = capacity
        else:
            self.capacity = 5

    def register_url(self, url):
        if url in self.url_set:
            return False
        if len(self.url_set) >= self.capacity:
            return False
        else:
            self.url_set.add(url)
            print('New length is {}'.format(len(self.url_set)))
            return True

