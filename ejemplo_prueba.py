samurai="jor ge"
print(len(samurai))
print(len(samurai.strip()))
print(len(samurai.replace(" ","" )))
while True:
    if samurai.find(" "):
        print("NO debe ir con espacios")