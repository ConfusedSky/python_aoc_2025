import sys

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

def check_range(low, high):
    invalid_ids = []

    value = low
    while value <= high:
        svalue = str(value)
        # this can probably be done smarter
        # however I'm just trying to get this done
        # ranges need to look at both the low and the high
        # so the range would need to be bumped up or shortened to
        # the nearest even number of digits
        if len(svalue) % 2 == 1:
            value += 1
            continue

        # this can be done faster as well by scanning the indexes in place
        # rather than making two strings
        midpoint = len(svalue)//2
        left = svalue[:midpoint]
        right = svalue[midpoint:]
        if left == right:
            invalid_ids.append(value)
            print(svalue, left, right)
        value += 1

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

