def read_freqs():
    freqs = []
    with open('day1.txt') as file:
        for freq in file:
            freqs.append(int(freq))
    return freqs


def get_total_freq():
    return sum(read_freqs())


def find_repeated_freq():
    total_freq = 0
    found_freqs = [0]
    duplicate_freq = None
    freqs = read_freqs()
    # freqs = [-6, +3, +8, +5, -6]
    while duplicate_freq is None:
        for freq in freqs:
            total_freq += int(freq)
            if total_freq in found_freqs:
                duplicate_freq = total_freq
                print('FOUND IT')
                break
            else:
                found_freqs.append(total_freq)
        #print(found_freqs)
    return duplicate_freq



# Part 1
print(get_total_freq())

# Part 2
print(find_repeated_freq())