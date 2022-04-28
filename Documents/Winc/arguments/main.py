# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line
# if'<name>'in msg:
# print(msg.index('<'), (msg.index('<')+5))

def greet(name, welcome="Hello, <name>!"):
    greeting = welcome.replace("<name>", name)
    return greeting


greet("Tijmen", "Hoe gaat het, <name>?")

# _________________________________________________________________________________________

gravity = {
    "sun": 274,
    "jupiter": 24.9,
    "neptune": 11.1,
    "saturn": 10.4,
    "earth": 9.8,
    "uranus": 8.9,
    "venus": 8.9,
    "mars": 3.7,
    "mercury": 3.7,
    "moon": 1.6,
    "pluto": 0.6,
}


def force(mass, body="earth"):
    f = round(float(mass) * gravity[body], 2)
    return f


force(100, "sun")

# _________________________________________________________________________________________


def pull(m1, m2, d):

    Fp = (6.674 * (10**-11)) * (float(m1) * float(m2)) / (float(d) ** 2)
    # Fp = ((float(m1) * float(m2)))/(float(d)**2)
    return Fp


pull(800, 1500, 3)
