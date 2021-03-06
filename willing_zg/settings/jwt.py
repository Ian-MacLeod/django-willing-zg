from zygoat_django.settings import REST_FRAMEWORK, prod_required_env

REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"] = (
    "simplejwt_extensions.authentication.JWTAuthentication",
)

DEFAULT_VERIFYING_KEY = """MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC91RWCawEvxQj+tigRvuHxouO8
jKd35ukUxFBFRAGcI57firbAkFII6zPIiWAENGMqtjX57hk9EjAZ27XvQ4SQACvD
5j7htsJT31bZbVUH7a3JEDpxa02VXpXdfPYSs8umZkdxMxxmiD9uH9VmLN3VS14l
xQlyJdlvbLmNCAf6uwIDAQAB"""

VERIFYING_KEY = f"""-----BEGIN PUBLIC KEY-----
{prod_required_env("DJANGO_JWT_VERIFYING_KEY", DEFAULT_VERIFYING_KEY)}
-----END PUBLIC KEY-----"""

SIMPLE_JWT = {
    "USER_ID_FIELD": "public_id",
    "ALGORITHM": "RS512",
    "SIGNING_KEY": None,
    "VERIFYING_KEY": VERIFYING_KEY,
}
