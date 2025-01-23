# Image Compressor / Compresor de Imágenes

[English](#english) | [Español](#español)

---

## English

### Description
A multi-threaded image compression tool that optimizes images in bulk while maintaining quality. The script processes multiple images simultaneously using Python threads, making it efficient for large batches of images.

### Features
- Multi-threaded image processing
- Supports JPG, JPEG, PNG, and WebP formats
- Automatic image resizing
- Quality adjustment
- Progress tracking and statistics
- Configurable compression parameters

### Requirements
- Python 3.x
- Pillow library

### Installation
1. Clone this repository:
```bash
git clone https://github.com/yourusername/image_compressor.git
cd image_compressor
```

2. Install required dependencies:
```bash
pip install Pillow
```

### Usage
1. Basic usage (will use default values):
```bash
python main.py
```

2. Advanced usage with parameters:
```bash
python main.py input_folder output_folder quality max_size threads
```

Parameters:
- `input_folder`: Source folder containing images (default: "input")
- `output_folder`: Destination folder for compressed images (default: "output")
- `quality`: Compression quality (0-100, default: 85)
- `max_size`: Maximum image dimension in pixels (default: 1920)
- `threads`: Number of processing threads (default: auto)

### Example
```bash
python main.py input output 85 1920 4
```

### Project Structure
```
image_compressor/
├── main.py
├── input/
│   └── (your images here)
└── output/
    └── (compressed images will be saved here)
```

---

## Español

### Descripción
Una herramienta de compresión de imágenes multi-hilo que optimiza imágenes en lote manteniendo la calidad. El script procesa múltiples imágenes simultáneamente usando hilos de Python, haciéndolo eficiente para grandes cantidades de imágenes.

### Características
- Procesamiento de imágenes multi-hilo
- Soporta formatos JPG, JPEG, PNG y WebP
- Redimensionamiento automático de imágenes
- Ajuste de calidad
- Seguimiento de progreso y estadísticas
- Parámetros de compresión configurables

### Requisitos
- Python 3.x
- Biblioteca Pillow

### Instalación
1. Clona este repositorio:
```bash
git clone https://github.com/tuusuario/image_compressor.git
cd image_compressor
```

2. Instala las dependencias requeridas:
```bash
pip install Pillow
```

### Uso
1. Uso básico (utilizará valores predeterminados):
```bash
python main.py
```

2. Uso avanzado con parámetros:
```bash
python main.py carpeta_entrada carpeta_salida calidad tamaño_maximo hilos
```

Parámetros:
- `carpeta_entrada`: Carpeta origen con las imágenes (predeterminado: "input")
- `carpeta_salida`: Carpeta destino para imágenes comprimidas (predeterminado: "output")
- `calidad`: Calidad de compresión (0-100, predeterminado: 85)
- `tamaño_maximo`: Dimensión máxima de imagen en píxeles (predeterminado: 1920)
- `hilos`: Número de hilos de procesamiento (predeterminado: automático)

### Ejemplo
```bash
python main.py input output 85 1920 4
```

### Estructura del Proyecto
```
image_compressor/
├── main.py
├── input/
│   └── (coloca tus imágenes aquí)
└── output/
    └── (las imágenes comprimidas se guardarán aquí)
```

---

## License / Licencia
MIT License

## Contributing / Contribuir
Feel free to submit pull requests or create issues for bugs and feature requests.

Siéntete libre de enviar pull requests o crear issues para reportar errores y solicitar nuevas características.
