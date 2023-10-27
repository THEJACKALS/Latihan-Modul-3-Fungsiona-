def convert_to_minutes(time_string):
    time_units = time_string.split(" ")
    weeks = int(time_units[0]) if "minggu" in time_string else 0
    days = int(time_units[2]) if "hari" in time_string else 0
    hours = int(time_units[4]) if "jam" in time_string else 0
    minutes = int(time_units[6]) if "menit" in time_string else 0

    total_minutes = weeks * 7 * 24 * 60 + days * 24 * 60 + hours * 60 + minutes
    return total_minutes

data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]

output_data = [convert_to_minutes(time) for time in data]
print(output_data)
