# XV OLIMPIADA INFORMATYCZNA "PLAKATOWANIE" (https://oi.edu.pl/static/attachment/20110704/oi15-b5.pdf)
def poster_fast(h):
    q = []
    counter = 0
    for i in range(len(h)):
        while len(q) and q[-1]>h[i]:
            q.pop()
        if not len(q) or q[-1] < h[i]:
            counter += 1
            q.append(h[i])
    return counter

def inp():

        N = int(input())
        hei = [0 for i in range(N)]
        for i in range(N):
            l = input().split(" ")
            hei[i] = int(l[1])
        print(poster_fast(hei))

def main():
    inp()

if __name__ == "__main__":
    main()