from gmag.settings.__debug import *





SECURE_SSL_REDIRECT=os.environ.get("SECURE_SSL_REDIRECT")
SESSION_COOKIE_SECURE=os.environ.get("SESSION_COOKIE_SECURE")
CSRF_COOKIE_SECURE=os.environ.get("CSRF_COOKIE_SECURE")
