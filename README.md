# gRPC in the snake pit

Getting started with

- gRPC
- Python
- Test Driven Development
- Docs-as-code
- Visual Studio Code


```powershell
# Install package manager "scoop"
```

```powershell
# Install packages via scoop
```


```bash
aman@NB02022 MINGW64 /d/github/grpc-in-the-snake-pit (develop)
$ rm -rf .venv && rm -f Pipefile.lock && git restore .venv
$ pipenv install --dev
```


```bash
# Generate python code from message definitions in protobuf language
cd src
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. helloworld.proto
```

```bash
# Start server in a shell:
cd src
python -m grpc_in_the_snake_pit.server
```

```bash
# Run cöient in another shell:
cd src
python -m grpc_in_the_snake_pit.client
```
