'''
For total_lines_of_code_in_snippets_daily = 3 4 4 1 5 3 4 the output should be 4

As you can see here, there are 3 code snippets with 4 Lines of code in each occurs at index 1 ,2 and 6. At the same time there are 2 code snippets with 3 Lines of Code Occurs at index 0 and 5 so the smaller index among the second occurence of twin code snippet is 2 hence the output is 4, i.e value at index 2.

If no such code snippet exist with similar lines of code output -1.
'''

# def twin_code(codes):
#     lines = {}
#     for i, code in enumerate(codes):
#         if code not in lines.keys():
#             lines[code] += 1
#         else:
#             lines[code] = 0
    
#     if max(lines.values()) <=1:
#         return -1
    
#     twin_codes = [lines.keys() for ]

def twin_code(lines):
    seen = set()

    for i, x in enumerate(lines):
        if x in seen:
            return x
        else:
            seen.add(x)

    return -1
