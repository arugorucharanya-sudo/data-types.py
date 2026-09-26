def string_calculation():
    print("\n========== STRING CALCULATION ==========")

    text = input("Enter a string: ")

    print("\nString Results:")
    print("Original String:", text)
    print("Length:", len(text))
    print("Uppercase:", text.upper())
    print("Lowercase:", text.lower())
    print("Title Case:", text.title())
    print("Reversed String:", text[::-1])
    print("Number of words:", len(text.split()))

    character = input("\nEnter a character to search: ")

    print(
        f"Occurrences of '{character}': "
        f"{text.lower().count(character.lower())}"
    )

    if character.lower() in text.lower():
        print(f"'{character}' is present in the string.")
    else:
        print(f"'{character}' is not present in the string.")
