def main():
    # Obtenemos el directorio actual
    current_dir = os.getcwd()
    
    # Creamos una lista vacía para almacenar los nombres de archivos y carpetas
    file_and_dir_names = []
    
    # Recorremos todos los elementos en el directorio actual
    for item in os.listdir(current_dir):
        # Obtenemos el tipo de elemento
        item_type = os.path.isdir(os.path.join(current_dir, item))
        
        # Añadimos el nombre del elemento y su tipo al lista
        file_and_dir_names.append((item, item_type))
    
    # Ordenamos la lista según el tipo de elemento (carpeta primero, luego archivos)
    file_and_dir_names.sort(key=lambda x: x[1], reverse=True)
    
    # Mostramos los resultados
    print("Directorio actual:", current_dir)
    print("Elementos en el directorio:")
    for item, is_dir in file_and_dir_names:
        print(f"{'Carpeta'
                 if is_dir else 'Archivo'}: {item}")