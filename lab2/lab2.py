def replace_with_backup(path, old: str, new: str) -> int:
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    with open(path + ".bak", "w", encoding="utf-8") as backup:
        backup.write(text)

    count = text.count(old)

    if count > 0:
        text = text.replace(old, new)

        with open(path, "w", encoding="utf-8") as file:
            file.write(text)

    return count