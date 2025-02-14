import chardet

with open(r"week_assignment\week4,5.py\encodinf_check.csv", "rb") as f:
    result = chardet.detect(f.read())
    print(result['encoding'])
