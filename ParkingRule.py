class ParkingRule:
    def __init__(self, date_specs, weekday_specs, hour_specs, duration_minutes, parking_indicator):
        self.date_specs = date_specs
        self.weekday_specs = weekday_specs
        self.hour_specs = hour_specs
        self.duration_minutes = duration_minutes
        self.parking_indicator = parking_indicator  # 0 -> no parking, 1 -> parking, 2 -> pay to park

    def display_parking_rule(self):
        return "Date Specs: ", self.date_specs, ", Weekday specs: ", self.weekday_specs, ", Hour Spec: ", self.hour_specs, ", Duration minutes: ", self.duration_minutes, ", Pay To Park: ", self.parking_indicator
