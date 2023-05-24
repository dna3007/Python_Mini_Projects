email = input("Enter an Email Address : ")
k,j,d=0,0,0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count('@')==1):
            if (email[-4]=='.') ^ (email[-3]=="."):     #^ xor what if both . at -4 and -3 posison
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("wrong Email (wrong syntax)")
            else:
                print(" wrong Email (\".\"is not at -4 or -3 posison )")
        else:
            print(" Wrong Email (there is no @ or more than one @) ")
    else:
        print(" Wrong Email (First letter should be alpha)")
else:
    print(" Wrong Email (required length is must be >= 6)")