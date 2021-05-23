import fire


def main(message: str) -> None:
    print(message)
    print(type(message))


if __name__ == "__main__":
    fire.Fire(main)
