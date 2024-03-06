"""
Emily Huang 12/6/22 CSCI-UA 2 - 004
Assignment #11 Part #3
"""

class Smartphone:

    def __init__(self, capacity, name):
        self.capacity = capacity
        self.name = name
        
        
    def add_app(self, appname, appsize):
        global space_avail


         #if not enough space
        if appsize > (self.capacity - space_avail):
            print("Cannot install app, no available space")

            
        else:

            #adding app name and size to lists
            apps.append(appname)
            app_with_size[appname] = appsize

            #capacity
            space_avail += appsize
       


    def remove_app(self, appname):
        global space_avail

    
        space_avail -= app_with_size[appname]
        apps.remove(appname)
        del app_with_size[appname]
        print("App removed:", appname)
            
            
        

    def has_app(self, appname):
        if appname in apps:
            return True
        else:
            return False
           

    def get_available_space(self):
        for app, size in app_with_size:
            space_avail += app_with_size[app]

        return space_avail

    def report(self):
        print("Name:", self.name)
        print("Capacity:", space_avail, "out of", self.capacity, "GB")
        print("Available space:", self.capacity - space_avail)
        if len(apps) > 0:
            
            print("Apps Installed:", len(apps))

            apps.sort()

            for app in apps:
                print("* ", app , " is using ", app_with_size[app], " GB", sep = '')

        else:
            print("Apps Installed: 0")
              
apps = []
app_with_size = {}
space_avail = 0 
size = int(input("Size of your new smartphone (32, 64 or 128 GB): "))

name = input("Smartphone name: ")
print("Smartphone created!")
phone_specs = Smartphone(size, name)
phone_specs.report()
print()

while True:
    menu = input("(r)eport, (a)dd app, r(e)move app or (q)uit: ").lower()

    
    if menu == "r":
        phone_specs.report()
       

    if menu == "a":
        appname = input("App name to add: ")
        appsize = int(input("App size in GB: "))

        if phone_specs.has_app(appname) == True:
            print("App already installed")


        else:
        
            phone_specs.add_app(appname, appsize)

        

    if menu == "e":
        appname = input("App name to remove: ")

        if phone_specs.has_app(appname) == False:
            print("App not installed")
        
        else:
            
            phone_specs.remove_app(appname)


    if menu == "q":
        print("Goodbye!")
        break
    print()
