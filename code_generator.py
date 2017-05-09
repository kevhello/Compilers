import re


def code_generator(source, filename):
    """
    Generates source code from input source code
    
    :param source: A list. Contains the source code (where each line is an element of the list)
    :param filename: The name of the file you want to output the generated source code to
    :return: Returns True upon successful completion
    """
    # Stores the string to be written to the file.
    content = ''
    
    # Allows us to enter vars after main() declaration
    # is sub-optimal, but w/e
    vars = ""

    # Go through each line, converting it to C++
    for line in source:
        if re.match(r'PRINT', line):
            line = re.sub(r'PRINT\s*\(', '\tcout <<', line, 0)
            line = re.sub(r'\)\s*;', '<< endl ;\n', line, 0)
            content += line
            continue

        if re.match(r'^PROGRAM', line):
            content += '#include <iostream>\nusing namespace std ;\n'
        elif re.match(r'^BEGIN', line):
            content += 'int main()\n{\n'
            content += "\t" + vars + "\n"
        elif re.match(r'^INTEGER', line):
            vars = re.sub(r'INTEGER\s*:', 'int', line)
            #line = re.sub(r'INTEGER\s*:', 'int', line)
            #content += line + '\n'
        elif re.match(r'^(P|Q|R|S)+(P|Q|R|S|[0-9])*', line):
            content += '\t' + line + '\n'
        elif re.match(r'END\.', line):
            content += '\treturn 0 ;\n}'

    # Write the code generated to the file
    file = open(filename, mode='w')
    file.writelines(content)
    file.close()

    return True
