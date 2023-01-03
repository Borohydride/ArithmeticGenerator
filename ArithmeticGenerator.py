import os,sys
os.chdir(sys.path[0])

#configure
maxnum=100
quantity=100
outfile=('ariths.html','ans.html')

import random,fractions,markdown
getnum=lambda:random.randint(1,maxnum)

getsymbol=lambda:random.choice(("+","-",r"\times",r"\div"))

def getarith():
    nums=(getnum(),getnum(),getnum(),getnum())
    symbol=getsymbol()
    arith=r"$\frac{"+str(nums[0])+"}{"+str(nums[1])+"}"+symbol+r"\frac{"+str(nums[2])+"}{"+str(nums[3])+"}=$"
    
    fraction1=fractions.Fraction(nums[0],nums[1])
    fraction2=fractions.Fraction(nums[2],nums[3])

    if symbol=="+":
        ans=fraction1+fraction2
    elif symbol=="-":
        ans=fraction1-fraction2
    elif symbol==r"\times":
        ans=fraction1*fraction2
    elif symbol==r"\div":
        ans=fraction1/fraction2
    
    ansstr=str(ans)

    if '/' in ansstr:
        ansla=r"$\frac{"+"}{".join(ansstr.split('/'))+"}$"
        if '-' in ansstr:
            ansla=r'-\frac{'.join(ansla.split(r'\frac{-'))
    else:
        ansla="$"+ansstr+"$"
    
    return arith,ansla


ariths=[]
anslas=[]
for i in range(1,quantity+1):
    arith,ansla=getarith()
    ariths.append('$'+str(i)+'.$ '+arith)
    anslas.append('$'+str(i)+'.$ '+arith+ansla)

arithstr="\n\n".join(ariths)
anslastr="\n\n".join(anslas)



from markdown import markdown
from mdx_math import MathExtension
def md2html(mdtext):
    html = '<!DOCTYPE html><body><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex/dist/katex.min.css" rel="external nofollow"  crossorigin="anonymous"><script src="https://cdn.jsdelivr.net/npm/katex/dist/katex.min.js" crossorigin="anonymous"></script><script src="https://cdn.jsdelivr.net/npm/katex/dist/contrib/mathtex-script-type.min.js" defer></script>{}</body></html>'
    text = markdown(mdtext, output_format='html', extensions=[MathExtension(enable_dollar_delimiter=True)])  # MarkDown转HTML
    html = html.format(text)
    return html

with open(outfile[0],'w',encoding='utf-8') as f:
    f.write(md2html(arithstr))
with open(outfile[1],'w',encoding='utf-8') as f:
    f.write(md2html(anslastr))

