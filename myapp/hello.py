import argparse

def hello(name="World"):
    return f"Hello {name}!"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Say hello")
    parser.add_argument("--name", type=str, default="World", help="Name to greet")
    args = parser.parse_args()

    print(hello(args.name))
