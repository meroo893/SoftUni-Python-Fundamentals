countries = input().split(", ")
capitals = input().split(", ")
combined = zip(countries, capitals)

combined = dict(combined)
"ZIP OBJECT MUST BE CONVERTED INTO DICTIONARY"

for country, capital in combined.items():
    print(f"{country} -> {capital}")
