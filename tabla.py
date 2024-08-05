import csv
import matplotlib.pyplot as plt

# Specify the path to your CSV file
csv_file_path = 'reclamos falabella - Hoja 1.csv'

# Open the CSV file
with open(csv_file_path, 'r', encoding='utf-8') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    lista = []
    elementos = []
    cantidad = []
    for row in csv_reader:
        # Access the data in each row
        # For example, print the first column of each row
        
        lista.append(row[2])
    for i in lista:
        if i not in elementos:
            elementos.append(i)
            cantidad.append(1)
        else:
            cantidad[elementos.index(i)] += 1
    print(cantidad)
    import matplotlib.pyplot as plt

    # Plot the graph
    plt.bar(elementos, cantidad)
    plt.xlabel('Elementos', rotation='vertical')
    plt.ylabel('Cantidad', rotation='vertical')
    plt.title('Gráfico de elementos')
    plt.xticks(rotation=90)
    plt.show()




    