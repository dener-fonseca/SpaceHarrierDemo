# Arquivo que compila o projeto, ou seja, gera o executável do jogo usando o cx_Freeze

# Com este arquivo aberto, escrever no terminal do Pycharm python setup.py build

# O executável será gerado na pasta build e talvez seja necessário ajustar o caminho do asset

from cx_Freeze import setup, Executable


# Dependências adicionais e importantes do pygame como o asset
build_exe_options = {
    "packages": ["pygame"],
    "include_files": [("assets", "assets")],
}

setup(
    name="SpaceHarrier",
    version="1.0",
    description="Space Harrier Demo",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py")]
)