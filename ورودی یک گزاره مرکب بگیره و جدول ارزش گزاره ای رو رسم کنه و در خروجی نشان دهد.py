expr = "p and not q"

print("جدول ارزش گزاره:")
print("p | q |", expr)
print("-----------------")

for p in [0,1]:
    for q in [0,1]:
        val = eval(expr, {}, {"p": bool(p), "q": bool(q)})
        print(p, "|", q, "|", int(val))