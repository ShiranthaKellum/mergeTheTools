from collections import OrderedDict

def mergeTheTools (s, k):
    n = len (s)
    for i in range (0, n, k):
        # print (str [i])
        # print (str [i : i+s])
        sub = s [i : i+k]                       # divide n/k number of substrings which each has k length.
        # u = []
        # u.append (sub [0])
        # print (sub)
        seq = []
        for j in sub:
            seq.append (j)

        # noDupList = set (seq)                 # set function remove the duplicates of a list and return an unorderd list.                              
        # print (u)
        u = OrderedDict.fromkeys (seq)          # fromkeys function of OrderedDict class removes duplicates and return a list without changing the original order.
        print ("".join (u))        


if __name__ == '__main__':
    # string = "AAABCADDE"
    string = input ()
    # size = 3
    size = int (input ())
    mergeTheTools (string, size)