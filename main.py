available_formatters = ["plain", "bold", "italic", "header", "link",
                        "inline-code", "new-line", "ordered-list", "unordered-list"]
special_commands = ["!help", "!done"]
markdown_text = ""


def header_formatter(markdown_text):
    level = int(input("Level: "))

    while level not in range(1, 7):
        print("The level should be within the range of 1 to 6")
        level = int(input("Level: "))

    text = input("Text: ")
    pattern = ['#']
    patterns = pattern * level

    if markdown_text == "":
        return ''.join(patterns) + ' ' + text + '\n'
    else:
        return '\n' + ''.join(patterns) + ' ' + text + '\n'


def bold_formatter():
    text = input("Text: ")
    return '**' + text + '**'


def italic_formatter():
    text = input("Text: ")
    return '*' + text + '*'


def plain_formatter():
    return input("Text: ")


def inline_code_formatter():
    text = input("Text: ")
    return '`' + text + '`'


def link_formatter():
    label = input("Label: ")
    url = input("URL: ")
    return '[' + label + ']' + '(' + url + ')'


def list_formatter(ordered=None):
    row_list = []
    rows = int(input("Number of rows: "))

    while rows <= 0:
        print("The number of rows should be greater than zero")
        rows = int(input("Number of rows: "))

    for i in range(1, rows + 1):
        row_list.append(input(f'Row #{i}: '))

    if ordered is None:
        unordered_list = map(lambda x: '* ' + x, row_list)
        return '\n'.join(unordered_list)
    else:
        unordered_list = map(lambda x: f'{row_list.index(x) + 1}. ' + x, row_list)
        return '\n'.join(unordered_list)


def check_formatter(formatter, markdown_text):
    if formatter == "header":
        markdown_text += header_formatter(markdown_text)
    elif formatter == "bold":
        markdown_text += bold_formatter()
    elif formatter == "italic":
        markdown_text += italic_formatter()
    elif formatter == "plain":
        markdown_text += plain_formatter()
    elif formatter == "inline-code":
        markdown_text += inline_code_formatter()
    elif formatter == "new-line":
        markdown_text += '\n'
    elif formatter == "link":
        markdown_text += link_formatter()
    elif formatter == "ordered-list":
        markdown_text += list_formatter(True) + '\n'
    elif formatter == "unordered-list":
        markdown_text += list_formatter() + '\n'
    print(markdown_text)
    return markdown_text


while True:
    option = input("Choose a formatter: ")
    if option == "!done":
        file = open("output.md", "w")
        file.write(markdown_text)
        file.close()
        break
    elif option == "!help":
        print(f"Available formatters: {' '.join(available_formatters)}")
        print(f"Special commands: {' '.join(special_commands)}")
    elif option not in available_formatters:
        print("Unknown formatting type or command")
    else:
        markdown_text = check_formatter(option, markdown_text)
