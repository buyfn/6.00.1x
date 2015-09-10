#s = 'azcbobobegghakl'
#s = 'pqtpqlqejruenwmnsbkvnqow'

current_streak = longest_streak = 0
current_streak_start = current_streak_end = longest_streak_start = longest_streak_end = 0

#print s

for i in range(len(s) - 1):
  #print i, current_streak_start, current_streak_end
  if s[i + 1] >= s[i]:
    current_streak += 1
    current_streak_end = i + 1
    if current_streak > longest_streak:
      longest_streak = current_streak
      longest_streak_start = current_streak_start
      longest_streak_end = current_streak_end
  else:
    current_streak = 0
    current_streak_start = i + 1

print('Longest substring in alphabetical order is: ' + s[longest_streak_start:longest_streak_end + 1])
