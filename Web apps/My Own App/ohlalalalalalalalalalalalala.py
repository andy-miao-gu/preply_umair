import language_tool_python

def grammar_check(text):
    # Create a LanguageTool instance
    tool = language_tool_python.LanguageTool('en-US')

    # Perform grammar checking
    matches = tool.check(text)

    # Print the results
    for match in matches:
        print(f"Type: {match.ruleId}")
        print(f"Message: {match.message}")
        print(f"Replacement: {match.replacements}\n")

# Example usage
input_text = "I is a engineer."
grammar_check(input_text)
