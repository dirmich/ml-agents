# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mlagents/envs/communicator_objects/custom_action.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mlagents/envs/communicator_objects/custom_action.proto',
  package='communicator_objects',
  syntax='proto3',
  serialized_options=_b('\252\002\034MLAgents.CommunicatorObjects'),
  serialized_pb=_b('\n6mlagents/envs/communicator_objects/custom_action.proto\x12\x14\x63ommunicator_objects\"\x0e\n\x0c\x43ustomActionB\x1f\xaa\x02\x1cMLAgents.CommunicatorObjectsb\x06proto3')
)




_CUSTOMACTION = _descriptor.Descriptor(
  name='CustomAction',
  full_name='communicator_objects.CustomAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=94,
)

DESCRIPTOR.message_types_by_name['CustomAction'] = _CUSTOMACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CustomAction = _reflection.GeneratedProtocolMessageType('CustomAction', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMACTION,
  __module__ = 'mlagents.envs.communicator_objects.custom_action_pb2'
  # @@protoc_insertion_point(class_scope:communicator_objects.CustomAction)
  ))
_sym_db.RegisterMessage(CustomAction)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
