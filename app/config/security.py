# Security configurations
SECURITY_CONFIG = {
    'PERMANENT_SESSION_LIFETIME': 1800,  # 30 minutes
    'SESSION_COOKIE_SECURE': True,
    'SESSION_COOKIE_HTTPONLY': True,
    'SESSION_COOKIE_SAMESITE': 'Lax',
    'REMEMBER_COOKIE_SECURE': True,
    'REMEMBER_COOKIE_HTTPONLY': True,
    'REMEMBER_COOKIE_DURATION': 3600  # 1 hour
}

# CSP Headers
CSP_HEADERS = {
    'default-src': "'self'",
    'script-src': "'self' 'unsafe-inline' 'unsafe-eval' cdn.jsdelivr.net cdnjs.cloudflare.com code.jquery.com",
    'style-src': "'self' 'unsafe-inline' cdn.jsdelivr.net cdnjs.cloudflare.com",
    'img-src': "'self' data: https:",
    'font-src': "'self' cdn.jsdelivr.net cdnjs.cloudflare.com",
    'connect-src': "'self'"
} 