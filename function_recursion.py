# ----------------------------------
# -------Function Recursion---------
# ----------------------------------

# word ="gggaaaaaamaalll"  and i need to return "gamal"


def clean(word):
    if len(word) == 1:
        return word

    print(f" start fun word : {word} ")

    if word[0] == word[1]:
        print(f" before condition : {word} ")

        return clean(word[1:])

    print(f" before return : {word} ")

    return word[0] + clean(word[1:])


# call fun
# print(clean("gggaaaaaamaalll"))

# --------------------------------------------------------------------

# ----------------------------------
# -------Function => lambda---------
# -------Anonyomus function---------
# 1- It's has no name
# 2- It can use it to return data from another fun
# 3- lambda used for simble task and def handle large task
# 4- lambda is one single expression not block of code
# 5- lambda type is function


# Normal fun
def say_hello(name, age):
    return f"Hello {name} and your age is : {age} "


print(say_hello("gamal", 26))


# lambda fun
Hello = lambda name, age: f"Hello {name} and your age is : {age}"

print(Hello("gamal", 26))


print(type(Hello))  # <class 'function'>

print(say_hello.__name__)  # say_hello
print(Hello.__name__)  # <lambda>
