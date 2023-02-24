s=str(input())
t=s[s.find('h')+1:s.rfind('h')]
t=t.replace('h', 'H')
print(s[:s.find('h')+1]+t+s[s.rfind('h'):])