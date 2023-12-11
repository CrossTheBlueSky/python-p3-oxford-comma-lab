def oxford_comma(items):
    if len(items) > 2:
        joined = ",-".join(items)
        separated = joined.split("-")
        separated.insert(-1, "and")
        return " ".join(separated)
    elif len(items) == 2:
        items.insert(-1, "and")
        return " ".join(items)
    else:
        return items[0]

