class Router:
    def __init__(self):
        self.routes = {}

    def bind(self, url, method, action):
        self.routes[(url, method)] = action

    def runRequest(self, url, method):
        if (url, method) in self.routes:
            return self.routes[(url, method)]()
        else:
            return 'Error 404: Not Found'


if __name__ == "__main__":
    router = Router()
    router.bind('/hello', 'GET', lambda: 'hello world')
    print(router.runRequest('/hello', 'GET'))
    print(router.runRequest('/hell', 'GET'))



