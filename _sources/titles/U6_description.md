# U6. REDES NEURONALES ARTIFICIALES

## El Perceptrón y La arquitectura Perceptron Multicapa

**40 - Las Neuronas biológicas y el Modelo Perceptrón**: [Video 21mins]() <br/> Se introduce el perceptrón como un modelo bioinspirado que emula el comportamiento básico de una neurona biológica y el concepto tradicional de redes neuronales artificales.

**41 - Perceptrones Multicapa**: [Video 21mins]() <br/> Se analiza la arquitectura básica de las redes neuronales artificales, conocida como perceptrón multicapa y se discuten elementos clave como las funciones de activación y la descripción matemática del proceso de propagación hacia adelante en una red neuronal artificial.

## Algoritmo de propagación hacia atrás

**42 - Backpropagation**: [Video 21mins]() <br/> Se explica el proceso de entrenamiento de las redes neuronales artificiales, el concepto de propagación hacia atrás del error y los pasos que es necesario llevar a cabo para completar un época del algoritmo de entrenamiento. Se discute también el problema conocido como desvanecimiento del gradiente y cómo se enfrenta.

**43 - Esquemas de entrenamiento**: [Video 21mins]() <br/> Se discuten los requerimientos en términos de memoria y cómputo que tiene el algoritmo Backpropagation y se introducen los esquemas de entrenamiento Batch, mini-batch y online, que ayudan a mitigar algunos de las limitaciones encontradas durante el entrenamiento, así como algunos ejemplos prácticos.

## Otras arquitecturas de red

**44 - Mapas auto-organizables**: [Video 28mins](https://youtu.be/3DO9FJhPt3k) <br/> Se presentan los principios de funcionamiento y el algoritmo de entrenamiento de una red neuronal conocida como Mapa auto-organizable, que puede ser usada para resolver problemas no supervisados de agrupamiento.

**45 - Ejemplos prácticos con Mapas auto-organizables**: [Video 9mins](https://youtu.be/VzIstWRtqPw) <br/> Se presenta el ejemplo típico de aplicación de los SOM usando un conjunto de muestras de 3 dimensiones, que pueden ser interpretadas como componentes de color. Adicionalmente, se muestra el desempeño del modelo cuando se aplica a un problema de agrupamiento de datos que conforman variedades y se compara con el resultado de un k-means. Se introduce el concepto de matriz U y la identificación del número de grupos detectados por el modelo.

**46 - Introducción a la analítica de secuencias**: [Video 23mins](https://youtu.be/JzOumjQ-7qA) <br/> Se introduce el concepto de secuencia, una modalidad de información en la que la suposición de independencia entre observaciones ya no se puede asumir en todos los casos. Se discute la arquitectura básica de red neuronal diseñada para trabajar con secuencias y diferentes configuraciones que pueden construirse con este tipo de redes para resolver diferentes tareas de ML.

**47 - Redes Neuronales Recurrentes**: [Video 36mins](https://youtu.be/rrrjZSVnr0M) <br/> Se revisa el proceso de propagación hacia adelante de las redes neuronales recurrentes y su algoritmo de entrenamiento; se discuten las limitaciones del modelo y se presenta un ejemplo implementado con dos librerías diferentes.

**48 - Redes Neuronales Recurrentes Bidireccionales**: [Video 5mins](https://youtu.be/CwZ2wyZzMJs) <br/> Revisamos una arquitectura alternativa de red neuronal recurrente que procesa las secuencias de entrada en los dos sentidos de manera simultánea.

**49 - Introducción a las redes LSTM y GRU**: [Video 17mins](https://youtu.be/GgPuTt_vHgU) <br/> Se introducen dos arquitecturas de redes neuronales recurrentes que incluyen unidades básicas diferentes al perceptrón estándar y tienen la capacidad de almacenar memoria de largo y corto alcance.