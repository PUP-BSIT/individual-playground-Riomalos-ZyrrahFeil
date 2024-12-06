choice = 0
while choice != 3:
    print("\nNumpy's")
    print("1. Array Dimensions")
    print("2. Operations")
    print("3. exit")
    choice = input('Enter your choice: ')

    match choice:

        case '1':
            from numpypackage import numpy1

            numpy1.numpy_dimensions()

        case '2':
            from numpypackage import operations

            operations.numpy_operations()

        case '3':
            exit()
