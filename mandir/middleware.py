"""
Cache-control middleware.

For HTML responses, send no-cache headers so the browser always re-fetches
the page (and thus picks up the latest version-stamped static URLs inside).

Static assets (.css, .js, images) are NOT touched here — they're served by
the static handler and benefit from long-lived caching plus the `?v=...`
query string for cache busting.
"""


class NoCacheHTMLMiddleware:
    """Sets no-cache headers on text/html responses."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        content_type = response.get('Content-Type', '')
        # Only touch dynamic HTML — leave static files alone
        if 'text/html' in content_type:
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate, private'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
        return response
