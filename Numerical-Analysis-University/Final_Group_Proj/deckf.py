
#half widths
half_widths = [
    0, 3, 5.4, 8.1, 10.5, 11.4, 12.9, 14.3,
    15.7, 16.4, 17.5, 18.3, 18.8, 18.9, 19.2,
    19.0, 19.0, 18.5, 17.6, 16.8, 16.7, 14.0, 12.4,
    10.4, 8.4, 6.6, 5.1, 2.9, 1.7, 0.7, 0.0
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
deck_f_area = total_area
deck_f_vol = total_volume