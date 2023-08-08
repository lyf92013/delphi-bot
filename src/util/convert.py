from pydantic import validate_arguments


@validate_arguments
def to_camel_case(snake_string: str | None) -> str | None:
    if not snake_string:
        return None

    words = snake_string.split("_")
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return words[0] + "".join(word.title() for word in words[1:])
