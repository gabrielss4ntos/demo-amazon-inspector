import json
import sys
import argparse

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def print_vulnerability_count(vulnerability_count):
    print("Valores de vulnerability_count:")
    print(f"High: {vulnerability_count.get('high', 0)}")
    print(f"Critical: {vulnerability_count.get('critical', 0)}")
    print(f"Medium: {vulnerability_count.get('medium', 0)}")
    print(f"Low: {vulnerability_count.get('low', 0)}")

def validate_thresholds(vulnerability_count, high_limit, critical_limit, medium_limit, low_limit):
    high_count = vulnerability_count.get("high", 0)
    critical_count = vulnerability_count.get("critical", 0)
    medium_count = vulnerability_count.get("medium", 0)
    low_count = vulnerability_count.get("low", 0)

    print("Contagem de vulnerabilidades:")
    print(f"High: {high_count}")
    print(f"Critical: {critical_count}")
    print(f"Medium: {medium_count}")
    print(f"Low: {low_count}")

    if high_count >= high_limit:
        raise ValueError(f"High vulnerabilities exceed or equal the limit ({high_count} >= {high_limit})")
    if critical_count >= critical_limit:
        raise ValueError(f"Critical vulnerabilities exceed or equal the limit ({critical_count} >= {critical_limit})")
    if medium_count >= medium_limit:
        raise ValueError(f"Medium vulnerabilities exceed or equal the limit ({medium_count} >= {medium_limit})")
    if low_count >= low_limit:
        raise ValueError(f"Low vulnerabilities exceed or equal the limit ({low_count} >= {low_limit})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script de validação de vulnerabilidades')
    parser.add_argument('-H', '--high', type=int, required=True, help='Limite para vulnerabilidades High')
    parser.add_argument('-c', '--critical', type=int, required=True, help='Limite para vulnerabilidades Critical')
    parser.add_argument('-m', '--medium', type=int, required=True, help='Limite para vulnerabilidades Medium')
    parser.add_argument('-l', '--low', type=int, required=True, help='Limite para vulnerabilidades Low')
    parser.add_argument('json_file', type=str, help='Caminho para o arquivo JSON')

    args = parser.parse_args()

    try:
        # Lê o arquivo JSON
        sbom_data_list = read_json(args.json_file)

        # Assume que estamos interessados nos dados do primeiro item da lista
        if sbom_data_list:
            sbom_data = sbom_data_list[0]
            vulnerability_count = sbom_data.get("sbom", {}).get("vulnerability_count", {})

            # Imprime os valores de vulnerability_count
            print_vulnerability_count(vulnerability_count)

            # Valida os limites
            validate_thresholds(vulnerability_count, args.high, args.critical, args.medium, args.low)

            print("Pipeline pode continuar. Limites de vulnerabilidade não ultrapassados.")
        else:
            print("Erro: Lista vazia no arquivo JSON.")
            sys.exit(1)
    
    except ValueError as e:
        print(f"Erro: {e}")
        sys.exit(1)
