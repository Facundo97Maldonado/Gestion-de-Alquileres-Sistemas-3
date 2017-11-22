# hotel-project

**Integrantes**

- **Martin Liut**
- **Matias Reynoso**
- **Federico Palomero**

-----------
Pasos para correr la instacia de Python 3 que utiliza el proyecto (ubuntu):

1.Instalar virtualenv

2.(En la home)Crear un nuevo enviroment apuntando a la carpeta donde esta la version de python.

`virtualenv -p /usr/bin/python3 env`

3.Nos va a generar una carpeta que para utilizarla usamos:
 
`. env/bin/activate`

4.Con el env activado, ya podemos instalar las dependencias que queramos y hacer andar nuestro proyecto.

`pip install django`

5.Manteniendo el env activado nos paramos en la carpeta de nuestro proyecto y corremos `manage.py migrate`

6.Ya podemos hacer `manage.py runserver`
