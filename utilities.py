# import settings.py
import settings

# create function to calculate percentage of HEIGHT
def height_prct(percentage):
    return (settings.HEIGHT / 100) * percentage

print(height_prct(25))