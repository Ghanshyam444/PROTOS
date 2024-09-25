from concurrent import futures
import grpc
from grpc_reflection.v1alpha import reflection


import item_pb2 as item_pb2
import item_pb2_grpc as item_pb2_grpc

items = []

def showItem():
    for item in items:
        print(item)

class ItemService (item_pb2_grpc.ItemServiceServicer):
    def CreateItem(self, request, context):
        items.append(request)
        return request
    def GetItem(self, request, context):
        for item in items:
            if item.id == request.id:
                return item
        return item_pb2.Item()
    # def UpdateItem(self, request, context):
    #     for i,item in enumerate(items):
    #         if item.id == request.id:
    #             items[i] = request
    #             return request
    #     return item_pb2.Item()

    def DeleteItem(self, request, context):
        global items
        items = [item for item in items if item.id != request.id]
        return request

    def ListItems(self,request,context):
        item_list = item_pb2.ItemList()
        item_list.items.extend(items)
        return item_list

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    item_pb2_grpc.add_ItemServiceServicer_to_server(ItemService(), server)
    server.add_insecure_port('[::]:50051')
    SERVICE_NAMES = (
        item_pb2.DESCRIPTOR.services_by_name['ItemService'].full_name, reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES,server)
    server.start()
    print("Server is running on port 50051...")
    server.wait_for_termination()

if __name__=="__main__":
    serve()
    showItem()
