import os


class Plugin():
    def __init__(self, name):
        self.folder_name = name
        self.filename = "core_" + str(self.folder_name)
        self.path = f"Plugins/{self.folder_name}/"
    path = ""
    filename = ""
    folder_name = ""

    def info(self):
        print(f"folder_name {self.folder_name}\nfilename {self.filename}\npath {self.path}")


class Plugger():

    def __pluginInclude(self):
        if os.path.isdir("Plugins"):

            plugin_folders = os.listdir("Plugins")

            for folder_name in plugin_folders:
                plugin = Plugin(folder_name)

                if self.__checkFile(plugin):
                    locals()[folder_name] = plugin
                    self.__installed.append(locals()[folder_name])

    def plug(self):
        self.__pluginInclude()
        return self.__installed

    def __checkFile(self,plugin):
        arg = str(plugin.path) + str(plugin.filename) + ".py"
        if os.path.isfile(arg):
            return True
        return False


    __installed = []


# pl = Plugger()
# print(pl.plug())
# print(os.listdir("Plugins"))
# #
# h = Plugin("Hentai")
# h.info()

def g():
    print("mmmm......")