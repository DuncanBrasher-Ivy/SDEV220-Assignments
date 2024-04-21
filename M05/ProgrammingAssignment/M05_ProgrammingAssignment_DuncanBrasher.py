import unittest


def catch(f):
    try:
        f()
        return True
    except Exception as e:
        print(e)
        return False


def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"



class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")


def main1():
    a = catch(test_sum)
    b = catch(test_sum_tuple)
    rs = [a, b]
    if all(rs):
        print("Everything passed")
    elif any(rs):
        print("Something passed")
    else:
        print("Nothing passed")


def main2():
    catch(unittest.main)


def main():
    main1()
    main2()


if __name__ == '__main__':
    main()


