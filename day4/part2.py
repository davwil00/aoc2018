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


def find_sleepiest_minute_per_guard(schedule):
    guard_mins = {}
    for guard, days in schedule.items():
        minute_count = defaultdict(int)
        for day in days.values():
            for minute in day:
                minute_count[minute] += 1

        most_frequent_minute = sorted(minute_count, key=lambda key: minute_count.get(key), reverse=True)[0]
        guard_mins[guard] = (most_frequent_minute, minute_count.get(most_frequent_minute))
    return guard_mins


def find_sleepiest_minute_overall(guard_mins):
    guard = max(guard_mins, key=lambda key: guard_mins.get(key)[1])
    return guard, guard_mins.get(guard)[0]


with open('input.txt', 'r') as input:
    schedule = compile_schedule(sort(input))
    guard_mins = find_sleepiest_minute_per_guard(schedule)
    sleepiest_minute = find_sleepiest_minute_overall(guard_mins)
    print(sleepiest_minute[0] * sleepiest_minute[1])
