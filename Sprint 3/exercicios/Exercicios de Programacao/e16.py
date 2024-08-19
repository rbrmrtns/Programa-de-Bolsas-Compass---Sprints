# %%

'''
Escreva uma função que recebe uma string de números
separados por vírgula e retorne a soma de todos eles. Depois
imprima a soma dos valores.
'''

def soma_nums_string(str):
    nums = str.split(',')
    result = 0
    
    for i in range(len(nums)):
        result += int(nums[i])
        
    return result
    
print(soma_nums_string("1,3,4,6,10,76"))

# %%