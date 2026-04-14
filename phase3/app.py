def load_log() -> list:
    with open("log.txt", "r") as f:
        return f.readlines()