import os
from PIL import Image
import sys
import threading
from queue import Queue
import time
from concurrent.futures import ThreadPoolExecutor
import threading

class EstadisticasCompartidas:
    def __init__(self):
        self.lock = threading.Lock()
        self.total_imagenes = 0
        self.total_bytes_originales = 0
        self.total_bytes_optimizados = 0
    
    def actualizar(self, bytes_original, bytes_optimizado):
        with self.lock:
            self.total_imagenes += 1
            self.total_bytes_originales += bytes_original
            self.total_bytes_optimizados += bytes_optimizado

def procesar_imagen(args):
    """
    Procesa una única imagen.
    """
    ruta_entrada, ruta_salida, calidad, max_size, estadisticas = args
    
    try:
        # Abrir imagen
        with Image.open(ruta_entrada) as img:
            # Convertir a RGB si es necesario
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # Redimensionar si es necesario
            if max(img.size) > max_size:
                ratio = max_size / max(img.size)
                new_size = tuple(int(dim * ratio) for dim in img.size)
                img = img.resize(new_size, Image.Resampling.LANCZOS)
            
            # Guardar imagen optimizada
            img.save(ruta_salida, 
                    'JPEG', 
                    quality=calidad, 
                    optimize=True)
            
            # Calcular estadísticas
            bytes_original = os.path.getsize(ruta_entrada)
            bytes_optimizado = os.path.getsize(ruta_salida)
            
            # Actualizar estadísticas compartidas
            estadisticas.actualizar(bytes_original, bytes_optimizado)
            
            # Mostrar progreso
            print(f"Hilo {threading.current_thread().name} - Optimizada: {os.path.basename(ruta_entrada)}")
            print(f"Tamaño original: {bytes_original/1024:.1f}KB")
            print(f"Tamaño optimizado: {bytes_optimizado/1024:.1f}KB")
            print(f"Reducción: {100-(bytes_optimizado/bytes_original*100):.1f}%")
            print("-" * 50)
            
    except Exception as e:
        print(f"Error procesando {ruta_entrada}: {str(e)}")

def optimizar_imagenes(carpeta_entrada, carpeta_salida, calidad=85, max_size=1920, max_workers=None):
    """
    Optimiza las imágenes de una carpeta usando múltiples hilos.
    
    Args:
        carpeta_entrada: Ruta de la carpeta con las imágenes originales
        carpeta_salida: Ruta donde se guardarán las imágenes optimizadas
        calidad: Calidad de compresión (0-100)
        max_size: Tamaño máximo del lado más largo de la imagen
        max_workers: Número máximo de hilos a utilizar (None = automático)
    """
    
    # Crear carpeta de salida si no existe
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)
    
    # Extensiones de imagen soportadas
    formatos_soportados = ['.jpg', '.jpeg', '.png', '.webp']
    
    # Crear objeto para estadísticas compartidas
    estadisticas = EstadisticasCompartidas()
    
    # Preparar lista de tareas
    tareas = []
    for filename in os.listdir(carpeta_entrada):
        extension = os.path.splitext(filename)[1].lower()
        if extension in formatos_soportados:
            ruta_entrada = os.path.join(carpeta_entrada, filename)
            ruta_salida = os.path.join(carpeta_salida, filename)
            tareas.append((ruta_entrada, ruta_salida, calidad, max_size, estadisticas))
    
    # Procesar imágenes con ThreadPoolExecutor
    tiempo_inicio = time.time()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(procesar_imagen, tareas)
    tiempo_fin = time.time()
    
    # Mostrar estadísticas finales
    if estadisticas.total_imagenes > 0:
        print("\nEstadísticas finales:")
        print(f"Total imágenes procesadas: {estadisticas.total_imagenes}")
        print(f"Tamaño total original: {estadisticas.total_bytes_originales/1024/1024:.1f}MB")
        print(f"Tamaño total optimizado: {estadisticas.total_bytes_optimizados/1024/1024:.1f}MB")
        print(f"Reducción total: {100-(estadisticas.total_bytes_optimizados/estadisticas.total_bytes_originales*100):.1f}%")
        print(f"Tiempo total de procesamiento: {tiempo_fin - tiempo_inicio:.2f} segundos")

def main():
    if len(sys.argv) < 3:
        print("Uso: python optimizar_imagenes.py carpeta_entrada carpeta_salida [calidad] [max_size] [max_workers]")
        sys.exit(1)
    
    carpeta_entrada = sys.argv[1]
    carpeta_salida = sys.argv[2]
    calidad = int(sys.argv[3]) if len(sys.argv) > 3 else 85
    max_size = int(sys.argv[4]) if len(sys.argv) > 4 else 1920
    max_workers = int(sys.argv[5]) if len(sys.argv) > 5 else None
    
    optimizar_imagenes(carpeta_entrada, carpeta_salida, calidad, max_size, max_workers)

if __name__ == "__main__":
    main()
