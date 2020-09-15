IDENTICAL = -1 
def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between 
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    length_line1 = len(line1)
    length_line2 = len(line2)
    shorter_length = min(length_line1, length_line2)
    i = 0
    while i < shorter_length:
        if line1[i] != line2[i]:
            return i
        i += 1
    if length_line1 == length_line2:
        return IDENTICAL
    else:
        return shorter_length

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.
      
      If either input line contains a newline or carriage return, 
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    for i in line1:
        if i == '\n':
            return ""
    for i in line2:
        if i == '\n':
            return ""
    shorter = min(len(line1), len(line2))
    if idx < 0 or idx > shorter:
        return ""
    str = "" 
    i = 0
    while i < idx:
        str += "="
        i += 1
    str += "^"
    return line1 + '\n' + str + '\n' + line2 + '\n'

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.
      
      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    shorter = min(len(lines1), len(lines2))
    i = 0
    while i < shorter:
        diff = singleline_diff(lines1[i], lines2[i])
        if diff != IDENTICAL:
            return (i, diff )
        i += 1
    if len(lines1) == len(lines2):
            return (IDENTICAL, IDENTICAL)
    else:
        return (i, 0) 

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or 
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    list_of_lines = []
    file = open(filename, 'r')
    file = file.readlines()
    for lines in file:
        list_of_lines.append(lines.strip())
    return list_of_lines
def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    list1 = get_file_lines(filename1)
    list2 = get_file_lines(filename2)
    (c1, c2) = multiline_diff(list1, list2)
    if c1 != -1 and c2 != -1:
        return_line = singleline_diff_format(list1[c1], list2[c1], c2)
        return "Line " + str(c1) + ':\n' + return_line
    return "No differences\n"
         
