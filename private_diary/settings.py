from.settings_common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]

#静的ファイルの配置場所
STATIC_ROOT ='/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'

# Amazon SES関連の設定
AWS_SES_ACCESS_KEY_ID = os.environ.get('AWS_SES_ACCESS_KEY_ID')
AWS_SES_SECRET_ACCESS_KEY = os.environ.get('AWS_SES_SECRET_ACCESS_KEY')
EMAIL_BACKEND ='django_ses.SESBackend'
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

# LOGGING = {
#     'version': 1,  # 1固定
#     'disable_existing_loggers': False,

#     # ロガーの設定 ログのエントリーポイント（ログの実行開始位置）
#     'loggers': {
#         # Djangoが利用するロガー設定
#         'django': {
#             'handlers': ['file'],
#             'level': 'INFO'
#         },
#         #     diaryアプリケーションが利用するロガー設定
#         'diary': {
#             'handlers': ['file'],
#             'level': 'INFO'
#         },
#     },
#     # ハンドラの設定　ログの出力先設定　出力先は複数設定可能
#     'handlers': {
#         'file': {
#             'level': 'INFO',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename':os.path.join(BASE_DIR,'logs/django.log'),
#             # 開発環境を本番に変更
#             'formatter':'prod',
#             # ログローテーション間隔単位を設定(D＝日)
#             'when':'D',
#             # ログローテーション間隔の設定
#             'interval': 1,
#             #保存しておくログファイルの数 
#             'backupCount':7,
#         },
#     },
#     # フォーマッタの設定　ログの出力形式を決める　形式は1つのみ
#     'formatters': {
#         'prod': {
#             'format': '\t'.join([
#                 '%(asctime)s',
#                 '[%(levelname)s]',
#                 '%(pathname)s(Line:%(lineno)d)',
#                 '%(message)s',
#             ])
#         },
#     }
# }

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')