#Utwórz listę zawierającą wartości poniższego słownika, bez duplikatów.

days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}

days_keys_s = (set(days.keys()))
days_values_s =(set(days.values()))
daysfinal = list(days_keys_s) + list(days_values_s)

print(daysfinal)