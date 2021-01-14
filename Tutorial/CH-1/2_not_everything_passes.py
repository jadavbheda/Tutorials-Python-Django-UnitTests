"""Method returns sum of all the elements in a list
"""
def sum(list_to_sum):
    total = 0
    for el in list_to_sum:
        total += el
    return total


"""Test to test sum method
"""
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")
