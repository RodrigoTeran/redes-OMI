lines_switches = []

def read_input(file_name):
    n_lines = []
    with open(f'libs/switch/{file_name}') as f:
        lines = f.readlines()
        for line in lines:
            n_lines.append(line.replace("\n", ""))
    return n_lines

def read_lines_switches():
    global lines_switches
    lines = read_input("switches.txt")
    lines_switches = lines

def generate(file_name, template, index = 0):
    line = lines_switches[index]
    splitted = line.split(" ")
    return f"{template.format(*splitted)}"

def generate_vlan_and_gateway(index):
    template = """interface vlan 911\n  description VLAN de gestion\n  ip address {} {}\n  no shut\n\nip default-gateway {}"""
    return generate("switches.txt", template, index)

def generate_step(index):
    lines = read_input(f"switches/{index + 1}.txt")
    code = ""

    for i in range(len(lines)):
        line = lines[i]
        if i < len(lines) - 1:
            code += f"{line}\n"
            continue
        code += line
    return code

def create_args():
    return {
        "date": "21:00:00 Jun 13 2023",
        "hostname": "",
        "usernames": """username CEO privilege 15 secret tc2006b\nusername CIT privilege 15 secret tc2006b\nusername Admin privilege 15 secret tc2006b""",
        "domain-name": "omi.com",
        "interfaces": generate_interfaces(),
        "dhcp": generate_dhcp()
    }
    template_router.format(**create_args())

def create_code_switch(index, hostname, template_switch):

    args = {
        "date": "21:00:00 Jun 13 2023",
        "hostname": hostname,
        "usernames": """username CEO privilege 15 secret tc2006b\nusername CIT privilege 15 secret tc2006b\nusername Admin privilege 15 secret tc2006b""",
        "domain-name": "omi.com",
        "vlan": generate_vlan_and_gateway(index),
        "steps": generate_step(index)
    }

    return {
        "name": f"{hostname}.txt",
        "code": template_switch.format(**args)
    }