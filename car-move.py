import movement as m

p = 0
tf = 1.6
while p == 0:
        a = raw_input('')

        if a == 'w':
                m.forward(tf)
        if a == 's':
                m.reverse(tf)
        if a == 'd':
                m.right(tf)
        if a == 'a':
                m.left(tf)
        if a == 'p':
                p = 1
