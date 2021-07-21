
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b%a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g == 1:
        return x % m


p = int(input("input p : "))
q = int(input("input q : "))
e0 = int(input("input e0 : "))
e1 = e0**int((p-1)/q) % p
d = int(input("input d : "))
e2 = e1**d % p

hM = 5000
r = 61

n = p*q
pn = (p-1)*(q-1)

re = modinv(r, q)

s1 = (e1**r % p) % q
s2 = (hM+d*s1)*re % q

s2e = modinv(s2, q)

v = ((e1**(hM*s2e) * e2**(s1*s2e)) % p) % q

print("e1 : ", e1)
print("e2 : ", e2)
print("s1 : ", s1)
print("s2 : ", s2)
print("s2e : ", s2e)

print("v : ", v)

if s1 == v:
    print("The signature is valid")
else:
    print("The signature is not valid")

