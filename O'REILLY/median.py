# https://py.checkio.org/en/mission/median/


def checkio(data):
    data.sort()
    if len(data) % 2 == 0:
        return (int(data[(len(data) // 2)]) + int(data[((len(data) // 2) - 1)])) / 2
    else:
        return int(data[len(data) // 2])
