
#half widths
half_widths = [
    0, 5.4, 7.7, 11.5, 12.9, 14.2, 15, 16,
    16.4, 17, 17.6, 17.8, 17.9, 17.9, 17.8, 18, 18.1, 
    17.8, 17.5, 16.9, 15.6, 14.3, 12.8, 11, 9.3, 7.5, 
    5.9, 4.5, 2.7, 1, 0
]

dx = 10          # spacing along ship (meters)
deck_height = 3  # meters


#simpsons coefficients

n = len(half_widths) - 1

if n % 2 != 0:
    raise ValueError("Number of intervals must be even.")

weights = []

for i in range(n + 1):
    if i == 0 or i == n:
        weights.append(1)
    elif i % 2 == 1:
        weights.append(2)
    else:
        weights.append(4)


 
#Halfarea

half_area = dx * sum(f * w for f, w in zip(half_widths, weights)) / 3

#totals

total_area = 2 * half_area
half_volume = half_area * deck_height
total_volume = 2 * half_volume


#output

print("Weights:", weights)
print(f"Half area: {half_area:.5f} m^2")
print(f"Total area: {total_area:.5f} m^2")
print(f"Half volume: {half_volume:.5f} m^3")
print(f"Total volume: {total_volume:.5f} m^3")
deck_e_area = total_area
deck_e_vol = total_volume