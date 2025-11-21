
country_code = "MEX"

match country_code:
    case "US"|"USA":
        print("United States")
    case "CA"|"CAN":
        print("Canada")
    case "MX"|"MEX":
        print("Mexico")
    case _:
        print("Unknown Country Code")

age = 15
match age:
    case age if age < 13:
        print("Child")
    case age if 13 <= age < 20:
        print("Teenager")
    case age if 20 <= age < 65:
        print("Adult")
    case _:
        print("Senior")