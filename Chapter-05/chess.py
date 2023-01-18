test1={'1a':'wking', '6c': 'wqueen', '2g': 'bbishop', '2h': 'bknight', '3e': 'bking','1h':'zqueen','4a':'bpawn','4b':'bpawn','4c':'bpawn','4d':'bpawn','4e':'bpawn','4f':'bpawn','4g':'bpawn','4h':'bpawn','5a':'wpawn','5b':'wpawn','5c':'wpawn','5d':'wpawn','5e':'wpawn','5f':'wpawn','5g':'wpawn','5h':'wpawn'}
test2={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
x = ["1", "2", "3", "4", "5", "6", "7", "8"]
y = ["a", "b", "c", "d", "e", "f", "g", "h"]
piece=["pawn","rook","knight","bishop","queen","king"]
col=["w","b"]

def isValidChessBoard(CB):
    for i in CB.keys():
        if i[0] in x and i[1] in y: 
            p1=True 
        else:
            p1=False
            break
    c=0
    for i in CB.values():
        for j in col:
            for k in piece:
                if i==j+k:
                    c+=1
                else:
                    pass
    a1=list(CB.values()).count("wking")
    b1=list(CB.values()).count("bking")        
    a2=list(CB.values()).count("wqueen")
    b2=list(CB.values()).count("bqueen")
    a3=list(CB.values()).count("wbishop")
    b3=list(CB.values()).count("bbishop")
    a4=list(CB.values()).count("wknight")
    b4=list(CB.values()).count("bknight")
    a5=list(CB.values()).count("wrook")
    b5=list(CB.values()).count("brook")
    a6=list(CB.values()).count("wpawn")
    b6=list(CB.values()).count("bpawn")
    if a1>1 or b1>1 or a2>1 or b2>1 or a3>2 or b3>2 or a4>2 or b4>2 or a5>2 or b5>2 or a5>8 or b5>8:
        d=1
    else:
        d=0
    if c==len(CB) and d==0:
        p2=True
    else:
        p2=False

    if p1==True and p2==True:
        return True
    else:
        return False

if isValidChessBoard(test2):
    print("Proper Chess board")
else:
    print("Improper Chess board")