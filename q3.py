try:
    h = eval(input('enter a no.'))
    print('user data',10/h)

except ValueError as e:
    print("Value invalid", e)
    except EOFError as e:
        print("End of file", e)
    except:
        print('ERROR')
