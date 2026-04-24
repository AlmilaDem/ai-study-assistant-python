import sys
import os

sys.path.append(os.path.abspath("src"))

from agent import StudyAssistantAgent
from tools import calculator_tool


def test_calculator_tool():
    result = calculator_tool("5 + 3")
    assert "8" in result


def test_empty_input():
    agent = StudyAssistantAgent()
    result = agent.process_request("")
    assert "Input cannot be empty" in result


def test_agent_uses_calculator():
    agent = StudyAssistantAgent()
    result = agent.process_request("calculate: 10 / 2")
    assert "Calculator Tool" in result
    assert "5" in result
