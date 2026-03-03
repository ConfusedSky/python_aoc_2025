import sys

def parse_directions(filepath):
    numbers = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            direction = line[0]
            value = int(line[1:])
            if direction == 'L':
                numbers.append(-value)
            elif direction == 'R':
                numbers.append(value)
            else:
                raise ValueError(f"Unknown direction '{direction}' in line: {line}")
    return numbers

def apply_direction(current_position, offset):
    ending_position = (current_position + 100 + offset) % 100
    passed_zero = abs(offset)//100

    # if we are currently at zero we shouldn't be counting flipping forward or
    # back as passing 0
    if current_position == 0:
        return ending_position, passed_zero

    if ending_position == 0:
        passed_zero += 1
    elif offset < 0:
        passed_zero += 1 if ending_position > current_position else 0
    else:
        passed_zero += 1 if ending_position < current_position else 0

    return ending_position, passed_zero

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parse_directions.py <filepath>")
        sys.exit(1)

    position = 50
    at_zero = 0
    print(f"0: {position}")
    filepath = sys.argv[1]
    numbers = parse_directions(filepath)
    for n in numbers:
        position, passed_zero = apply_direction(position, n)
        at_zero += passed_zero
        print(f"{n}: {position} {passed_zero}")

    print(at_zero)
