class RowError(ValueError):
    """Помилка в рядку таблиці."""

    def __init__(self, line_no, reason):
        self.line_no = line_no
        super().__init__(f"рядок {line_no}: {reason}")


def parse_rows(lines: list[str], *, errors: str = "raise") -> tuple[list[dict], list[int]]:
    if errors not in ("raise", "skip"):
        raise ValueError("невідомий режим errors")

    if not lines:
        raise RowError(1, "немає заголовка")

    columns = [x.strip() for x in lines[0].split(";")]
    result = []
    skipped = []

    for line_no, line in enumerate(lines[1:], 2):
        try:
            values = [x.strip() for x in line.split(";")]
            if len(values) != len(columns):
                raise RowError(line_no, "неправильна кількість полів")

            row = dict(zip(columns, values))
            if "score" in row:
                try:
                    row["score"] = int(row["score"])
                except ValueError as e:
                    raise RowError(line_no, "score не є числом") from e

            result.append(row)
        except RowError:
            if errors == "raise":
                raise
            skipped.append(line_no)

    return result, skipped
