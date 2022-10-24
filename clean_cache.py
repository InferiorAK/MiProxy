import shutil
try:
    shutil.rmtree("__pycache__")
except FileNotFoundError:
    pass
try:
    shutil.rmtree("core/__pycache__")
except FileNotFoundError:
    pass
try:
    shutil.rmtree("core/res/__pycache__")
except FileNotFoundError:
    pass