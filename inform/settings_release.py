DEBUG = False
ALLOWED_HOSTS = ["*"]
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False
EMAIL_HOST = 'smtp.mxhichina.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'notify@hxkid.com'
EMAIL_HOST_PASSWORD = '1qaz2WSX'
DEFAULT_FROM_EMAIL = 'notify@hxkid.com'
