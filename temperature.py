def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def describe(c):
    if c >= 35:
        return "Hot"
    elif c >= 25:
        return "Warm"
    elif c >= 15:
        return "Mild"
    else:
        return "Cold"

if __name__ == "__main__":
    for c in [0, 18, 28, 37]:
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C = {round(f, 1)}°F -> {describe(c)}")
    print(f"98.6°F = {round(fahrenheit_to_celsius(98.6), 1)}°C")