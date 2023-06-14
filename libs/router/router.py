from .input import args

template_router = """! ====================================
!    Configuracion Router Frontera
! ====================================

! Cambiar al modo privilegiado
enable

! ANTES DE ENTRAR A MODO CONFIGURACION DEL EQUIPO

! Parametros del reloj
clock set {date}

configure terminal

! Bautizar al equipo
hostname {hostname}

! Desactivar DNS
! Evita que un servidor busque un comando no reconocido (tarda)
no ip domain-lookup

! Establecer seguridad basica
enable secret tc2006b

{usernames}

! Dar de alta db
ip domain-name {domain-name}

! Algoritmo para encriptar (modulus 512 | 1024)
crypto key generate rsa

yes
1024

! Linea de la consola
line console 0
login local
logging sync

! 5 conexiones default en el router (0 4)
line vty 0 1
transport input ssh
login local
logging sync

! Banner
banner motd #
System administrator:
 _____ ___________  ___   _   _ 
|_   _|  ___| ___ \/ _ \ | \ | |
  | | | |__ | |_/ / /_\ \|  \| |
  | | |  __||    /|  _  || . ` |
  | | | |___| |\ \| | | || |\  |
  \_/ \____/\_| \_\_| |_/\_| \_/

Contact: a01704108@tec.mx

********************************* WARNING *********************************
*                                                                         *
*       If you are not authorized to use this system disconnect now       *
*                                                                         *
*   All attempts to access this system and/or its resources are recorded  *
*                                                                         *
***************************************************************************
#

! Configuracion de interfaces
{interfaces}

int g0/1
  no shutdown

! Configurar un DHCP para asignar IPs de manera automatica
{dhcp}

! Establecer una ruta por default para sacar el trafico al internet
! Es mejor que la secundaria este arriba
ip route 0.0.0.0  0.0.0.0  s0/1/0"""

def create_router_code():
    with open('outputs/router.txt', 'w') as f:
        f.write(template_router.format(**args))