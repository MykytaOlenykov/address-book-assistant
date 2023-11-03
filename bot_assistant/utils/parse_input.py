from prompt_toolkit.lexers import Lexer
from prompt_toolkit.styles.named_colors import NAMED_COLORS
from prompt_toolkit.completion import NestedCompleter


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


class RainbowLexer(Lexer):
    def lex_document(self, document):
        colors = list(sorted({"Teal": "#008080"}, key=NAMED_COLORS.get))

        def get_line(lineno):
            return [
                (colors[i % len(colors)], c)
                for i, c in enumerate(document.lines[lineno])
            ]

        return get_line


Completer = NestedCompleter.from_nested_dict(
    {
        "hello": None,
        "exit": None,
        "close": None,
        "help": None,
        "add-contact": None,
        "change-contact": None,
        "show-contact": None,
        "all": None,
        "delete-contact": None,
        "show-phone": None,
        "remove-phone": None,
        "add-email": None,
        "show-email": None,
        "change-email": None,
        "remove-email": None,
        "add-address": None,
        "show-address": None,
        "change-address": None,
        "remove-address": None,
        "add-note": None,
        "find-note": None,
        "show-note": None,
        "delete-note": None,
        "add-tags": None,
        "change-tag": None,
        "remove-tags": None,
        "add-birthday": None,
        "birthdays": None,
        "show-birthday": None,
    }
)
