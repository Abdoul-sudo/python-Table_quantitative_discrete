# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def xj(arr):
    return list(set(datas))

def nj(xj, arr):
    return [arr.count(i) for i in xj]

def Nj(nj):
    return [round(sum(nj[:key+1]), 2) for key, val in enumerate(nj)]

def fj(nj, N):
    return [round(i/N, 2) for i in nj]

def Fj(fj):
    return [round(sum(fj[:key+1]), 2) for key, val in enumerate(fj)]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    datas = [1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,6,6,6,8,8]
    count = len(datas)


    xj = xj(datas)
    nj = nj(xj, datas)
    Nj = Nj(nj)
    fj = fj(nj, count)
    Fj = Fj(fj)

    count_fj = len(fj)

    # AFFICHAGE
    print("xj | nj | Nj | fj | Fj\n___________________________")
    for key, value in enumerate(xj):
        print(f'{xj[key]} | {nj[key]} | {Nj[key]} | {fj[key]} | {Fj[key]}')
    print(f'___________________________')
    print(f'..| {count} |..  | {count_fj}  |.. ')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
