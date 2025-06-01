# s = open('24_13715.txt').readline()

# l = 0
# k = 0
# m = 0

# for r in range(len(s) - 1):
#     if s[r] + s[r + 1] == 'AB':
#         k += 1
        
#     print(m)    
        
#     while k > 50:
#         if s[l] + s[l + 1] == 'AB':
#             k -= 1
#         l += 1
#     m = max(m, r - l + 1)

# print(m)


s = open('24_13715.txt').readline()

l = 0
k = 0
m = 0

for r in range(1, len(s)):
    if s[r - 1] + s[r] == 'AB':
        k += 1
        
    #print(m)    
    while k > 50:
        if s[l] + s[l + 1] == 'AB':
            k -= 1
        l += 1
    m = max(m, r - l + 1)

print(m)