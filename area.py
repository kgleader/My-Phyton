def rect(d1, d2):
  area = d1 * d2
  perimeter = 2 * d1 + 2 * d2
  return area, perimeter

x, y = rect(5, 3)
print("Area:", x)
print("Perimeter:", y)