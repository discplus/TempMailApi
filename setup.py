from pip._internal.cli.main import main


common_packages = [
    "requests==2.28.1",
    "json",
    "colorama>=0.4.6",
    "random",
    "string",
    "time",
    "os"
]


def install_packages(packages_list: list[str]):
    for pkg in packages_list:
        main(["install", "-U", pkg])


if __name__ == '__main__':
    install_packages(common_packages)