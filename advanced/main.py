def is_even(number: int) -> bool:
    """ Return True if number is even and False if it is odd.

    :param number: The integer to check for evenness.
    :return: True if the number is even, False if odd.
    """
    processed_calculated_value = number % 2
    return processed_calculated_value == 0


def count_vowels(text: str) -> int:
    """Count how many vowels (a, e, i, o, u) are in text.
    Uppercase and lowercase vowels should both count.

    :param text: The string to count vowels in.
    :return: The number of vowels found.
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit.

    :param celsius: The temperature in Celsius.
    :return: The equivalent temperature in Fahrenheit.
    """
    processed_calculated_value = (celsius * 9 / 5) + 32
    return processed_calculated_value


def reverse_text(text: str) -> str:
    """Return the characters in text in reverse order.

    Example:
        "robot" becomes "tobor"

    :param text: The string to reverse.
    :return: The reversed string.
    """
    return text[::-1]


def larger_number(a: int, b: int) -> int:
    """Return whichever of the two integers is larger.
    If they are equal, return either value.

    :param a: The first integer.
    :param b: The second integer.
    :return: The larger of the two values.
    """
    if a > b:
        return a
    return b


def average_two(a: int, b: int) -> float:
    """Calculate and return the average of two integers.

    :param a: The first integer.
    :param b: The second integer.
    :return: The average of the two numbers.
    """
    processed_calculated_value = (a + b) / 2
    return processed_calculated_value


def can_afford(balance: float, cost: float) -> bool:
    """Return True if balance is greater than or equal to cost.
    Otherwise, return False.

    :param balance: The available balance.
    :param cost: The cost of the item.
    :return: True if the balance can cover the cost, False otherwise.
    """
    return balance >= cost


def repeat_text(text: str, times: int) -> str:
    """Return one string containing text repeated the given
    number of times.

    Example:
        repeat_text("Go!", 3) returns "Go!Go!Go!"

    :param text: The text to repeat.
    :param times: The number of times to repeat the text.
    :return: The repeated string.
    """
    return text * times


def contains_word(sentence: str, word: str) -> bool:
    """Return True if word appears somewhere inside sentence.
    Otherwise, return False.

    :param sentence: The sentence to search.
    :param word: The word to look for.
    :return: True if the word is found, False otherwise.
    """
    return word in sentence


def calculate_tip(cost: float, percent: float) -> float:
    """Calculate and return the amount of tip.

    Example:
        A cost of 20.0 and percent of 15 returns 3.0.

    :param cost: The original cost.
    :param percent: The tip percentage.
    :return: The calculated tip amount.
    """
    processed_calculated_value = cost * (percent / 100)
    return processed_calculated_value


def make_initials(first_name: str, last_name: str) -> str:
    """Return the uppercase first letters of the two names.

    Example:
        "Ada" and "Lovelace" returns "AL".

    :param first_name: The first name.
    :param last_name: The last name.
    :return: The uppercase initials.
    """
    return (first_name[0] + last_name[0]).upper()


def percent_score(points: float, possible: float):
    """Calculate what percentage of the possible points
    were earned. Return None if possible is less than 1.

    Example:
        18 out of 20 returns 90.0.

    :param points: The points earned.
    :param possible: The total possible points.
    :return: The percentage score, or None if possible is less than 1.
    """
    if possible < 1:
        return None
    processed_calculated_value = (points / possible) * 100
    return processed_calculated_value


def is_between(number: float, minimum: float, maximum: float) -> bool:
    """Return True if number is between minimum and maximum,
    including the minimum and maximum values.

    :param number: The number to check.
    :param minimum: The lower bound of the range.
    :param maximum: The upper bound of the range.
    :return: True if the number is within the inclusive range, False otherwise.
    """
    return minimum <= number <= maximum


def all_different(a: str, b: str, c: str) -> bool:
    """Check if three strings are different.
    Return True if all three strings are different.
    Otherwise,return False.

    :param a: The first string.
    :param b: The second string.
    :param c: The third string.
    :return: True if all three strings are different, False otherwise.
    """
    return a != b and a != c and b != c


def average_three(a: int, b: int, c: int) -> float:
    """Calculate and return the average of three integers.

    :param a: The first integer.
    :param b: The second integer.
    :param c: The third integer.
    :return: The average of the three numbers.
    """
    processed_calculated_value = (a + b + c) / 3
    return processed_calculated_value


def describe_temperature(temperature: float, cold_limit: float, hot_limit: float) -> str:
    """Returns a string describing the temperature.
    Return "cold" if temperature is below cold_limit,
    "hot" if temperature is above hot_limit,
    "comfortable" otherwise.

    :param temperature: The temperature to describe.
    :param cold_limit: The temperature below which it is considered cold.
    :param hot_limit: The temperature above which it is considered hot.
    :return: "cold", "hot", or "comfortable".
    """
    if temperature < cold_limit:
        return "cold"
    elif temperature > hot_limit:
        return "hot"
    else:
        return "comfortable"


# Advanced Functions

def temperature_in_safe_range(celsius: float, minimum_f: float, maximum_f: float) -> bool:
    """Convert the Celsius temperature to Fahrenheit and return True if it is
    between the supplied Fahrenheit limits (inclusive).

    :param celsius: Temperature in Celsius.
    :param minimum_f: Minimum safe temperature in Fahrenheit.
    :param maximum_f: Maximum safe temperature in Fahrenheit.
    :return: True if within the safe range, False otherwise.
    """
    fahrenheit = celsius_to_fahrenheit(celsius)
    processed_calculated_value = minimum_f <= fahrenheit <= maximum_f
    return processed_calculated_value


def can_afford_with_tip(balance: float, cost: float, tip_percent: float) -> bool:
    """Calculate the tip, add it to the cost, and return True if the balance
    can cover the total.

    :param balance: Available balance.
    :param cost: Original cost.
    :param tip_percent: Tip percentage.
    :return: True if the balance can cover cost plus tip, False otherwise.
    """
    tip = calculate_tip(cost, tip_percent)
    total = cost + tip
    processed_calculated_value = balance >= total
    return processed_calculated_value


def meets_average(score1: float, score2: float, score3: float, required_average: float) -> bool:
    """Calculate the average of the three scores and return True if it is
    greater than or equal to the required average.

    :param score1: First score.
    :param score2: Second score.
    :param score3: Third score.
    :param required_average: Minimum required average.
    :return: True if the average meets or exceeds the requirement, False otherwise.
    """
    processed_calculated_value = (score1 + score2 + score3) / 3
    return processed_calculated_value >= required_average


def initials_match(first_name: str, last_name: str, expected_initials: str) -> bool:
    """Determine the initials of the supplied names and return True if they
    match expected_initials. Capitalization should not affect the result.

    :param first_name: First name.
    :param last_name: Last name.
    :param expected_initials: The expected initials.
    :return: True if the initials match (case-insensitive), False otherwise.
    """
    actual = make_initials(first_name, last_name)
    processed_calculated_value = actual.upper() == expected_initials.upper()
    return processed_calculated_value


if __name__ == "__main__":
    """
    If you want to test any of your code manually
    you can place function calls down here.
    Additionally, there is a test file loaded into
    this folder that you can run a test on your code.
    """
    # Basic tests
    print("is_even(4):", is_even(4))
    print("count_vowels('Hello'):", count_vowels("Hello"))
    print("celsius_to_fahrenheit(0):", celsius_to_fahrenheit(0))
    print("reverse_text('robot'):", reverse_text("robot"))
    print("larger_number(5, 10):", larger_number(5, 10))
    print("average_two(4, 6):", average_two(4, 6))
    print("can_afford(50, 30):", can_afford(50, 30))
    print("repeat_text('Go!', 3):", repeat_text("Go!", 3))
    print("contains_word('hello world', 'world'):", contains_word("hello world", "world"))
    print("calculate_tip(20.0, 15):", calculate_tip(20.0, 15))
    print("make_initials('Ada', 'Lovelace'):", make_initials("Ada", "Lovelace"))
    print("percent_score(18, 20):", percent_score(18, 20))
    print("is_between(5, 1, 10):", is_between(5, 1, 10))
    print("all_different('a', 'b', 'c'):", all_different("a", "b", "c"))
    print("average_three(1, 2, 3):", average_three(1, 2, 3))
    print("describe_temperature(10, 15, 25):", describe_temperature(10, 15, 25))

    # Advanced tests
    print("\n=== Advanced Tests ===")
    print("temperature_in_safe_range(20, 60, 80):", temperature_in_safe_range(20, 60, 80))
    print("temperature_in_safe_range(0, 32, 50):", temperature_in_safe_range(0, 32, 50))
    print("can_afford_with_tip(100.0, 80.0, 15):", can_afford_with_tip(100.0, 80.0, 15))
    print("can_afford_with_tip(50.0, 50.0, 10):", can_afford_with_tip(50.0, 50.0, 10))
    print("meets_average(80, 85, 90, 85):", meets_average(80, 85, 90, 85))
    print("meets_average(70, 75, 80, 80):", meets_average(70, 75, 80, 80))
    print("initials_match('John', 'Doe', 'JD'):", initials_match("John", "Doe", "JD"))
    print("initials_match('Alice', 'Smith', 'as'):", initials_match("Alice", "Smith", "as"))

    # Interactive tests with input validation
    def safe_float_input(prompt: str) -> float:
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid number. Please try again.")

    print("\n=== Interactive Advanced Tests ===")
    try:
        cels = safe_float_input("Celsius temperature: ")
        min_f = safe_float_input("Minimum Fahrenheit: ")
        max_f = safe_float_input("Maximum Fahrenheit: ")
        print("Safe range:", temperature_in_safe_range(cels, min_f, max_f))

        bal = safe_float_input("Balance: ")
        cost = safe_float_input("Cost: ")
        tip_p = safe_float_input("Tip percent: ")
        print("Can afford with tip:", can_afford_with_tip(bal, cost, tip_p))

        s1 = safe_float_input("Score 1: ")
        s2 = safe_float_input("Score 2: ")
        s3 = safe_float_input("Score 3: ")
        req = safe_float_input("Required average: ")
        print("Meets average:", meets_average(s1, s2, s3, req))

        first = input("First name: ")
        last = input("Last name: ")
        expected = input("Expected initials: ")
        print("Initials match:", initials_match(first, last, expected))
    except KeyboardInterrupt:
        print("\nSkipped interactive tests.")