from datetime import datetime
import re
from collections import defaultdict


def sort(input):
    return sorted(input, key=lambda entry: get_date(entry))


def get_date(entry):
    return datetime.strptime(entry[:18], '[%Y-%m-%d %H:%M]')


def compile_schedule(data):
    schedule = defaultdict(lambda: defaultdict(list))
    current_guard = None
    asleep_minute = None
    new_guard_re = re.compile('Guard #(\d+) begins shift')
    for entry in data:
        instruction = entry[19:].strip()
        if instruction == 'falls asleep':
            asleep_minute = int(entry[15:17])
        elif instruction == 'wakes up':
            current_date = get_date(entry).date()
            current_minute = int(entry[15:17])
            [schedule[current_guard][current_date].append(m) for m in range(asleep_minute, current_minute)]
            asleep_minute = None
        else:
            m = new_guard_re.match(instruction)
            if m:
                current_guard = int(m.group(1))
    return schedule


def find_sleepiest_guard(schedule):
    sorted_guards = sorted(schedule.items(), key=lambda g: sum([len(m) for m in g[1].values()]), reverse=True)
    return sorted_guards[0][0]


def find_sleepiest_minute(guard):
    minute_count = defaultdict(int)
    for day in guard.values():
        for minute in day:
            minute_count[minute] += 1
    return max(minute_count, key=lambda key: minute_count.get(key))


with open('input.txt', 'r') as input:
    schedule = compile_schedule(sort(input))
    guard = find_sleepiest_guard(schedule)
    minute = find_sleepiest_minute(schedule[guard])
    print(guard * minute)
