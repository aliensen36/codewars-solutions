sentence = "adsfjewfn fuiyedcf  ewqiurqew fwequifg"

def get_count(sentence):
    return sum(char in 'aeiou' for char in sentence)

print(get_count(sentence))