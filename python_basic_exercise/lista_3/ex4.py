city_a=80000
city_b=200000
i=0

while city_a<=city_b:
    city_a+=city_a*0.03
    city_b+= city_b*0.015
    i+=1
    print(f"{city_a} {city_b}")

print(f"levou {i} anos")



