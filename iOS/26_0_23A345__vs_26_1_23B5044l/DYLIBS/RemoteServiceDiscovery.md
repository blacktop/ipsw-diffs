## RemoteServiceDiscovery

> `/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery`

```diff

-202.0.1.0.0
-  __TEXT.__text: 0xe188
-  __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_methlist: 0x36c
+202.40.9.0.0
+  __TEXT.__text: 0xf0a0
+  __TEXT.__auth_stubs: 0xab0
+  __TEXT.__objc_methlist: 0x4a0
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x12bc
+  __TEXT.__cstring: 0x136a
   __TEXT.__gcc_except_tab: 0x3bc
-  __TEXT.__oslogstring: 0x1c37
-  __TEXT.__unwind_info: 0x4c0
-  __TEXT.__objc_classname: 0x99
-  __TEXT.__objc_methname: 0x94d
-  __TEXT.__objc_methtype: 0x169
-  __TEXT.__objc_stubs: 0x760
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x5f8
-  __DATA_CONST.__objc_classlist: 0x30
+  __TEXT.__oslogstring: 0x1cc3
+  __TEXT.__unwind_info: 0x500
+  __TEXT.__objc_classname: 0xbe
+  __TEXT.__objc_methname: 0xa99
+  __TEXT.__objc_methtype: 0x1fb
+  __TEXT.__objc_stubs: 0x900
+  __DATA_CONST.__got: 0xf0
+  __DATA_CONST.__const: 0x698
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x218
-  __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x528
-  __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__objc_const: 0xb68
-  __AUTH.__objc_data: 0x28
-  __DATA.__objc_ivar: 0xbc
+  __DATA_CONST.__objc_selrefs: 0x288
+  __DATA_CONST.__objc_superrefs: 0x38
+  __AUTH_CONST.__auth_got: 0x568
+  __AUTH_CONST.__const: 0x2c0
+  __AUTH_CONST.__cfstring: 0x20
+  __AUTH_CONST.__objc_const: 0xd90
+  __AUTH.__objc_data: 0x78
+  __DATA.__objc_ivar: 0xcc
+  __DATA.__data: 0x60
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x1b8
   __DATA_DIRTY.__bss: 0x50

   - /usr/lib/libFDR.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 81E5CBB5-9FAE-3B68-8CA9-DF73F93A964B
-  Functions: 432
-  Symbols:   1349
-  CStrings:  494
+  UUID: 46490A40-29BE-3D6E-8673-187562D5BE06
+  Functions: 463
+  Symbols:   1444
+  CStrings:  536
 
Symbols:
+ +[RemoteDeviceQuery wildcard]
+ -[OS_remote_device(RemoteDeviceCommon) copyProperty:allowSensitive:]
+ -[OS_remote_device(RemoteDeviceCommon) device_alias]
+ -[OS_remote_device(RemoteDeviceCommon) device_name]
+ -[OS_remote_device(RemoteDeviceCommon) hasServiceWithName:peerMessage:]
+ -[OS_remote_device(RemoteDeviceCommon) hasServiceWithName:peerMessage:].cold.1
+ -[RemoteDeviceQuery availableService]
+ -[RemoteDeviceQuery dealloc]
+ -[RemoteDeviceQuery description]
+ -[RemoteDeviceQuery init]
+ -[RemoteDeviceQuery matches:forMessage:log:]
+ -[RemoteDeviceQuery name]
+ -[RemoteDeviceQuery setAvailableService:]
+ -[RemoteDeviceQuery setName:]
+ -[RemoteDeviceQuery setType:]
+ -[RemoteDeviceQuery setUuid:]
+ -[RemoteDeviceQuery type]
+ -[RemoteDeviceQuery uuid]
+ GCC_except_table102
+ GCC_except_table128
+ GCC_except_table133
+ GCC_except_table173
+ GCC_except_table210
+ GCC_except_table212
+ GCC_except_table375
+ GCC_except_table77
+ GCC_except_table79
+ GCC_except_table86
+ GCC_except_table88
+ GCC_except_table93
+ GCC_except_table98
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_RemoteDeviceQuery
+ _OBJC_IVAR_$_RemoteDeviceQuery._availableService
+ _OBJC_IVAR_$_RemoteDeviceQuery._name
+ _OBJC_IVAR_$_RemoteDeviceQuery._type
+ _OBJC_IVAR_$_RemoteDeviceQuery._uuid
+ _OBJC_METACLASS_$_RemoteDeviceQuery
+ __OBJC_$_CLASS_METHODS_RemoteDeviceQuery
+ __OBJC_$_INSTANCE_METHODS_OS_remote_device(RemoteDeviceCommon)
+ __OBJC_$_INSTANCE_METHODS_RemoteDeviceQuery
+ __OBJC_$_INSTANCE_VARIABLES_RemoteDeviceQuery
+ __OBJC_$_PROP_LIST_RemoteDeviceCommon
+ __OBJC_$_PROP_LIST_RemoteDeviceQuery
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RemoteDeviceCommon
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RemoteDeviceCommon
+ __OBJC_CLASS_PROTOCOLS_$_OS_remote_device(RemoteDeviceCommon)
+ __OBJC_CLASS_RO_$_RemoteDeviceQuery
+ __OBJC_LABEL_PROTOCOL_$_RemoteDeviceCommon
+ __OBJC_METACLASS_RO_$_RemoteDeviceQuery
+ __OBJC_PROTOCOL_$_RemoteDeviceCommon
+ ___CFConstantStringClassReference
+ ____remote_device_browse_matching_common_block_invoke
+ ____remote_device_browse_matching_common_block_invoke.388
+ ____remote_device_browse_matching_common_block_invoke.388.cold.1
+ ____remote_device_browse_matching_common_block_invoke.388.cold.2
+ ____remote_device_browse_matching_common_block_invoke.cold.1
+ ____remote_device_browse_matching_common_block_invoke.cold.2
+ ____remote_device_start_browsing_block_invoke.383
+ ____remote_device_start_browsing_block_invoke.383.cold.1
+ ____remote_service_accept_block_invoke.391
+ ____remote_service_connect_socket_impl_block_invoke.358
+ ____remote_service_connect_socket_impl_block_invoke.359
+ ____remote_service_connect_socket_impl_block_invoke.cold.7
+ ___block_descriptor_40_e8_32bs_e29_v20?0"OS_remote_device"8B16ls32l8
+ ___block_descriptor_40_e8_32bs_e47_q24?0"OS_remote_device"8"OS_remote_device"16ls32l8
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40bs48bs_e29_v20?0"OS_remote_device"8B16ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48bs_e29_v20?0"OS_remote_device"8B16ls48l8s32l8s40l8
+ ___block_literal_global.265
+ ___block_literal_global.294
+ ___block_literal_global.297
+ ___block_literal_global.300
+ ___block_literal_global.303
+ ___block_literal_global.306
+ ___block_literal_global.309
+ ___block_literal_global.313
+ ___block_literal_global.340
+ ___block_literal_global.343
+ ___block_literal_global.364
+ ___block_literal_global.367
+ ___block_literal_global.370
+ ___block_literal_global.385
+ ___block_literal_global.394
+ ___remote_device_browse_present_matching_block_invoke
+ ___remote_device_comparator_cast_block_invoke
+ ___remote_device_create_from_client_description_block_invoke.372
+ ___remote_service_listen_with_device_block_invoke.270
+ ___remote_socket_poll_connect_async_block_invoke.1
+ ___remote_socket_poll_connect_async_block_invoke.1.cold.1
+ __remote_device_browse_matching_common
+ __remote_device_browse_matching_common.cold.1
+ __xpc_dictionary_set_device_type_with_str
+ __xpc_dictionary_set_uuid_with_str
+ __xpc_dictionary_set_uuid_with_str.cold.1
+ _malloc_type_calloc
+ _objc_enumerationMutation
+ _objc_msgSend$availableService
+ _objc_msgSend$copyProperty:allowSensitive:
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$device_alias
+ _objc_msgSend$device_name
+ _objc_msgSend$hasServiceWithName:peerMessage:
+ _objc_msgSend$matches:forMessage:log:
+ _objc_msgSend$name
+ _objc_msgSend$setAvailableService:
+ _objc_msgSend$setName:
+ _objc_msgSend$sortUsingComparator:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$wildcard
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _remote_device_browse_present_matching
+ _remote_device_copy_device_matching
+ _remote_device_copy_device_matching.cold.1
+ _remote_device_copy_device_matching.cold.2
+ _remote_device_matches
+ _remote_socket_poll_connect_async.cold.2
+ _strcasestr
+ _strtoull
+ _uuid_compare
+ _uuid_parse
+ _uuid_unparse
- GCC_except_table103
- GCC_except_table120
- GCC_except_table129
- GCC_except_table165
- GCC_except_table202
- GCC_except_table204
- GCC_except_table367
- GCC_except_table76
- GCC_except_table78
- GCC_except_table80
- GCC_except_table82
- GCC_except_table87
- GCC_except_table92
- __OBJC_$_INSTANCE_METHODS_OS_remote_device
- __OBJC_$_PROP_LIST_OS_remote_device
- ____remote_device_start_browsing_block_invoke.369
- ____remote_device_start_browsing_block_invoke.369.cold.1
- ____remote_service_accept_block_invoke.374
- ____remote_service_connect_socket_impl_block_invoke.344
- ____remote_service_connect_socket_impl_block_invoke.345
- ___block_descriptor_56_e8_32s40s48bs_e29_v20?0"OS_remote_device"8B16ls48l8s32l8s40l8
- ___block_literal_global.250
- ___block_literal_global.275
- ___block_literal_global.280
- ___block_literal_global.283
- ___block_literal_global.286
- ___block_literal_global.292
- ___block_literal_global.295
- ___block_literal_global.299
- ___block_literal_global.326
- ___block_literal_global.329
- ___block_literal_global.350
- ___block_literal_global.353
- ___block_literal_global.356
- ___block_literal_global.371
- ___block_literal_global.377
- ___remote_device_create_from_client_description_block_invoke.358
- ___remote_device_start_browsing_matching_block_invoke.223
- ___remote_device_start_browsing_matching_block_invoke.223.cold.1
- ___remote_device_start_browsing_matching_block_invoke.223.cold.2
- ___remote_device_start_browsing_matching_block_invoke.223.cold.3
- ___remote_device_start_browsing_matching_block_invoke.cold.2
- ___remote_service_listen_with_device_block_invoke.256
- ___remote_socket_poll_connect_async_block_invoke.cold.1
- _remote_device_copy_device_with_name.cold.1
- _remote_device_copy_device_with_name.cold.2
- _remote_device_copy_device_with_uuid.cold.1
- _remote_device_copy_device_with_uuid.cold.2
- _remote_device_start_browsing_matching.cold.1
CStrings:
+ "%{public}s> : Device isn't connected"
+ "(name~='%s', type='%s', uuid='%s', '%s' in services)"
+ "@\"NSObject<OS_xpc_object>\"28@0:8*16B24"
+ "@28@0:8*16B24"
+ "B32@0:8r*16@\"NSObject<OS_xpc_object>\"24"
+ "B32@0:8r*16@24"
+ "B40@0:8@16@24@32"
+ "DeviceName"
+ "DeviceUUID"
+ "HWModel"
+ "Key '%{public}s' has invalid type"
+ "LocationID"
+ "RemoteDeviceCommon"
+ "RemoteDeviceQuery"
+ "SerialNumber"
+ "T*,R,N"
+ "TI,R,N"
+ "Tr*,N,V_availableService"
+ "Tr*,N,V_name"
+ "Tr*,N,V_uuid"
+ "Tr*,R,N"
+ "UniqueDeviceID"
+ "_availableService"
+ "_name"
+ "any"
+ "assertion failure: \"uuid_parse(value_str, uuid) == 0\" -> %llu"
+ "availableService"
+ "connect socket failed"
+ "copyProperty:allowSensitive:"
+ "countByEnumeratingWithState:objects:count:"
+ "description"
+ "hasServiceWithName:peerMessage:"
+ "matches:forMessage:log:"
+ "q24@?0@\"OS_remote_device\"8@\"OS_remote_device\"16"
+ "r*16@0:8"
+ "remote_device_copy_device_matching: device not found"
+ "remote_socket_poll_connect_async: EBADF"
+ "setAvailableService:"
+ "setName:"
+ "sortUsingComparator:"
+ "stringWithFormat:"
+ "v24@0:8r*16"
+ "wildcard"
- "remote_device_copy_device_with_name: device not found"
- "remote_device_copy_device_with_uuid: device not found"

```
