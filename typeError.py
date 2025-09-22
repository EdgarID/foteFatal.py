import wordCut as cut
import extraGraphic as oral
import phonoGrammic as phon
import morphoGrammic as morph
import logoGrammic as logo
import ideoGrammic as ideo

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
    ret=[False,False,False,False,False,False]
    txt=open(file)
    ret[0]=cut.func(txt)
    ret[1]=oral.func(txt)
    ret[2]=phon.func(txt)
    ret[3]=morph.func(txt)
    ret[4]=logo.func(txt)
    ret[5]=ideo.func(txt)
    txt.close()
    return (ret)
        