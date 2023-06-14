from .input import create_code_switch, read_input, read_lines_switches

template_switch = """! ====================================
!    Configuracion switch 
! ====================================

! Cambiar al modo privilegiado
enable

! ANTES DE ENTRAR A MODO CONFIGURACION DEL EQUIPO

! Parametros del reloj
clock set {date}

! ==========================
! == CONFIGURACION GLOBAL ==
! ==========================
! Para terminal
configure terminal

! Bautizar al equipo
hostname {hostname}

! Desactivar DNS
! Evita que un servidor busque un comando no reconocido (tarda)
no ip domain-lookup

! Establecer seguridad basica
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

! Aplicar VTP para activar el servidor de VLANs
vtp domain CoworQ
vtp mode {mode}
vtp password tc2006b

! Pasos para conseguir configuraciones exitosas de VLANs
! 1. Dar da alta las VLANs con nombre
vlan 100
  name VLAN Primaria

vlan 200
  name VLAN Secundaria

vlan 300
  name VLAN Preparatoria

vlan 400
  name VLAN Entrenadores

vlan 500
  name VLAN Prensa

vlan 600
  name VLAN Jueces

vlan 700
  name VLAN Servidor

vlan 911
  name Gestion

{steps}

{vlan}"""

def create_switch_code(index, hostname):
    output = create_code_switch(index, hostname, template_switch)
    with open(f'outputs/switch_{output.get("name", "")}.txt', 'w') as f:
        f.write(output.get("code", ""))


def create_switches_codes():
    read_lines_switches()
    lines = read_input("hostnames.txt")
    for i in range(len(lines)):
      line = lines[i]
      create_switch_code(i, line)