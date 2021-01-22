class Converter:

    def convert_miles_to_km(self, user_input):
        miles = float(user_input.get())
        km = round(miles * 1.609, 2)
        return km
