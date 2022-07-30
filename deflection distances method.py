#offsets method

#deflection distances method
from math import*
def whole_val_inc(p):
    x=p//1
    while(x%20!=0):
        x+=1
    return x
def whole_val_dec(n):
    c=n//1
    while(c%20!=0):
        c-=1
    return c

R=float(input("enter radius in meters :"))
delt=float(input("enter delta value in decimals :"))
CH_pi=float(input("enter chainage of PI :"))
T=(4*R*tan(delt/2))
C=20
print("tangent length  =",T)
len_curv=(3.14*R*delt)/180
print("length of curve  =",len_curv)
CH_pc=CH_pi-T
print("chainage of point of curvature =",CH_pc)
CH_pt=CH_pc+len_curv
print("chainage of point of tangency =",CH_pt)
len_frst_sub_chord=whole_val_inc(CH_pc)-CH_pc
print("length first sub chord  =",len_frst_sub_chord)
len_last_sub_chord=CH_pt-whole_val_dec(CH_pt)
print("length of last sub chord =",len_last_sub_chord)
no_of_full_chrd=(whole_val_dec(CH_pt)-whole_val_inc(CH_pc))/20
print("no. of full chords  =",no_of_full_chrd,"of 20 meter length")
print("total no. of chords =",no_of_full_chrd+2)
o1=(len_frst_sub_chord*len_frst_sub_chord)/(2*R)
print("length of first offset =",o1)
o2=(C/(2*R))*(len_frst_sub_chord+C)
print("lengt of second offset =",o2)
o=(C*C)/(R)
print("O3 ,O4 ,O5.......  =",o)
o_lst=(len_last_sub_chord/(2*R))*(C+len_last_sub_chord)
print("lengt of last offset =",o_lst)
