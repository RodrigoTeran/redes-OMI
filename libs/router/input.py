def read_input(file_name):
    n_lines = []
    with open(f'libs/router/{file_name}') as f:
        lines = f.readlines()
        for line in lines:
            n_lines.append(line.replace("\n", ""))
    return n_lines

def generate(file_name, template):
    lines = read_input(file_name)
    code = ""

    for i in range(len(lines)):
        line = lines[i]
        splitted = line.split(" ")
        if i < len(lines) - 1:
            code += f"{template.format(*splitted)}\n\n"
            continue
        code += f"{template.format(*splitted)}"
    return code

def generate_interfaces():
    template = """int {}\n  description Descripcion\n  ip address {} {}\n  no shut"""
    return generate("interfaces.txt", template)

def generate_dhcp():
    template = """ip dhcp excluded-address {}\nip dhcp pool {}\n  network {} {}\n  default-router {}\n  dns-server {}"""
    return generate("dhcp.txt", template)

args = {
    "date": "21:00:00 Jun 13 2023",
    "hostname": "RF-Evento",
    "usernames": """username CEO privilege 15 secret tc2006b\nusername CIT privilege 15 secret tc2006b\nusername Admin privilege 15 secret tc2006b""",
    "domain-name": "omi.com",
    "interfaces": generate_interfaces(),
    "dhcp": generate_dhcp()
}