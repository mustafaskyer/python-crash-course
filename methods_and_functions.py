# fn
name = "Name";

name = name.upper();

print(name);
print("name len", len(name));

# replace
name = name.replace("NAM", "Welcom");
print("replaced string ", name);


sentence = "Hi my name is Mu and I am 25. years old"
print("Splitted Sentence", sentence.split(". "));


# indexing string
hello = "Hello World"
last_char = hello[-4];
five_chars = hello[0:5];
last_five_chars = hello[-5:0];
print("Indexing last char", last_char);
print("Indexing five char", five_chars);
print("Indexing last five char", last_five_chars);