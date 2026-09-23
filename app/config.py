import os


def _load_dotenv(path=".env"):
    """Load simple KEY=VALUE entries without requiring python-dotenv."""
    if not os.path.isfile(path):
        return

    with open(path, encoding="utf-8") as env_file:
        for line in env_file:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            os.environ.setdefault(key, value)


_load_dotenv()


RETELL_API_KEY = os.getenv("RETELL_API_KEY")


if not RETELL_API_KEY:
    raise RuntimeError("RETELL_API_KEY is not set")