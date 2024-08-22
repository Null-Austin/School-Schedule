file = open('schedule.txt', 'r')
schedule = file.read()

def get_times():
    lines = schedule.splitlines()[1:]  # get all text except the first line
    num_lines = len(lines)  # how many lines there are
    index = 0  # start with the first line
    time_list = []

    while index < num_lines:
        first_word = lines[index].split(' ', 1)[1]  # get the value of the first word (0)
        time_list.append(first_word)
        index += 1

    return time_list
def get_clases():
    lines = schedule.splitlines()[1:]  # get all text except the first line
    num_lines = len(lines)  # how many lines there are
    index = 0  # start with the first line
    time_list = []

    while index < num_lines:
        first_word = lines[index].split(' ', 1)[0]  # get the value of the first word (0)
        time_list.append(first_word)
        index += 1

    return time_list
def split_times(time):
    return([time.replace('-',' ').split(' ', 1)[1],time.replace('-',' ').split(' ', 1)[0]][::-1])

times = get_times()
