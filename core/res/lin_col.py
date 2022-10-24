# Color

# Linux
r = "\x1b[1;31m"
g = "\x1b[1;32m"
y = "\x1b[1;33m"
# b = "\x1b[1;34m"
# p = "\x1b[1;35m"
# c = "\x1b[1;36m"
# w = "\x1b[1;37m"

def col(r,g,b,txt):
    return "\033[1;38;2;{};{};{}m{} \033[1;38;2;255;255;255m".format(r,g,b,txt)