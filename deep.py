# This program is a simple implementation of a question and answer system. It asks the user for the answer to the Great Question of Life, the Universe, and Everything, and then checks if the answer is correct. The correct answer is "42", "forty-two", or "forty two". If the user provides any of these answers, the program will respond with "Yes". Otherwise, it will respond with "No".
def main():
    i = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    print(value(i))

def value(c):
    match c:
        case "42"|"forty-two"|"forty two":
            return "Yes"
        case _:
            return "No"
main()
