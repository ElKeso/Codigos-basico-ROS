Datos de ROS:
   				I) Comandos Ros en terminal:
doble tabular para ver elememntos....

roscore: Inicia ROS

rostopic: muestra topicos...

rostopic list: listado de topicos

rqt_graph: esquema de nodos y topicos

rosrun: corre un paquete rosrun "paquete" "nodo"

rosccp:biblioteca c++ para hacer nodos

rospack find ....: entrega ruta del paquete ros

roscd ....: te envia a la localizacion del paquete

roscd log ....: envia a carpeta de registros del paquete

rosls ....: indica las carpetas disponibles dentro del paquete 

			I) crear y configurar workspace

mkdir (nombre carpeta)..:  es un comando para crear una carpeta para el workspace
para crear un workspace necesita otra carpeta en su interior llamada src, osea usar comando mkdir src dentro de la carpeta.

posteriormente se usa el comando catkin_make para crear el workspace en la carpeta creada

para poder utilizar el workspace se debe usar el comando:

source ~/(carpetacreada)/devel/setup.bash

despues copiar el comando en el gedit de ros con el comando

gedit ~/.bashrc


para crear nodos y programas se debe crear paquetes dentro de la carpeta src

			II) crear paquetes, nodos y programas

para crear un paquete se utiliza el comando 

catkin_create_pkg (nombre del paquete) (rospy y otras dependencias)...:

este creara un paquete donde en su interior puede albergar nodos, publicadoes topicos etc

para abrir localizacion del paquete en visual studio coder usar comando code . ...:

cuando se realizen nuevos nodos o nuevos paquetes volver a usar catkin_make para actualizar

como consejo crear en (carpeta)/src/(paquete) crear carpeta scripts para nodos con mkdir scripts

para crear archivos python y crear nuestros nodos se utiliza los comandos

touch (nombredelarchivo).py
chmod +x (nombre del archivo).py


finalizar nodos 
es necesario ir a archivo CMakelist.txt y en la linea 136 descomentar el add_executable((nombre del nodo) src/(ubicacionnodo))
y en linea 149 descomentar target_link_libraries((nombre del nodo)...
linea 150 descomentar y linea 151 descomentar 

comandos:

ROS_INFO("TEXT") muestra elementos en pantalla


 
