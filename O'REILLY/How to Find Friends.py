# https://py.checkio.org/en/mission/find-friends/

def check_connection(network, first, second):
    net_dic = {}

    for con in network:
        con = con.split('-')
        name_1 = con[0]
        name_2 = con[1]
        if name_1 not in net_dic.keys():
            net_dic[name_1] = [name_2]
        else:
            net_dic[name_1].append(name_2)

        if name_2 not in net_dic.keys():
            net_dic[name_2] = [name_1]
        else:
            net_dic[name_2].append(name_1)

    return(find_rec(net_dic, first, second, []))


def find_rec(network, first, second, ex=[]):
    ex.append(first)
    print(ex)
    if second in network[first]:
        return True
    else:
        for name in network[first]:
            if name not in ex:
                return find_rec(network, name, second, ex)

        return False
