
def counter(s:str):
    count = 0
    k = 0
    d = s.lower()
    while k<len(s):
        if d[k] in 'aeoui':
            count+=1
        k+=1
    print(count)

counter("Assalamualeykum")
