fn1=0
fn2=1
fn3=0
print(fn1)

print(fn2)

while (fn1+fn2)<=100:
    fn3=fn1+fn2
    fn1=fn2
    fn2=fn3
    print(fn3)