# WordMaster - A Powerful Text Manipulation Tool

def reverse_text(text):
    """Reverses the entire text."""
    return text[::-1]


def change_case(text, case_type):
    """Changes the case of the text."""
    if case_type == "uppercase":
        return text.upper()
    elif case_type == "lowercase":
        return text.lower()
    elif case_type == "capitalize":
        return text.title()
    else:
        return text


def count_words_chars(text):
    """Counts the number of words and characters."""
    words = len(text.split())
    chars_with_spaces = len(text)
    chars_without_spaces = len(text.replace(" ", ""))
    return words, chars_with_spaces, chars_without_spaces


def remove_extra_spaces(text):
    """Removes unnecessary spaces from the text."""
    return " ".join(text.split())


def find_and_replace(text, find_str, replace_str):
    """Finds and replaces all occurrences of a string."""
    return text.replace(find_str, replace_str)


def split_text(text, split_type):
    """Splits text into a list of words or sentences."""
    if split_type == "words":
        return text.split()
    elif split_type == "sentences":
        import re
        return re.split(r'(?<=[.!?]) +', text)
    else:
        return [text]


def join_text(parts, joiner=" "):
    """Joins a list of words or sentences into a single string."""
    return joiner.join(parts)


def main():
    print("Welcome to WordMaster - A Powerful Text Manipulation Tool!")
    print("Select an operation to perform:")
    print("1. Reverse Text")
    print("2. Change Case")
    print("3. Count Words/Characters")
    print("4. Remove Extra Spaces")
    print("5. Find and Replace")
    print("6. Split Text")
    print("7. Join Text")
    print("8. Exit")

    while True:
        choice = input("\nEnter your choice (1-8): ").strip()

        if choice == "1":
            text = input("Enter the text to reverse: ")
            print("Reversed Text:", reverse_text(text))

        elif choice == "2":
            text = input("Enter the text: ")
            case_type = input("Choose case (uppercase/lowercase/capitalize): ").lower()
            print("Updated Text:", change_case(text, case_type))

        elif choice == "3":
            text = input("Enter the text: ")
            words, chars_with_spaces, chars_without_spaces = count_words_chars(text)
            print(f"Words: {words}, Characters (with spaces): {chars_with_spaces}, Characters (without spaces): {chars_without_spaces}")

        elif choice == "4":
            text = input("Enter the text with extra spaces: ")
            print("Text without extra spaces:", remove_extra_spaces(text))

        elif choice == "5":
            text = input("Enter the text: ")
            find_str = input("Enter the word/phrase to find: ")
            replace_str = input("Enter the word/phrase to replace with: ")
            print("Updated Text:", find_and_replace(text, find_str, replace_str))

        elif choice == "6":
            text = input("Enter the text to split: ")
            split_type = input("Split into (words/sentences): ").lower()
            print("Split Result:", split_text(text, split_type))

        elif choice == "7":
            parts = input("Enter the list of words/sentences to join (comma-separated): ").split(",")
            joiner = input("Enter the joining character (default is space): ") or " "
            print("Joined Text:", join_text(parts, joiner))

        elif choice == "8":
            print("Thank you for using WordMaster. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

# Run the script
if __name__ == "__main__":
    main()
