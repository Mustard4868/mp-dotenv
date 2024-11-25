def get_env(key, *, path: str = "./.env") -> dict:
    with open(path) as f:
        for line in f:
            if not line.startswith("#"):
                env, value = line.strip().split("=")
                if env == key:
                    return value