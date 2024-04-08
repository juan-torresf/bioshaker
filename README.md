# bioshaker
Código para cálculos de un bioshaker. PIA FÍSICA II.

Se irá actualizando mediante se tengan nuevas versiones.

Apartir de que en el código sale una advertencia de cualquier tipo, lo mejor es no usarlo y no tomar en cuenta los cálculos. 

Versión 1.0.2.

-Pide edad, sexo y actividad física, es para calcular el GER, después según tu actividad física se calcula el GET, la diferencia entre los dos nos da el gasto energético por la actividad física. Las listas de GER y GET están declaras al inicio del código, los rangos de edad y los cálculos están dentro de la función get_get(m).
-El sexo biológico ahora sirve para el saludo inicial.
-Si se está solicitando tiempo y excede el límite recomendable según tus datos, te dará una advertencia.
-Se mejoró la impresión en el menú y los demás modos. Además de agregar una tecla para salir desde el menú.
-Si las calorias que se quieren quemar exceden tu gasto energético por actividad física, te dará una advertencia.
-Reloj dinámico para la realización de ejercio.
-Nombre y versión del bioshaker como variable.
-Se mejoraron los cálculos gracias a investigaciones posteriores.

  Consideraciones futuros para la versión 1.0.3 (spoiler): datos globales, cuidado de masa, actulizar método de tiempo, temporizador dinámico, delay para el ejercicio, límite para el   uso del bioshaker.

Versión 1.0.1.

Mediante los datos iniciales del bioshaker  la fórmula de la posición, se saca la fórmula de la velocidad. La cual después se usa para el cálculo de la energía cinética, se hace la interal definida de 0 hasta T/4 que después se múltiplica por dos para tener únicamente la parte posítiva de la onda que nos interesa. Se relaciona para sacar por unidad de tiempo (segundos) y después se convierte en calorías.

Apartir de ahí, se establecen variós modos para que el usuario utilice el que se le acomode mejor.
