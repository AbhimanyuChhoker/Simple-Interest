# SI = P * R * T / 100
p = int(input("Principal:"))
r = int(input("Rate of Interest:"))
t = int(input("Time(In years):"))


def si(principal, rate, time):
    simple_interest = principal * rate * time / 100
    print("Simple Interest: ", simple_interest)
    return simple_interest


si(p, r, t)
