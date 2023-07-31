Las instrucciones del repositorio original son las siguientes:

Hola y bienvenidos al equipo Gilded Rose. Como sabéis, somos una pequeña posada con una excelente ubicación en una ciudad prominente gestionada por una amable posadera llamada Allison. También compramos y vendemos productos de alta calidad. Desafortunadamente, la calidad de nuestros productos se ha ido degradando a medida que se acercan a su fecha de caducidad. Tenemos un sistema que actualiza nuestro inventario por nosotros. Fue desarrollado por un tipo sensato llamado Leeroy, que ha seguido adelante con nuevas aventuras. Tu tarea consiste en añadir la nueva función a nuestro sistema para que podamos empezar a vender una nueva categoría de artículos. Primero una introducción a nuestro sistema:

Todos los artículos tienen un valor SellIn que indica el número de días que tenemos para vender el artículo.
Todos los objetos tienen un valor de calidad que indica el valor del artículo.
Al final de cada día nuestro sistema reduce ambos valores de cada artículo.
Bastante sencillo, ¿no? Pues aquí es donde la cosa se pone interesante:

Una vez pasada la fecha de caducidad, la calidad se degrada el doble de rápido.
La calidad de un artículo nunca es negativa.
El "brie añejado" aumenta su calidad a medida que envejece.
La calidad de un artículo nunca es superior a 50.
"Sulfuras", al ser un objeto legendario, nunca tiene que venderse y su calidad nunca disminuye.
Los "Backstage passes", como el brie curado, aumentan su calidad a medida que se acerca su valor SellIn. La calidad aumenta en 2 cuando quedan 10 días o menos y en 3 cuando quedan 5 días o menos, pero la calidad baja a 0 después del concierto.
Recientemente hemos fichado a un proveedor de artículos conjurados. Esto requiere una actualización de nuestro sistema:

La calidad de los objetos "conjurados" se degrada el doble de rápido que la de los objetos normales.
Siéntete libre de hacer cualquier cambio en el método UpdateQuality y de añadir cualquier código nuevo, siempre y cuando todo siga funcionando correctamente. Sin embargo, no modifiques la clase Item ni la propiedad Items, ya que pertenecen al duende de la esquina que se enfurecerá y te disparará un tiro, ya que no cree en la propiedad compartida del código (puedes hacer que el método UpdateQuality y la propiedad Items sean estáticos si quieres, nosotros te respaldaremos).

Sólo como aclaración, un objeto nunca puede tener su calidad por encima de 50, sin embargo "Sulfuras" es un objeto legendario y como tal su calidad es 80 y nunca debe cambiar.