class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds

    def get_orbital_value(self, factor):
        return round(((self.seconds / 60) / 1440) / (365.25 * factor), 2)

    def on_mercury(self):
        return self.get_orbital_value(0.2408467)

    def on_venus(self):
        return self.get_orbital_value(0.61519726)

    def on_earth(self):
        return self.get_orbital_value(1)

    def on_mars(self):
        return self.get_orbital_value(1.8808158)

    def on_jupiter(self):
        return self.get_orbital_value(11.862615)

    def on_saturn(self):
        return self.get_orbital_value(29.447498)

    def on_uranus(self):
        return self.get_orbital_value(84.016846)

    def on_neptune(self):
        return self.get_orbital_value(164.79132)
