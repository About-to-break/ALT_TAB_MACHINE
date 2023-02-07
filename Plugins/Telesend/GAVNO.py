import importlib

# Contrived example of generating a module named as a string
modulename = "plugger"

# The file gets executed upon import, as expected.
mymodule = __import__(modulename)

# Then you can use the module like normal



