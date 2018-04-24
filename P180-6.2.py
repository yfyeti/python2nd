def duplic(lst):
    for i in lst:
        if (lst.count(i) >= 2):
            print("True")
            break


lst1 = [123123, 23123, '123123', [123], (123), 123]
duplic(lst1)
