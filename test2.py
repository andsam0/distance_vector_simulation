from router import Router 

a = Router("a")
b = Router("b")
c = Router("c")
d = Router("d")
e = Router("e")


a.add_neighbour(b,200)
a.add_neighbour(c,2)

b.add_neighbour(a,200)
b.add_neighbour(c,2)
b.add_neighbour(d,1)
b.add_neighbour(e,20)

c.add_neighbour(a,2)
c.add_neighbour(b,2)
c.add_neighbour(e,1)

d.add_neighbour(b,1)

e.add_neighbour(b,20)
e.add_neighbour(c,1)

print("TAB A", a.table)
print("|")
print("TAB B", b.table)
print("|")
print("TAB C", c.table)
print("|")
print("TAB D", d.table)
print("|")
print("TAB E", e.table)

a.send_table()
b.send_table()
c.send_table()
d.send_table()
e.send_table()


a.update_table()
b.update_table()
c.update_table()
d.update_table()
e.update_table()

print("UPDATED")
print("TAB A", a.table)
print("|")
print("TAB B", b.table)
print("|")
print("TAB C", c.table)
print("|")
print("TAB D", d.table)
print("|")
print("TAB E", e.table)

a.update_table()
b.update_table()
c.update_table()
d.update_table()
e.update_table()

print("UPDATED")
print("TAB A", a.table)
print("|")
print("TAB B", b.table)
print("|")
print("TAB C", c.table)
print("|")
print("TAB D", d.table)
print("|")
print("TAB E", e.table)

    