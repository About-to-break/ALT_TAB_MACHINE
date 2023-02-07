import pyfiglet, serial
from colorama import init, Fore
from keyboard import press_and_release
from datetime import datetime
from importlib.machinery import SourceFileLoader


# Global constants
VER = "V.0.3.2"

def createDefaultPort():
    fl = open("save.dat","w")
    new_default = 0
    while (not(new_default)):
        try:
            new_default = int(input(Fore.BLUE + "default port number: "))
        except ValueError:
            print(Fore.LIGHTRED_EX + "Invalid port number, try again!")
    fl.write(str(new_default))
    fl.close()
    return new_default
def checkForExistenceOfDeafultPort():
    try:
        fl = open("save.dat","r+")
    except FileNotFoundError:
        fl = open("save.dat","w+")
    default_port = fl.readline()
    fl.close()
    try:
        default_port = int(default_port)
    except ValueError:
        print(Fore.LIGHTYELLOW_EX + "Can't find a default port number, let's make it!")
        default_port = createDefaultPort()
    return default_port
def presetSelection():
    command =input(Fore.LIGHTWHITE_EX + "Choose a preset:\na - for alt + tab (default)\nd - for win + d (notifications won't show)\nw - for win key\n")
    if command == "a":
        return "alt+tab"
    if command == "d":
        return "win + d"
    if command == "w":
        return "win"
    return "a"

def pluginEvent():
    global plugin_para
    if plugin_para:
        for plugin in activated_plugins:
            plugin.action()

def isFeedback(plugin_name):
    status = plugin_name.statusSignalizer()
    if status:
        return True

def enableColoredOutput():
    init()  # colorama
def machine():
    # Подтягиваем параметры из установщика
    global plugin_para
    global bot
    print(Fore.LIGHTMAGENTA_EX + pyfiglet.figlet_format("ALT + TAB MACHINE"))
    print(Fore.GREEN + "|----------", VER, "----------|", sep="")
    default_port = checkForExistenceOfDeafultPort()
    port_num = input(Fore.BLUE + "Type the port number of plugged sensor (0 for default, -1 for creation of a new default): ")
    try:
        port_num =int(port_num)
    except TypeError:
        print(Fore.RED + "Invalid port number")
        return 1
    if (port_num == 0):
        port_num = default_port
    if (port_num == -1):
        port_num = createDefaultPort()
    s_port = serial.Serial()
    s_port.baudrate = 9600
    s_port.port = "COM" + str(port_num)
    print(Fore.BLUE + "---Configuring listener...")
    try:
        s_port.open()
    except OSError:
        print(Fore.RED + "It is impossible to open port!")
    if not(s_port.isOpen()):
        print(Fore.RED + "An unknown error occurred while port opening")
        return 1
    print(Fore.BLUE + "---Port listener successfully started!")
    if plugin_para:
        print(Fore.BLUE + "---Enabling plugins...")
        print(Fore.BLUE + "---Enabled!")
    preset_command = presetSelection()
    print(Fore.GREEN + "|--------------------------|")
    while (s_port.isOpen()):
        if s_port.readline():
            press_and_release(preset_command)
            print(Fore.LIGHTGREEN_EX + "---" + Fore.LIGHTYELLOW_EX + datetime.now().strftime("%H:%M:%S") + Fore.LIGHTGREEN_EX + "---Movement!")
            pluginEvent()


if __name__ == "__main__":

    enableColoredOutput()

    activated_plugins = []
    plugin_para = False

    print(Fore.WHITE + "---Configuring plugins...")

    from plugger import Plugin,Plugger
    pl = Plugger()
    installed_plugins = pl.plug()
    print(installed_plugins)


    i = 0
    for plugin in installed_plugins:
        try:
            activated_plugins.append(plugin)
            #activated_plugins[i] = SourceFileLoader(plugin.filename, plugin.path).load_module()
            activated_plugins[i] = SourceFileLoader("core_Telesend", "Plugins/Telesend").load_module()
            print(activated_plugins[i],"acivated!")
            i +=1
        except FileNotFoundError:
            print(plugin.folder_name, "failed to activate!")


    for plugin in activated_plugins:
        if isFeedback(plugin):
            print(plugin, "Started!")
            plugin_para = True

    machine()




