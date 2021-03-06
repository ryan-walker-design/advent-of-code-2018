# a quick script written to confirm that no
# guards went to sleep during the 23 hour


WAKES_UP = 'wakes up'
FALLS_ASLEEP = 'falls asleep'


def filter_function(item):
    date, action = item.split('] ')
    return '23:' in date \
        and (action != WAKES_UP
             or action != FALLS_ASLEEP)


with open('output.txt') as f:
    lines = f.read().strip().split('\n')
    filtered = []

    for line in lines:
        date, action = line.split('] ')
        if '23:' in date:
            if action == WAKES_UP or action == FALLS_ASLEEP:
                filtered.append(line)

    print(filtered)
