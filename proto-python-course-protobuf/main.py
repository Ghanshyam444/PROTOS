from numbers import Complex

import google.protobuf.json_format as json_format

import proto.simple_pb2 as simple_pb2
import proto.complex_pb2 as complex_pb2
import proto.enumerations_pb2 as enumerations_pb2
import proto.oneofs_pb2 as oneofs_pb2
import proto.maps_pb2 as maps_pb2
import proto.prac_pb2 as prac_pb2

def complex():
    message = complex_pb2.Complex()
    message.one_dummy.id = 42
    message.one_dummy.name = "My Name"
    message.multiple_dummies.add(id=43, name="My Name 2")
    message.multiple_dummies.add(id=44, name="My Name 3")
    message.multiple_dummies.add(id=45, name="My Name 4")
    return message
def simple():
    return simple_pb2.Simple(
        id=44,
        is_simple=True,
        name="hello",
        sample_lists=[1, 2, 3, 4],
    )

def trysimple():
    mss = simple_pb2.Simple()
    mss.id = 49
    mss.is_simple = True
    mss.name = "HELLOOOO"
    mss.sample_lists.extend([5,7,10])
    return mss

def enums():
    return enumerations_pb2.Enumeration(
        #eye_color=enumerations_pb2.EYE_COLOR_GREEN
        eye_color = 1, # THis is the ordinal number type of assignment
    )

def oneofs():
    message = oneofs_pb2.Result(message="a message")
    print(message)
    message.id = 42
    print(message)

def maps():
    message =  maps_pb2.MapExample()
    message.ids["myid"].id = 42
    message.ids["myid2"].id = 43
    message.ids["myid3"].id = 44
    print(message)

def file(message):
    path = "simple.bin"

    print("Write To File")
    print(message)
    with open(path,"wb") as f:
        bytes_as_str = message.SerializeToString()
        f.write(bytes_as_str)

    print("Read From File")
    with open(path,"rb") as f:
        t = type(message)
        message2 = t().FromString(f.read())
    print(message2)

def to_json(message):
    return json_format.MessageToJson(message,indent = None,preserving_proto_field_name=True)

def from_json(json_str,type):
    return json_format.Parse(json_str,type,ignore_unknown_fields=True)

def prac():
    k =  prac_pb2.Prac(
        id = 1
    )
    path = "king.bin"
    with open(path,"wb") as f:
        bytes_as_str = k.SerializeToString()
        f.write(bytes_as_str)

if __name__ == "__main__":
    # print("Welcome to This Code")
    # print(simple())
    # print("Bye From this Code")
    # print("\nWelcome to Complex Code")
    # print(complex())
    # print("\nTrial Basis Running")
    # print(trysimple())
    # print("\nSee The Enumerations")
    # print(enums())
    # print("\nOrdinal Number is the tag given to the enumeration e.g 1 to red\n")
    # print(oneofs())
    # print("\n")
    # file(simple())
    # json_str = to_json(complex())
    # print(json_str)
    # print(from_json(json_str,complex_pb2.Complex()))
    # maps()
    # print(from_json('{"id":42, "unknown" : "test"}',simple_pb2.Simple()))
    print(prac())