main:
@t0 = 5 INT
- INT a
a = @t0 INT
@t1 = 3 INT
@t2 = - @t1 INT
- INT b
b = @t2 INT
@t3 = 'x' CHAR
- CHAR x
x = @t3 CHAR
@t4 = 'w' CHAR
- CHAR y
y = @t4 CHAR
- INT c
@t5 = a + b INT
c = @t5 INT
@t6 = 2 INT
@t7 = c == @t6 INT
if @t7 GOTO #L1 else GOTO #L2
#L1:
- INT l
l = 1 INT
@t8 = x - l CHAR
x = @t8 CHAR
GOTO #L0
#L2:
@t9 = x - y CHAR
@t10 = 'a' CHAR
@t11 = @t9 - @t10 CHAR
x = @t11 CHAR
#L0:
print x CHAR
end: