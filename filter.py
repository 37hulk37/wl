import re

keywords = {
    "api.vk.com",
    "eh.vk.com",
    "ads.x5.ru",
}


def filter(blocks):
    filtered = []

    for block in blocks:
        match = re.search(r"sni=([^&]+)", block)

        if not match:
            continue

        sni = match.group(1)
        if not any(k in sni.lower() for k in keywords):
            continue

        filtered.append(block)

    return filtered


def __main__():
    with open("vless_lite.txt", "r", encoding="utf-8") as f:
        content = f.read()

    blocks = re.split(r"(?=vless://)", content)

    filtered = filter(blocks)

    with open("vless_russians.txt", "w", encoding="utf-8") as f:
        f.write("".join(filtered[:50]))


if __name__ == "__main__":
    __main__()
