import ru_local as ru


# Output the title heading
print(ru.title_heading)

# Output the input data
print(ru.oil_in_gasoline, ru.gasoline_combustion, ru.gasoline_in_BTU)
print(ru.ethanol_in_energy, ru.gasoline_cost)

# User enters his value (gasoline volume in gallons)
print(ru.user_input_value, end='')
gallon = float(input())


# Volume of gasoline in liters
liter = round((gallon * 3.785), 2)
print(ru.gallon_in_litres, liter)

# Number of barrels of oil for this volume of gasoline
barrel = round((gallon / 19.5), 2)
print(ru.gallon_in_barrels, barrel)

# The volume of carbon dioxide when this gasoline is burned in the engine
car_dio = gallon * 20
print(ru.gallon_in_car_dio, car_dio)

# Equivalent volume of ethanol
ethanol = round(((gallon * 11500) / 75700), 2)
print(ru.gallon_in_ethanol, ethanol)

# Cost in US dollars
gallon_cost = round((gallon * 3.0), 2)
print(ru.gallon_in_dol, gallon_cost)

