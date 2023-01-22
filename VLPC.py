#!/usr/bin/python3
import sys

encoding="UTF-8"
key=bytes(input("Enter the key: "),encoding)
lk=len(key)
ed = input("Enter e to encrypt or d to decrypt: ")
if ed=="e":
    plain=bytes(input("Enter the text: "),encoding)
    lp=len(plain)
    lpmo=lp-1
    ip=0
    ik=0
    while ip<lp:
        sys.stdout.write(str(plain[ip]^key[ik])+("," if ip<lpmo else ""))
        ip+=1
        ik+=1
        if ik==lk:
            ik=0
elif ed=="d":
    allnumbers = input("Enter the numbers: ").split(",")
    la=len(allnumbers)
    ia=0
    ik=0
    while ia<la:
        allnumbers[ia]=int(allnumbers[ia])^key[ik]
        ia+=1
        ik+=1
        if ik==lk:
            ik=0
    print(bytes(allnumbers).decode(encoding))
else:
    print("Unrecognized option.")
