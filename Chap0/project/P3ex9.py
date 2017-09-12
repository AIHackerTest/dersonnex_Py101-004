formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4)) #format is a function,which calling it to replace {}
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
)) 