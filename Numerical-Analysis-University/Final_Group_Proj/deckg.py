
#half widths
half_widths = [
   2.7,5.3,7.8,0,0,0,0,0,0,0,0,0,0,0,0,
   0,0,0,0,0,11.6,9.6,7.7,6,4.6,3.4,0,0,0,0,0
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

target_half_area = 3605.86667
target_sumproduct = target_half_area * 3 / 10

actual_sumproduct = sum(f * w for f, w in zip(half_widths, weights))

print("Target SUMPRODUCT:", target_sumproduct)
print("Actual SUMPRODUCT:", actual_sumproduct)
print("Difference:", actual_sumproduct - target_sumproduct)

 
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
deck_g_area = total_area
deck_g_vol = total_volume