def main():
    list = [[1,2,3],[0,4,5],[4,0,1],[6,5,4]]
    key = "abcd"
    dicc = {k:v for k,v in zip(key,list)}

    for _,l in enumerate(list):
        if 0 == l[0]:
            continue
        elif 0 in l:
            l.pop(l.index(0))
        
        print(l)
    for k in dicc:
        print(f"{k}:{dicc.get(k)}")

main()