random_list = [3.1, 105, 'Hello', 2.7, 'Python', 5.5, 'world', 'AI']

# Filter untuk memisahkan nilai Float, int, dan string
floats = list(filter(lambda x: isinstance(x, float), random_list))
ints = list(filter(lambda x: isinstance(x, int), random_list))
strings = list(filter(lambda x: isinstance(x, str), random_list))

# Map untuk Memetakan nilai int menjadi satuan, puluhan, dan ratusan
def map_ints_to_units(int_value):
    return {
        'ratusan': int_value // 100,
        'puluhan': (int_value % 100) // 10,
        'satuan': int_value % 10
    }

mapped_ints = list(map(map_ints_to_units, ints))

# Output
print("Data Float : ", floats)
print("Data Int : ", mapped_ints)
print("Data String : ", strings)
