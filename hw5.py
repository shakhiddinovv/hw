def abs(**args):
    return (args)
print(abs(a = 'Hello', b = 'ABC' ))

def calculator(a, b, action):
    if action == 'add': return eval(f'{a} + {b}')
    if action == 'subtract': return eval(f'{a} - {b}')
    if action == 'multiply': return eval(f'{a} * {b}')
    if action == 'divide': return eval(f'{a} / {b}')
print(calculator(2, 3, 'add'))
print(calculator(2, 3, 'subtract'))

def multiplyMatrix(a, b, c, d):
    return eval(f'{a} * {d}, {b} * {d}, {c} * {d}')
print(multiplyMatrix({1, 2, 3}, 4))

def convertTemp(a, temp1, temp2):
    if temp1 == 'C' and temp2 == 'F':
        return eval(f'({a} * 1.8) + 32')
    if temp1 == 'F' and temp2 == 'C':
        return eval(f'({a} - 32) / 1.8')
print(convertTemp(30, 'C', 'F'))    
print(convertTemp(86, 'F', 'C'))

def calcQuadFunc(x):
    if x >= 0: return eval(f'({x} ** 2) + (2 * {x}) -3')
    else: return eval(f'({-x} ** 2) - (2 * {x}) - 3')
print(calcQuadFunc(1))


def nearest_value(nums, target):
    if len(nums) == 0: return 'Error'
    nums = list(nums)
    distances_to_target = []
    for num in nums:
        distances_to_target. append(abs(target - num))
    print(nums[distances_to_target.index(min(distances_to_target))])
print(nearest_value({4, 7, 10, 11, 12, 15}, 9))

def correct_sentence(sentence: str):
    if sentence != "Greetings, friends.":
        return "Greetings, friends."
    else: pass
print(correct_sentence("greetings, friends."))
print(correct_sentence("Greetings, friends."))