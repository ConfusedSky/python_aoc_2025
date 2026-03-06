import sys
import math
import bisect

def parse_ranges(filepath):
    ranges = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
    ranges = list(
        map(
            lambda x: list(map(
                lambda y: int(y),
                x.split('-')
            )),
            line.split(',')
        )
    )
    return ranges

all_scans = {}
def get_legal_scans(length):
    if all_scans.get(length):
        return all_scans[length]

    legal_scans = [1]
    # Check for all legal scan lengths
    # You can square root here because if a value is evenly divisible
    # you get the lower and the higher value and since low*high must be less
    # than the length this is correct
    # this can be memorized to speed this up
    for i in range(2, math.floor(math.sqrt(length)) + 1):
        if length % i == 0 and i != length:
            # These should be inserted in order
            bisect.insort(legal_scans, i)
            if length//i != i:
                bisect.insort(legal_scans, length//i)

    # This could be done a lot faster however the number of elements is
    # really low so it doesn't seem to be an issue
    # sort the scans in highest to lowest order so we check the cheaper scans
    # first
    legal_scans.reverse()
    all_scans[length] = legal_scans

    return legal_scans


def check_value(value):
    svalue = str(value)
    length = len(svalue)

    if length == 1:
        return False

    legal_scans = get_legal_scans(length)


    for scan in legal_scans:
        has_solution = True

        for i in range(0, scan):
            expected = svalue[i]
            for index in range(i + scan, length, scan):
                if svalue[index] != expected:
                    has_solution = False
                    break
            if not has_solution:
                break

        if has_solution:
            print(value, scan, legal_scans, length)
            return True


    return False

def check_range(low, high):
    invalid_ids = []

    for value in range(low, high + 1):
        if check_value(value):
            invalid_ids.append(value)

    return invalid_ids

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parse_directions.py <filepath>")
        sys.exit(1)

    filepath = sys.argv[1]
    ranges = parse_ranges(filepath)

    print(ranges)
    total = 0
    for [low, high] in ranges:
        invalid_ids = check_range(low, high)
        for id in invalid_ids:
            total += id
    print(total)

