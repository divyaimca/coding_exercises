def count_substring(string, sub_string):
    import re
    #return len(re.findall('(?={0})'.format(re.escape(sub_string)), string))

    count = start = i = 0
    end = len(sub_string)
    
    while i < len(string):
        print(string[start:end])
        if string[start:end] == sub_string:
            count += 1
        start += 1
        i += 1
        end += 1
        
    return count

print(count_substring('ABCDCDC','CDC'))