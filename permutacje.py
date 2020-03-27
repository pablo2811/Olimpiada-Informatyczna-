# XIX OLIMPIADA INFORMATYCZNA "LITERKI" (https://oi.edu.pl/l/19oi_ksiazeczka/)


from sys import stdin

def edit(u, w, n):
    i = 0
    mapping = {}
    for let in range(n-1,-1,-1):
        if u[let] in mapping.keys():
            mapping[u[let]].append(n-i)
        else:
            mapping[u[let]] = [n-i]
        i += 1
    per = [0]*n
    for k in range(n):
        per[k] = mapping[w[k]].pop()
    return count_inverse(per,1,n)


def count_inverse(per,a,b):
    if a == b:
        return 0
    else:
        c1 = []
        c2 = []
        res = 0
        j = 0
        pivot = (a+b)//2
        for el in per:
            if el <= pivot:
                c1.append(el)
                res += j
            else:
                c2.append(el)
                j += 1
        return res + count_inverse(c1,a,pivot) + count_inverse(c2,pivot+1,b)


def inp():
    n = int(stdin.readline())
    jas = stdin.readline()
    malg = stdin.readline()
    odp = edit(jas[:-1], malg[:-1], n)
    print(odp)


def main():
    inp()


if __name__ == "__main__":
    main()

