import proto.simple_pb2 as simple_pb2


def simple():
    return simple_pb2.Simple(
        id=42,
        is_simple=True,
        name="My name",
        sample_lists=[1, 2, 3, 4],
    )


if __name__ == '__main__':
    print("Function Starts Here")
    print(simple())
    print("hello, how are you")
