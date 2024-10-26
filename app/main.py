from app.display_strategy import (
    DisplayStrategy,
    ConsoleDisplay,
    ReverseDisplay,
)
from app.print_strategy import PrintStrategy, ReversePrint, ConsolePrint
from app.serialize_strategy import (
    SerializeStrategy,
    JsonSerializer,
    XmlSerializer,
)


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def perform_display(self, strategy: DisplayStrategy) -> None:
        strategy.display(self.content)

    def perform_print(self, strategy: PrintStrategy) -> None:
        strategy.print_book(self.title, self.content)

    def perform_serialize(self, strategy: SerializeStrategy) -> str:
        return strategy.serialize(self.title, self.content)


def get_display_strategy(action_type: str) -> DisplayStrategy:
    return ConsoleDisplay() if action_type == "console" else ReverseDisplay()


def get_print_strategy(action_type: str) -> PrintStrategy:
    return ConsolePrint() if action_type == "console" else ReversePrint()


def get_serialize_strategy(action_type: str) -> SerializeStrategy:
    return JsonSerializer() if action_type == "json" else XmlSerializer()


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    output = ""

    for action, action_type in commands:
        if action == "display":
            book.perform_display(get_display_strategy(action_type))
        elif action == "print":
            book.perform_print(get_print_strategy(action_type))
        elif action == "serialize":
            output = book.perform_serialize(
                get_serialize_strategy(action_type))

    return output


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
