while True:
    try:
        x = int(input("Hey, enter a no."))
        break
    except (AttributeError):
        print("Its, not a valid attribute.")
    except (TypeError):
        print("Its, not a valid type.")
    except (ValueError):
        print("Its, not a valid value.")
