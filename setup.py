from cx_Freeze import setup, Executable

# Dependências adicionais do pygame
build_exe_options = {
    "packages": ["pygame"],
    "include_files": ["asset/"],
}

setup(
    name="SpaceHarrier",
    version="1.0",
    description="Space Harrier em Pygame",
    options={"build_exe": build_exe_options},
    executables=[Executable("code/Game.py")]
)