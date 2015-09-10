bob_count = 0

for i in range(len(s) - 2):
  if s[i:(i+3)] == 'bob':
    bob_count += 1

print bob_count
