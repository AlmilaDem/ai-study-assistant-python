from tools import calculator_tool, file_reader_tool


class StudyAssistantAgent:
    def process_request(self, user_input: str) -> str:
        if not user_input or not user_input.strip():
            return "Error: Input cannot be empty."

        user_input = user_input.strip()

        if user_input.startswith("calculate:"):
            expression = user_input.replace("calculate:", "").strip()
            result = calculator_tool(expression)
            return self.format_response("Calculator Tool", result)

        if user_input.startswith("read file:"):
            file_path = user_input.replace("read file:", "").strip()
            result = file_reader_tool(file_path)
            return self.format_response("File Reader Tool", result)

        return self.format_response(
            "No external tool",
            "The system received the question. More detailed AI-style analysis will be added later."
        )

    def format_response(self, tool_name: str, result: str) -> str:
        return (
            f"Tool used: {tool_name}\n"
            f"Result:\n{result}"
        )
