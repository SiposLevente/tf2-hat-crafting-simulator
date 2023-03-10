def read_settings() -> dict[str, str]:
    content = [x.strip() for x in open(
        "settings.conf", "r", encoding="utf-8").read().split('\n') if '=' in x]
    return_dict: dict[str, str] = dict()
    for line in content:
        key, value = line.split('=')
        return_dict[key] = value
    return return_dict


def read_hats() -> list[str]:
    return [x.strip() for x in open("hats.txt", "r", encoding="utf-8").read().split('\n') if '#' not in x and x != ""]
