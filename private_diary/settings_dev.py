from.settings_common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5xxn&(ymab(_mj3)%huxr-k6$2(@j3jo0!ih!d&%ocxkqbqj*u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# ロギングの設定　ログ（履歴）記録する
LOGGING = {
    'version': 1,  # 1固定
    'disable_existing_loggers': False,

    # ロガーの設定 ログのエントリーポイント（ログの実行開始位置）
    'loggers': {
        # Djangoが利用するロガー設定
        'django': {
            'handlers': ['console'],
            'level': 'INFO'
        },
        #     diaryアプリケーションが利用するロガー設定
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
    },
    # ハンドラの設定　ログの出力先設定　出力先は複数設定可能
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev',
        },
    },
    # フォーマッタの設定　ログの出力形式を決める　形式は1つのみ
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s',
            ])
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'