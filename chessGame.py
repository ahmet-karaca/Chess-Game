import sys
f=open(sys.argv[1],"r")
commands=[line.split() for line in f.readlines()]
f.close()


board = [['r1', 'n1', 'b1', 'qu', 'ki', 'b2', 'n2', 'r2'],['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8'],["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],['R1', 'N1', 'B1', 'QU', 'KI', 'B2', 'N2', 'R2']]
boardii = [['r1', 'n1', 'b1', 'qu', 'ki', 'b2', 'n2', 'r2'],['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8'],["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],['R1', 'N1', 'B1', 'QU', 'KI', 'B2', 'N2', 'R2']]

boardstr = ""
h = ""
columns = ["a", "b", "c", "d", "e", "f", "g", "h"]

def setboard(x):
    global boardstr
    global h
    h = ""
    for i in range(0,len(x)):
        b = (x[i])
        for j in range (len(b)):
            h += b[j]
        
        
def setboardf(x):
    global boardstr
    global h
    h = ""
    boardd = x.copy()
    a = boardd[0]
    b = boardd[1]
    c = boardd[2]
    d = boardd[3]
    e = boardd[4]
    f = boardd[5]
    g = boardd[6]
    i = boardd[7]
    boardd[0] = i
    boardd[1] = g
    boardd[2] = f
    boardd[3] = e
    boardd[4] = d
    boardd[5] = c
    boardd[6] = b
    boardd[7] = a
    
    for i in range(0,len(boardd)):
        b = (boardd[i])
        for j in range (len(b)):
            h += b[j]
            boardstr +=(b[j]+" ")
        boardstr +=("\n")
        
        
def smoc(x) :# showmoves output converter
    global b
    b = []
    for i in range(len(x)):
        b += [columns[x[i][1]] +str(x[i][0]+1)]
    b = sorted(b)
    return x


def popi(x):  #position of pieces
    setboard(board)
    global rop
    global cop
    global copp
    nop = h.index(x)//2    #number of pieces
    rop = (nop//8)         #rows of pieces
    copp = (nop%8)
    cop = columns[copp] #column of pieces
    
    
def smr(x):    # rook - kale
    global smrl
    popi(x)
    smrl = []
    
    for i in range(1,8):  #dikey yukarı kontrol
        if (rop-i) > (-1):
            if board[rop-i][copp] == "  ":
                smrl += [[rop-i, copp]]
            elif (board[rop][copp]).islower() != (board[rop-i][copp]).islower() :#düşman kare
                if (board[rop-i][copp]) == 'KI' or (board[rop-i][copp]) == 'ki':
                    "düşman şah"
                else :
                    smrl += [[rop-i,copp]]
                break
            elif (board[rop][copp]).islower() == (board[rop-i][copp]).islower() :     #dost kare
                break
            
    for i in range(1,8):  #dikey aşağı kontrol
        if (rop+i) < (8):
            if board[rop+i][copp] == "  ":
                smrl += [[rop+i, copp]]
            elif (board[rop][copp]).islower() != (board[rop+i][copp]).islower() :#düşman kare
                if (board[rop+i][copp]) == 'KI' or (board[rop+i][copp]) == 'ki':
                    "düşman şah"
                else :
                    smrl += [[rop+i,copp]]
                break
            elif (board[rop][copp]).islower() == (board[rop+i][copp]).islower() :     #dost kare
                break
            
    for i in range(1,8):  #yatay sağa kontrol
        if (copp+i) < (8):
            if board[rop][copp+i] == "  ":
                smrl += [[rop, copp+i]]
            elif (board[rop][copp]).islower() != (board[rop][copp+i]).islower() :#düşman kare
                if (board[rop][copp+i]) == 'KI' or (board[rop][copp+i]) == 'ki':
                    "düşman şah"
                else:
                    smrl += [[rop, copp+i]]
                break
            elif (board[rop][copp]).islower() == (board[rop][copp+i]).islower() :     #dost kare
                break
            
    for i in range(1,8):  #yatay sağa kontrol
        if (copp-i) > (-1):
            if board[rop][copp-i] == "  ":
                smrl += [[rop, copp-i]]
            elif (board[rop][copp]).islower() != (board[rop][copp-i]).islower() :#düşman kare
                if (board[rop][copp-i]) == 'KI' or (board[rop][copp-i]) == 'ki':
                    "düşman şah"
                else :
                    smrl += [[rop, copp-i]]
                break
            elif (board[rop][copp]).islower() == (board[rop][copp-i]).islower() :     #dost kare
                break
    smoc(smrl)
    
def smn(x): # knight - at
    global smnl
    popi(x)
    smnl = []
    
    if copp < 7 and rop > 1:
        if board[rop-2][copp+1] == "  ":
            smnl += [[rop-2, copp+1]]
        elif (board[rop][copp]).islower() != (board[rop-2][copp+1]).islower() :#düşman kare
            if (board[rop-2][copp+1]) == 'KI' or (board[rop-2][copp+1]) == 'ki' :
                "düşman şah"
            else :
                smnl += [[rop-2, copp+1]]
        
    if copp < 6 and rop > 0:
        if board[rop-1][copp+2] == "  ":
            smnl += [[rop-1, copp+2]]
        elif (board[rop][copp]).islower() != (board[rop-1][copp+2]).islower() :#düşman kare
            if (board[rop-1][copp+2]) == 'KI' or (board[rop-1][copp+2]) == 'ki' :
                "düşman şah"
            else :
                smnl += [[rop-1, copp+2]]
            
    if copp < 7 and rop < 6:
        if board[rop+2][copp+1] == "  ":
            smnl += [[rop+2, copp+1]]
        elif (board[rop][copp]).islower() != (board[rop+2][copp+1]).islower() :#düşman kare
            if (board[rop+2][copp+1]) == 'KI' or (board[rop+2][copp+1]) == 'ki' :
                "düşman şah"
            else :
                smnl += [[rop+2, copp+1]]

    if copp < 6 and rop < 7:
        if board[rop+1][copp+2] == "  ":
            smnl += [[rop+1, copp+2]]
        elif (board[rop][copp]).islower() != (board[rop+1][copp+2]).islower() :#düşman kare
            if (board[rop+1][copp+2]) == 'KI' or (board[rop+1][copp+2]) == 'ki':
                "düşman şah"
            else :
                smnl += [[rop+1, copp+2]]

    if copp >0 and rop >1 :
        if board[rop-2][copp-1] == "  ":
            smnl += [[rop-2, copp-1]]
        elif (board[rop][copp]).islower() != (board[rop-2][copp-1]).islower() :#düşman kare
            if (board[rop-2][copp-1]) == 'KI' or (board[rop-2][copp-1]) == 'ki':
                "düşman şah"
            else :
                smnl += [[rop-2, copp-1]]

    if copp >1 and rop >0 :
        if board[rop-1][copp-2] == "  ":
            smnl += [[rop-1, copp-2]]
        elif (board[rop][copp]).islower() != (board[rop-1][copp-2]).islower() :#düşman kare
            if (board[rop-1][copp-2]) == 'KI' or (board[rop-1][copp-2]) == 'ki':
                "düşman şah"
            else :
                smnl += [[rop-1, copp-2]]

    if copp >0 and rop < 6:
        if board[rop+2][copp-1] == "  ":
            smnl += [[rop+2, copp-1]]
        elif (board[rop][copp]).islower() != (board[rop+2][copp-1]).islower() :#düşman kare
            if (board[rop+2][copp-1]) == 'KI' or (board[rop+2][copp-1]) == 'ki':
                "düşman şah"
            else :
                smnl += [[rop+2, copp-1]]
        
    if copp >1 and rop < 7:
        if board[rop+1][copp-2] == "  ":
            smnl += [[rop+1, copp-2]]

    if copp < 7 and rop > 0:
        if board[rop-1][copp+1] == "  ":
            smnl += [[rop-1, copp+1]]

    if copp < 7 and rop < 7:
        if board[rop+1][copp+1] == "  ":
            smnl += [[rop+1, copp+1]]

    if copp >0 and rop >0 :
        if board[rop-1][copp-1] == "  ":
            smnl += [[rop-1, copp-1]]
        
    if copp >0 and rop < 7:
        if board[rop+1][copp-1] == "  ":
            smnl += [[rop+1, copp-1]]
    smoc(smnl)

def smbu(x):    # bishop black - fil siyah büyük    
    global smbul
    popi(x)
    smbul = []
                
    for i in range(1,8):  #yukarı sağa kontrol
        if (rop-i) > (-1) and (copp+i) < (8):
            if board[rop-i][copp+i] == "  ":                smbul += [[rop-i, copp+i]]
            elif (board[rop][copp]).islower() != (board[rop-i][copp+i]).islower() :#düşman kare
                if (board[rop-i][copp+i]) == 'KI' or (board[rop-i][copp+i]) == 'ki':
                    "düşma şah"
                else :
                    smbul += [[rop-i, copp+i]]
                break
            elif (board[rop][copp]).islower() == (board[rop-i][copp+i]).islower() :     #dost kare
                break
            
    for i in range(1,8):  #yukarı sola kontrol
        if (rop-i) > (-1) and (copp-i) > (-1):
            if board[rop-i][copp-i] == "  ":
                smbul += [[rop-i, copp-i]]
            elif (board[rop][copp]).islower() != (board[rop-i][copp-i]).islower() :#düşman kare
                if (board[rop-i][copp-i]) == 'KI' or (board[rop-i][copp-i]) == 'ki':
                    "düşman şah"
                else :
                    smbul += [[rop-i, copp-i]]
                break
            elif (board[rop][copp]).islower() == (board[rop-i][copp-i]).islower() :     #dost kare
                break
    smoc(smbul)
    
def smbd(x):    # bishop white - fil beyaz küçük   
    global smbdl
    popi(x)
    smbdl = []

    for i in range(1,8):  #aşağı sağa kontrol
        if (rop+i) < (8) and (copp+i) < (8):
            if board[rop+i][copp+i] == "  ":
                smbdl += [[rop+i, copp+i]]
            elif (board[rop][copp]).islower() != (board[rop+i][copp+i]).islower() :#düşman kare
                if (board[rop+i][copp+i]) == 'KI' or (board[rop+i][copp+i]) == 'ki':
                    "düşman şah"
                else :
                    smbdl += [[rop+i, copp+i]]
                break
            elif (board[rop][copp]).islower() == (board[rop+i][copp+i]).islower() :     #dost kare
                break
            
    for i in range(1,8):  #yukarı sola kontrol
        if (rop+i) < (8) and (copp-i) > (-1):
            if board[rop+i][copp-i] == "  ":
                smbdl += [[rop+i, copp-i]]
            elif (board[rop][copp]).islower() != (board[rop+i][copp-i]).islower() :#düşman kare
                if (board[rop+i][copp-i]) == 'KI' or (board[rop+i][copp-i]) == 'ki':
                    "düşman şah"
                else :
                    smbdl += [[rop+i, copp-i]]
                break
            elif (board[rop][copp]).islower() == (board[rop+i][copp-i]).islower() :     #dost kare
                break
    smoc(smbdl)

def smq(x):    # queen - vezir
    global smql
    popi(x)
    smql = []
    
    for i in range(1,8):  #dikey yukarı kontrol
        if (rop-i) > (-1):
            if board[rop-i][copp] == "  ":
                smql += [[rop-i, copp]]
            elif (board[rop][copp]).islower() != (board[rop-i][copp]).islower() :#düşman kare
                if (board[rop-i][copp]) == 'KI' or (board[rop-i][copp]) == 'ki':
                    "düşman şah"
                else :
                    smql += [[rop-i,copp]]
                break
            elif (board[rop][copp]).islower() == (board[rop-i][copp]).islower() :     #dost kare
                break
            
    for i in range(1,8):  #dikey aşağı kontrol
        if (rop+i) < (8):
            if board[rop+i][copp] == "  ":
                smql += [[rop+i, copp]]
            elif (board[rop][copp]).islower() != (board[rop+i][copp]).islower() :#düşman kare
                if (board[rop+i][copp]) == 'KI' or (board[rop+i][copp]) == 'ki':
                    "düşman şah"
                else :
                    smql += [[rop+i,copp]]
                break
            elif (board[rop][copp]).islower() == (board[rop+i][copp]).islower() :     #dost kare
                break
            
    for i in range(1,8):  #yatay sağa kontrol
        if (copp+i) < (8):
            if board[rop][copp+i] == "  ":
                smql += [[rop, copp+i]]
            elif (board[rop][copp]).islower() != (board[rop][copp+i]).islower() :#düşman kare
                if (board[rop][copp+i]) == 'KI' or (board[rop][copp+i]) == 'ki':
                    "düşman şah"
                else :
                    smql += [[rop, copp+i]]
                break
            elif (board[rop][copp]).islower() == (board[rop][copp+i]).islower() :     #dost kare
                break
             
    for i in range(1,8):  #yatay sağa kontrol
        if (copp-i) > (-1):
            if board[rop][copp-i] == "  ":
                smql += [[rop, copp-i]]
            elif (board[rop][copp]).islower() != (board[rop][copp-i]).islower() :#düşman kare
                if (board[rop][copp-i]) == 'KI' or (board[rop][copp-i]) == 'ki':
                    "düşman şah"
                else :
                    smql += [[rop, copp-i]]
                break
            elif (board[rop][copp]).islower() == (board[rop][copp-i]).islower() :     #dost kare
                break

    for i in range(1,8):  #yukarı sağa kontrol
        if (rop-i) > (-1) and (copp+i) < (8):
            if board[rop-i][copp+i] == "  ":
                smql += [[rop-i, copp+i]]
            elif (board[rop][copp]).islower() != (board[rop-i][copp+i]).islower() :#düşman kare
                if (board[rop-i][copp+i]) == 'KI' or (board[rop-i][copp+i]) == 'ki':
                    "düşman şah"
                else :
                    smql += [[rop-i, copp+i]]
                break
            elif (board[rop][copp]).islower() == (board[rop-i][copp+i]).islower() :     #dost kare
                break

    for i in range(1,8):  #yukarı sola kontrol
        if (rop-i) > (-1) and (copp-i) > (-1):
            if board[rop-i][copp-i] == "  ":
                smql += [[rop-i, copp-i]]
            elif (board[rop][copp]).islower() != (board[rop-i][copp-i]).islower() :#düşman kare
                if (board[rop-i][copp-i]) == 'KI' or (board[rop-i][copp-i]) == 'ki':
                    "düşman şah"
                else :
                    smql += [[rop-i, copp-i]]
                break
            elif (board[rop][copp]).islower() == (board[rop-i][copp-i]).islower() :     #dost kare
                break

    for i in range(1,8):  #aşağı sağa kontrol
        if (rop+i) < (8) and (copp+i) < (8):
            if board[rop+i][copp+i] == "  ":
                smql += [[rop+i, copp+i]]
            elif (board[rop][copp]).islower() != (board[rop+i][copp+i]).islower() :#düşman kare
                if (board[rop+i][copp+i]) == 'KI' or (board[rop+i][copp+i]) == 'ki':
                    "düşman şah"
                else:
                    smql += [[rop+i, copp+i]]
                break
            elif (board[rop][copp]).islower() == (board[rop+i][copp+i]).islower() :     #dost kare
                break
            
    for i in range(1,8):  #yukarı sola kontrol
        if (rop+i) < (8) and (copp-i) > (-1):
            if board[rop+i][copp-i] == "  ":
                smql += [[rop+i, copp-i]]
            elif (board[rop][copp]).islower() != (board[rop+i][copp-i]).islower() :#düşman kare
                if (board[rop+i][copp-i]) == 'KI' or (board[rop+i][copp-i]) == 'ki':
                    "düşman taş"
                else :
                    smql += [[rop+i, copp-i]]
                break
            elif (board[rop][copp]).islower() == (board[rop+i][copp-i]).islower() :     #dost kare
                break    
    smoc(smql)
    
def smk(x):    # king - şah
    global smkl
    popi(x)
    smkl= []
    
    if rop > 0:
        if board[rop-1][copp] == "  ":
            smkl += [[rop-1, copp]]
        elif (board[rop][copp]).islower() != (board[rop-1][copp]).islower() :#düşman kare
            if (board[rop-1][copp]) == 'KI' or (board[rop-1][copp]) == 'ki':
                "düşman şah"
            else :
                smkl += [[rop-1,copp]]

    if rop < 7:       
        if board[rop+1][copp] == "  ":
            smkl += [[rop+1, copp]]
        elif (board[rop][copp]).islower() != (board[rop+1][copp]).islower() :#düşman kare
            if (board[rop+1][copp]) == 'KI' or (board[rop+1][copp]) == 'ki':
                "düşman şah"
            else :
                smkl += [[rop+1,copp]]

    if copp < 7:
        if board[rop][copp+1] == "  ":
            smkl += [[rop, copp+1]]
        elif (board[rop][copp]).islower() != (board[rop][copp+1]).islower() :#düşman kare
            if (board[rop][copp+1]) == 'KI' or (board[rop][copp+1]) == 'ki':
                "düşman şah"
            else :
                smkl += [[rop, copp+1]]

    if copp >0:
        if board[rop][copp-1] == "  ":
            smkl += [[rop, copp-1]]
        elif (board[rop][copp]).islower() != (board[rop][copp-1]).islower() :#düşman kare
            if (board[rop][copp-1]) == 'KI' or (board[rop][copp-1]) == 'ki':
                "düşman şah"
            else :
                smkl += [[rop, copp-1]]

    if copp < 7 and rop > 0:
        if board[rop-1][copp+1] == "  ":
            smkl += [[rop-1, copp+1]]
        elif (board[rop][copp]).islower() != (board[rop-1][copp+1]).islower() :#düşman kare
            if (board[rop-1][copp+1]) == 'KI' or (board[rop-1][copp+1]) == 'ki':
                "düşman"
            else :
                smkl += [[rop-1, copp+1]]

    if copp < 7 and rop < 7:
        if board[rop+1][copp+1] == "  ":
            smkl += [[rop+1, copp+1]]
        elif (board[rop][copp]).islower() != (board[rop+1][copp+1]).islower() :#düşman kare
            if (board[rop+1][copp+1]) == 'KI' or (board[rop+1][copp+1]) == 'ki':
                "düşman şah"
            else :
                smkl += [[rop+1, copp+1]]

    if copp >0 and rop >0 :
        if board[rop-1][copp-1] == "  ":
            smkl += [[rop-1, copp-1]]
        elif (board[rop][copp]).islower() != (board[rop-1][copp-1]).islower() :#düşman kare
            if (board[rop-1][copp-1]) == 'KI' or (board[rop-1][copp-1]) == 'ki':
                "düşman şah"
            else :
                smkl += [[rop-1, copp-1]]

    if copp >0 and rop < 7:
        if board[rop+1][copp-1] == "  ":
            smkl += [[rop+1, copp-1]]
        elif (board[rop][copp]).islower() != (board[rop+1][copp-1]).islower() :#düşman kare
            if (board[rop+1][copp-1]) == 'KI' or (board[rop+1][copp-1]) == 'ki':
                "düşman şah"
            else :
                smkl += [[rop+1, copp-1]]
    smoc(smkl)
    
def smp(x):    # pawn - piyon
    global smpl
    popi(x)
    smpl = []
    
    if x.islower() == False :
        if rop > 0 :
            if board[rop-1][copp] == "  ":
                smpl += [[rop-1, copp]]
            elif (board[rop][copp]).islower() != (board[rop-1][copp]).islower() :#düşman kare
                if (board[rop-1][copp]) == 'KI' or (board[rop-1][copp]) == 'ki':
                    "düşman şah"
                else :
                    smpl += [[rop-1,copp]]
            
    elif x.islower() == True :
        if rop < 7:
            if board[rop+1][copp] == "  ":
                smpl += [[rop+1, copp]]
            elif (board[rop][copp]).islower() != (board[rop+1][copp]).islower() :#düşman kare
                if (board[rop+1][copp]) == 'KI' or (board[rop+1][copp]) == 'ki':
                    "düşman şah"
                else:
                    smpl += [[rop+1,copp]]
    smoc(smpl)

def pri ():
    global boardstr
    boardstr = ""
    setboardf(board)
    boardstrf = "-------------------------\n"+boardstr[0:len(boardstr)-1]+"\n-------------------------"
    setboard(board)
    print(boardstrf)
    
def ini ():
    global boardstr
    global board
    boardstr = ""
    board = [['r1', 'n1', 'b1', 'qu', 'ki', 'b2', 'n2', 'r2'],['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8'],["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],['R1', 'N1', 'B1', 'QU', 'KI', 'B2', 'N2', 'R2']]
    setboardf(board)
    boardstrf = "-------------------------\n"+boardstr[0:len(boardstr)-1]+"\n-------------------------"
    print(boardstrf)
    
def move(x, y):
    popi(x)
    k = copp
    l = rop
    m = y[0]
    m = int((columns.index(m)))
    n = int(y[1])-1
    
    if x[0] == "r" or x[0] == "R":
        smr(x)
    elif x[0] == "n" or x[0] == "N":
        smn(x)
    elif x[0] == "b" :
        smbd(x)
    elif x[0] == "B":
        smbu(x)
    elif x[0] == "q" or x[0] == "Q":
        smq(x)
    elif x[0] == "k" or x[0] == "K":
        smk(x)
    elif x[0] == "p" or x[0] == "P":
        smp(x)

    if y in b:
        board[l][k] = "  "
        board[n][m] = x
        print("OK")
    else:
        print("FAILED")

for i in range(len(commands)):
    if commands[i][0] == "move":
        print("> move",commands[i][1],commands[i][2])
        move(commands[i][1],commands[i][2])
        
    if commands[i][0] == "print":
        print("> print")
        pri()
    
    if commands[i][0] == "showmoves":
        if commands[i][1][0] == "r" or commands[i][1][0] == "R":
            smr(commands[i][1])
            if b != []: 
                print("> showmoves",commands[i][1])
                print(" ".join(b))
            else :
                print("> showmoves",commands[i][1])
                print("FAILED")
        elif commands[i][1][0] == "n" or commands[i][1][0] == "N":
            smn(commands[i][1])
            if b != []: 
                print("> showmoves",commands[i][1])
                print(" ".join(b))
            else :
                print("> showmoves",commands[i][1])
                print("FAILED")
        elif commands[i][1][0] == "b" :
            smbd(commands[i][1])
            if b != []: 
                print("> showmoves",commands[i][1])
                print(" ".join(b))
            else :
                print("> showmoves",commands[i][1])
                print("FAILED")
        elif commands[i][1][0] == "B":
            smbu(commands[i][1])
            if b != []: 
                print("> showmoves",commands[i][1])
                print(" ".join(b))
            else :
                print("> showmoves",commands[i][1])
                print("FAILED")
        elif commands[i][1][0] == "q" or commands[i][1][0] == "Q":
            smq(commands[i][1])
            if b != []: 
                print("> showmoves",commands[i][1])
                print(" ".join(b))
            else :
                print("> showmoves",commands[i][1])
                print("FAILED")
        elif commands[i][1][0] == "k" or commands[i][1][0] == "K":
            smk(commands[i][1])
            if b != []: 
                print("> showmoves",commands[i][1])
                print(" ".join(b))
            else :
                print("> showmoves",commands[i][1])
                print("FAILED")
        elif commands[i][1][0] == "p" or commands[i][1][0] == "P":
            smp(commands[i][1])
            if b != []: 
                print("> showmoves",commands[i][1])
                print(" ".join(b))
            else :
                print("> showmoves",commands[i][1])
                print("FAILED")
        
    if commands[i][0] == "initialize":
        print("> initialize")
        print("OK")
        ini()
        
    if commands[i][0] == "exit":
        print("> exit")
        sys.exit()