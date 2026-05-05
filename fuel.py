# Fuel Gauge: Practice using functions to determine how much fuel is in a tank, based on a fraction provided by the user.
def main():
    while True:
        try:
            i = input("Fraction: ")
            n , d = (i.split("/"))
            n = int(n)
            d = int(d)
            #print (n,d)
            value = float(n/d)*100
            #print(value)
            if 0 <= value <= 1 :
                print("E")
                return
            elif 100 >= value >= 99 :
                print("F")
                return
            elif 1 < value < 99:
                number = int(round(value,0))
                print(number,"%",sep = "")
                return
            else:
                pass
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()
