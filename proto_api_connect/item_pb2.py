# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: item.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'item.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nitem.proto\x1a\x1bgoogle/protobuf/empty.proto\" \n\x04Item\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\" \n\x08ItemList\x12\x14\n\x05items\x18\x01 \x03(\x0b\x32\x05.Item2\xaa\x01\n\x0bItemService\x12\x1a\n\nCreateItem\x12\x05.Item\x1a\x05.Item\x12\x17\n\x07GetItem\x12\x05.Item\x1a\x05.Item\x12\x1a\n\nUpdateItem\x12\x05.Item\x1a\x05.Item\x12\x1a\n\nDeleteItem\x12\x05.Item\x1a\x05.Item\x12.\n\tListItems\x12\x16.google.protobuf.Empty\x1a\t.ItemListb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'item_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ITEM']._serialized_start=43
  _globals['_ITEM']._serialized_end=75
  _globals['_ITEMLIST']._serialized_start=77
  _globals['_ITEMLIST']._serialized_end=109
  _globals['_ITEMSERVICE']._serialized_start=112
  _globals['_ITEMSERVICE']._serialized_end=282
# @@protoc_insertion_point(module_scope)