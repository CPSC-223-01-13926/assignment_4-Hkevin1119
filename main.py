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

    myChoice = input("Enter menu choice: ")
    print()

    if myChoice == 1:
        myFile = input("Enter data filename: ")
        weather = read_data(myFile)
    elif myChoice == 2:
        weatherDate = input("Enter date (YYYYMMDD): ")
        weatherTime = input("Enter time (HHMMSS): ")
        weatherTemp = int(input("Enter temperature: "))
        weatherHumid = int(input("Enter humidity: "))
        weatherRain = float(input("Enter rainfall: "))
        weather[weatherDate+weatherTime] = {'t':weatherTime,'h':weatherHumid,'r':weatherRain}
    elif myChoice == 3:
        d = input("Enter Date: ")
        display = report_daily(weather, d)
        print(display)
    elif myChoice == 4:
        display = report_historical(weather)
        print(display)
    elif myChoice == 9:
        break
