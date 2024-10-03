def total_calculation():
    total_weight = 0
    num_components = int(input("Enter number of components: "))

    for i in range(1, num_components + 1):
        num_components = input(f'Input component {i} name: ')
        component_weight = int(input(f'Input component {i} weight (as %): '))

        total_weight += component_weight

    print(f'Total: {total_weight}')

total_calculation()
