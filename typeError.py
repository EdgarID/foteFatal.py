import Lettre as L
import Form as F
import POStagging as pos
import Syntax as S
import Grammar as G
import Punctuation as P

def test(file):
    txt=open(file)
    print(txt.read())
    
    txt.close()

def identification(file):
    """this identification is based of the Nina
    Catach's error's typologie, with the last
    two extragraphic errors and the four graphic
    one, but it's doable with any other set of
    error, based on what we'll decide."""
    ret=[0,0,0,0,0]
    txt=open(file)
    ret[0]=L.func(txt)
    ret[1]=F.func(txt)
    txtpos=pos.func(txt)
    ret[2]=S.func(txtpos)
    ret[3]=G.func(txtpos)
    ret[4]=P.func(txtpos)
    txt.close()
    return (ret)
        