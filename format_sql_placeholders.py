def format_placeholders(s,args):
    a=s.count("?")
    if a!=len(args):
        raise ValueError("Unmatching ammount of args.")
    for i in args:
        n=s.find("?")
        if type(i)==str:
            s=s[:n]+"'"+i+"'"+s[n+1:]
        else:
            s=s[:n]+str(i)+s[n+1:]
    return s

o=format_placeholders("SELECT * FROM [TEST] WHERE XYZ=? and X=? and Z=? and q=?;",[1,2,3,"sad"])
print(o)
