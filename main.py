from weather import *
myFile = "weather.dat"

myChoice = 0
while(True):
    print("      *** TUFFY TITAN WEATHER LOGGER MAIN MENU")
    print()
    print("1. Set data FileName")
    print("2. Add Weather Data")
    print("3. Print Daily Report")
    print("4. Print Historical Report")
    print("9. Exit the program")
    print()

    myChoice = int(input("Enter menu choice: "))
    print()

    if myChoice == 1:
        myFile = input("Enter data filename: ")
        weather = read_data(myFile)
    elif myChoice == 2:
        dt = input('Enter date:\n>>>')
        tm = input('Enter time:\n>>>')
        t =int (input('Enter temperature:\n>>>'))
        h = int(input('Enter humidity:\n>>>'))
        r = float(input('Enter rainfall:\n>>>'))
        weather[dt+tm] = {'t':t, 'h':h, 'r':r}
        write_data(weather,myFile)
    elif myChoice == 3:
        d = input("Enter Date: ")
        display = report_daily(weather, d)
        print(display)
    elif myChoice == 4:
        display = report_historical(weather)
        print(display)
    elif myChoice == 9:
        break
