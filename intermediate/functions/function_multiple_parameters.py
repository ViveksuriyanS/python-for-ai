def is_all_rounder(can_bat, can_bowl, can_field):
    if can_bat and can_bowl and can_field:
        print("All-rounder")
    else:
        print("Not an all-rounder")

# Example usage
is_all_rounder(True, True, True)
is_all_rounder(True, False, True)
