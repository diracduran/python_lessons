"""
You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence. It can be only one.

Input: non empty list of strings.

Output: a string.

Example:

most_frequent([
    'a', 'b', 'c', 
    'a', 'b',
    'a'
]) == 'a'
most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
"""

def most_frequent(data: list) -> str:
    max = 0
    frequent_item = None
    for item in data:
        item_count = data.count(item)
        if item_count > max:
            max = item_count
            frequent_item = item
    return frequent_item


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))

    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"

    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")