user_inp = ""
resultant, final = "", ""
sub_block_num = 1
main_flag = True
outer_indent = 2
indent = 0

def printing(user_inp, indent_num):
    #fn_string += repeat_tree()
    user_inp = input()
    fn_string = " "*indent_num + "-"*indent_num + ">" + user_inp + "\n"
    #print(fn_string)
    return fn_string

def block(outer_indent, user_inp, final):
    temp_str = printing(user_inp, outer_indent)
     #print(final)
    return temp_str

def sub_block(sub_block_num, user_inp, final):
    temp_str = printing(user_inp, sub_block_num*2)
    return temp_str

def label(sub_block_num, user_inp, final):
    temp_str = printing(user_inp, (sub_block_num*2)+4)
    return temp_str

def display():
    print(resultant)

def input_handler(user_inp, final, sub_block_num=sub_block_num):
    if user_inp == 'b':
        print("Block created.")
        final = block(outer_indent, user_inp, final)
        user_inp = input()
        if user_inp == 'sub-b':
            print("Sub block created")
            sub_block_num += 1
            final += sub_block(sub_block_num, user_inp, final)
            return final
        elif user_inp == 'label':
            print("Label section created")
            final += label(sub_block_num, user_inp, final)
            return final
    
    if user_inp == 'disp':
        display()
        exit()

while main_flag:
    user_inp = input()
    resultant += input_handler(user_inp, final)
