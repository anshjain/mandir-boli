"""
Context processors for templates.

`static_version` returns a short string that can be appended to static file
URLs as `?v={{ static_version }}` to force browsers to re-download CSS/JS
after a deploy.

It uses, in order of preference:
  1. settings.STATIC_VERSION  (set this in settings.py or via env var)
  2. The mtime of the project root directory (auto-bumps when files change)
"""
import os
from django.conf import settings


_CACHED_VERSION = None


def _compute_default_version():
    """Use the latest mtime of key static dirs as a fallback version."""
    try:
        candidates = []
        for sub in ('static', 'media'):
            p = os.path.join(settings.BASE_DIR, sub)
            if os.path.isdir(p):
                candidates.append(int(os.path.getmtime(p)))
        return str(max(candidates)) if candidates else 'dev'
    except Exception:
        return 'dev'


def static_version(request):
    """Return {'static_version': '<token>'} for use in templates."""
    global _CACHED_VERSION
    if _CACHED_VERSION is None:
        _CACHED_VERSION = (
            getattr(settings, 'STATIC_VERSION', None)
            or os.environ.get('STATIC_VERSION')
            or _compute_default_version()
        )
    return {'static_version': _CACHED_VERSION}
