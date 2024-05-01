sample_list = [2, 3, 4]
ada_3_disitu = 3 in sample_list

sample_tuple = ("hello", "python")
ada_hello_disitu = "hello" in sample_tuple

sample_dict = { "nama": "adha", "age": 23 }
is_age = 23 in sample_dict

sample_set = { "free", "tomorrow" }
is_free = "free" in sample_set

print("Sample list: %r" % (ada_3_disitu));
print("Sample tuple: %r" % (ada_hello_disitu));
print("Sample dict: %r" % (is_free));
print("Sample set: %r" % (is_age));
