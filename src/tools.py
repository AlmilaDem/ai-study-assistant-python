def calculator_tool(expression: str) -> str:
    try:
        allowed_characters = "0123456789+-*/(). "
        if not all(char in allowed_characters for char in expression):
            return "Error: Invalid characters in expression."

        result = eval(expression)
        return f"Calculation result: {result}"

    except Exception as error:
        return f"Calculation error: {error}"


def file_reader_tool(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        if not content.strip():
            return "The file is empty."

        return content

    except FileNotFoundError:
        return "Error: File not found."

    except Exception as error:
        return f"File reading error: {error}"
