class SimpleURLShortener:
    def __init__(self):
        self.url_map = {}
        self.counter = 1

    def shorten_url(self, long_url):
        short_url = f'short/{self.counter}'  # Example: short/1, short/2, etc.
        self.url_map[short_url] = long_url
        self.counter += 1
        return short_url

    def resolve_url(self, short_url):
        return self.url_map.get(short_url, None)

# Example usage
url_shortener = SimpleURLShortener()

long_url = 'https://google.com'
short_url = url_shortener.shorten_url(long_url)

print(f'Shortened URL: {short_url}')

# Resolve the shortened URL
resolved_url = url_shortener.resolve_url(short_url)
print(f'Resolved URL: {resolved_url}')
