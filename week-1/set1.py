s = 'zdxcpfopp'
# count = 0
# for letter in s:
#     if letter in 'aeiou':
#         count += 1
# print(count)
# count = 0
# while True:
#     index = s.find('bob')
#     if index == -1:
#         break
#     else:
#         count += 1
#         s = s[index + 1:]
# print(count)
# print('a' <= 'b') # True
longest_world_alphabetical_order = ''
world_alphabetical_order = ''
for x in range(len(s)):
    sub_world = s[x:]
    if len(longest_world_alphabetical_order) < len(world_alphabetical_order):
        longest_world_alphabetical_order = world_alphabetical_order
    world_alphabetical_order = ''

    for letter in sub_world:
        if len(world_alphabetical_order) == 0:
            world_alphabetical_order = letter
            continue
        if world_alphabetical_order[-1] <= letter:
            world_alphabetical_order = world_alphabetical_order + letter
        else:
            if len(world_alphabetical_order) > len(longest_world_alphabetical_order):
                longest_world_alphabetical_order = world_alphabetical_order
            world_alphabetical_order = letter
if len(longest_world_alphabetical_order) == 0:
    longest_world_alphabetical_order == world_alphabetical_order
print(longest_world_alphabetical_order)
