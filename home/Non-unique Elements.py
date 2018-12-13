# https://py.checkio.org/en/mission/non-unique-elements/


def checkio(data):
    pam = []
    if data:
        for i in data:
            if data.count(i) > 1:
                pam.append(i)
    return pam
