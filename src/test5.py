import fire


def main(*, message: str, suuji: int = 0) -> None:
    print(message)
    print(suuji)


if __name__ == "__main__":
    fire.Fire(main)
