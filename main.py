import Stamp_Collection as Stamp


def main():
    stamp1 = Stamp.GroupII("Shot Putt", 75, 1984)
    stamp2 = Stamp.GroupII("Men's Gym", 100, 1984)
    stamp3 = Stamp.GroupII("Weight Lift", 150, 1984)
    stamp4 = Stamp.GroupI("Niagara Falls", 80, 1999)
    stamp5 = Stamp.GroupI("Acadia MAine", 60, 2000)
    stamp6 = Stamp.GroupI("Yosemite", 84, 2001)
    stamp7 = Stamp.GroupI("Mile Woods", 72, 2007)
    phil = Stamp.Philatelist()
    phil.set_name("Philip Hathaway")
    # Add Philatelist's stamps
    phil.add_stamp(stamp1)
    phil.add_stamp(stamp2)
    phil.add_stamp(stamp3)
    phil.add_stamp(stamp4)
    phil.add_stamp(stamp5)
    phil.add_stamp(stamp6)
    phil.add_stamp(stamp7)
    print("The total commercial value of the Philatelist's stamps is: $" +
          str(phil.calculate_total_commercial_value() / 100))


main()
