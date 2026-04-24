from agent import StudyAssistantAgent


def main():
    agent = StudyAssistantAgent()

    print("AI Study Assistant")
    print("Example inputs:")
    print("calculate: 5 + 3 * 2")
    print("read file: example.txt")
    print()

    user_input = input("Enter your request: ")
    response = agent.process_request(user_input)

    print()
    print(response)


if __name__ == "__main__":
    main()
