## CloudTelemetry

> `/System/Library/PrivateFrameworks/CloudTelemetry.framework/CloudTelemetry`

```diff

-2320.10.0.0.0
-  __TEXT.__text: 0x17a28
-  __TEXT.__auth_stubs: 0xf20
+2350.100.1.0.0
+  __TEXT.__text: 0xf960
+  __TEXT.__auth_stubs: 0xbd0
   __TEXT.__objc_methlist: 0x18c
-  __TEXT.__const: 0x1448
-  __TEXT.__cstring: 0x5f0
-  __TEXT.__constg_swiftt: 0x5f4
-  __TEXT.__swift5_typeref: 0x617
-  __TEXT.__swift5_reflstr: 0x594
-  __TEXT.__swift5_fieldmd: 0x5c8
-  __TEXT.__swift5_proto: 0xc8
-  __TEXT.__swift5_types: 0x7c
-  __TEXT.__swift_as_entry: 0x84
-  __TEXT.__swift_as_ret: 0x9c
-  __TEXT.__swift5_assocty: 0x148
-  __TEXT.__swift5_capture: 0x174
-  __TEXT.__oslogstring: 0x480
+  __TEXT.__const: 0xd50
+  __TEXT.__constg_swiftt: 0x2f8
+  __TEXT.__swift5_typeref: 0x412
+  __TEXT.__swift5_reflstr: 0x434
+  __TEXT.__swift5_fieldmd: 0x348
+  __TEXT.__swift5_proto: 0x94
+  __TEXT.__swift5_types: 0x48
+  __TEXT.__swift_as_entry: 0x6c
+  __TEXT.__swift_as_ret: 0x88
+  __TEXT.__cstring: 0x1f4
+  __TEXT.__swift5_assocty: 0x110
+  __TEXT.__swift5_capture: 0xd8
+  __TEXT.__oslogstring: 0x38e
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x810
-  __TEXT.__eh_frame: 0xe48
-  __TEXT.__objc_classname: 0x17
-  __TEXT.__objc_methname: 0x2c7
-  __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0x2c0
-  __DATA_CONST.__const: 0x70
-  __DATA_CONST.__objc_classlist: 0x48
+  __TEXT.__unwind_info: 0x560
+  __TEXT.__eh_frame: 0xc10
+  __TEXT.__objc_classname: 0xfe
+  __TEXT.__objc_methname: 0x481
+  __TEXT.__objc_methtype: 0x110
+  __TEXT.__objc_stubs: 0x100
+  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__const: 0x38
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x108
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x790
-  __AUTH_CONST.__const: 0xba8
-  __AUTH_CONST.__objc_const: 0x880
+  __AUTH_CONST.__auth_got: 0x5f0
+  __AUTH_CONST.__const: 0x700
+  __AUTH_CONST.__objc_const: 0x5b8
   __AUTH.__objc_data: 0x90
-  __DATA.__data: 0x2b0
-  __DATA.__bss: 0x1180
+  __DATA.__data: 0x1d8
+  __DATA.__bss: 0xd80
   __DATA_DIRTY.__objc_data: 0xf8
-  __DATA_DIRTY.__data: 0x7a0
-  __DATA_DIRTY.__bss: 0x650
-  __DATA_DIRTY.__common: 0x40
+  __DATA_DIRTY.__data: 0x4d8
+  __DATA_DIRTY.__bss: 0x4e0
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/CloudTelemetryShared.dylib
   - /System/Library/PrivateFrameworks/CloudTelemetryTools.framework/CloudTelemetryTools
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D9E1D046-CC8D-3F79-BCC2-DBF576B45731
-  Functions: 657
-  Symbols:   507
-  CStrings:  137
+  UUID: 87BE5FBE-3D8B-34AE-A102-07539976818A
+  Functions: 379
+  Symbols:   306
+  CStrings:  107
 
Symbols:
+ _objc_msgSend$attributesOfItemAtPath:error:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$description
+ _objc_msgSend$init
+ _objc_msgSend$mainBundle
+ _objc_msgSend$respondsToSelector:
+ _objc_release_x26
+ _symbolic _____Sg 14CloudTelemetry10EventValueO
- _XPC_ACTIVITY_ALLOW_BATTERY
- _XPC_ACTIVITY_CHECK_IN
- _XPC_ACTIVITY_DELAY
- _XPC_ACTIVITY_DISK_INTENSIVE
- _XPC_ACTIVITY_EXPECTED_DURATION
- _XPC_ACTIVITY_GRACE_PERIOD
- _XPC_ACTIVITY_GROUP_CONCURRENCY_LIMIT
- _XPC_ACTIVITY_GROUP_NAME
- _XPC_ACTIVITY_INTERVAL_1_MIN
- _XPC_ACTIVITY_INTERVAL_5_MIN
- _XPC_ACTIVITY_NETWORK_UPLOAD_SIZE
- _XPC_ACTIVITY_POST_INSTALL
- _XPC_ACTIVITY_POWER_NAP
- _XPC_ACTIVITY_PRIORITY
- _XPC_ACTIVITY_PRIORITY_MAINTENANCE
- _XPC_ACTIVITY_RANDOM_INITIAL_DELAY
- _XPC_ACTIVITY_REPEATING
- _XPC_ACTIVITY_REQUIRE_INEXPENSIVE_NETWORK_CONNECTIVITY
- _XPC_ACTIVITY_REQUIRE_NETWORK_CONNECTIVITY
- __Block_copy
- __Block_release
- __DATA__TtC20CloudTelemetryShared11XPCActivity
- __DATA__TtC20CloudTelemetryShared13XPCConnection
- __DATA__TtC20CloudTelemetryShared17XPCActivityHandle
- __IVARS__TtC20CloudTelemetryShared11XPCActivity
- __IVARS__TtC20CloudTelemetryShared13XPCConnection
- __IVARS__TtC20CloudTelemetryShared17XPCActivityHandle
- __METACLASS_DATA__TtC20CloudTelemetryShared11XPCActivity
- __METACLASS_DATA__TtC20CloudTelemetryShared13XPCConnection
- __METACLASS_DATA__TtC20CloudTelemetryShared17XPCActivityHandle
- __NSConcreteStackBlock
- ___swift_destroy_boxed_opaque_existential_0
- ___swift_memcpy9_8
- __swift_FORCE_LOAD_$_swiftCoreFoundation_$_CloudTelemetryShared
- __swift_FORCE_LOAD_$_swiftDispatch_$_CloudTelemetryShared
- __swift_FORCE_LOAD_$_swiftFoundation_$_CloudTelemetryShared
- __swift_FORCE_LOAD_$_swiftObjectiveC_$_CloudTelemetryShared
- __swift_FORCE_LOAD_$_swiftXPC_$_CloudTelemetryShared
- __swift_FORCE_LOAD_$_swift_Builtin_float_$_CloudTelemetryShared
- __swift_FORCE_LOAD_$_swiftos_$_CloudTelemetryShared
- __xpc_type_activity
- __xpc_type_array
- __xpc_type_bool
- __xpc_type_connection
- __xpc_type_data
- __xpc_type_date
- __xpc_type_dictionary
- __xpc_type_double
- __xpc_type_endpoint
- __xpc_type_error
- __xpc_type_int64
- __xpc_type_null
- __xpc_type_shmem
- __xpc_type_string
- __xpc_type_uint64
- __xpc_type_uuid
- _associated conformance 20CloudTelemetryShared10XPCMessageV11MessageTypeOSHAASQ
- _associated conformance 20CloudTelemetryShared8XPCErrorV10Foundation14LocalizedErrorAAs0G0
- _block_copy_helper
- _block_copy_helper.12
- _block_copy_helper.15
- _block_copy_helper.18
- _block_copy_helper.6
- _block_copy_helper.9
- _block_descriptor
- _block_descriptor.11
- _block_descriptor.14
- _block_descriptor.17
- _block_descriptor.20
- _block_descriptor.8
- _block_destroy_helper
- _block_destroy_helper.10
- _block_destroy_helper.13
- _block_destroy_helper.16
- _block_destroy_helper.19
- _block_destroy_helper.7
- _flat unique So13OS_xpc_object_p
- _free
- _malloc
- _objc_release
- _objc_retain_x21
- _objc_retain_x26
- _swift_arrayDestroy
- _swift_coroFrameAlloc
- _swift_deletedMethodError
- _swift_endAccess
- _swift_getExistentialTypeMetadata
- _swift_isEscapingClosureAtFileLocation
- _swift_release_n
- _swift_retain_n
- _swift_unknownObjectRelease_n
- _swift_unknownObjectWeakAssign
- _swift_unknownObjectWeakDestroy
- _swift_unknownObjectWeakInit
- _swift_unknownObjectWeakLoadStrong
- _symbolic $s20CloudTelemetryShared17XPCActivityConfigP
- _symbolic $s20CloudTelemetryShared18XPCActivityHandlerP
- _symbolic $s20CloudTelemetryShared21XPCConnectionDelegateP
- _symbolic SPy_____G3key______5valuet s4Int8V 20CloudTelemetryShared9XPCObjectO
- _symbolic SPy_____G3key______5valuetSg s4Int8V 20CloudTelemetryShared9XPCObjectO
- _symbolic SPy_____G______pSbIgygd_ s4Int8V So13OS_xpc_objectP
- _symbolic SPy_____G______t s4Int8V 20CloudTelemetryShared9XPCObjectO
- _symbolic SaySSG
- _symbolic ScCy___________pG 20CloudTelemetryShared13XPCDictionaryV s5ErrorP
- _symbolic ScTyyt______pGSg s5ErrorP
- _symbolic _____ 10Foundation4DataV
- _symbolic _____ 20CloudTelemetryShared10XPCMessageV
- _symbolic _____ 20CloudTelemetryShared10XPCMessageV11MessageTypeO
- _symbolic _____ 20CloudTelemetryShared11MessageKeysO
- _symbolic _____ 20CloudTelemetryShared11XPCActivityC
- _symbolic _____ 20CloudTelemetryShared13XPCConnectionC
- _symbolic _____ 20CloudTelemetryShared17XPCActivityHandleC
- _symbolic _____ 20CloudTelemetryShared21XPCIncomingConnectionV
- _symbolic _____ 20CloudTelemetryShared25PostInstallActivityConfigV
- _symbolic _____ 20CloudTelemetryShared26CacheCleanupActivityConfigV
- _symbolic _____ 20CloudTelemetryShared26SubmitEventsActivityConfigV
- _symbolic _____ 20CloudTelemetryShared8XPCErrorV
- _symbolic _____ 20CloudTelemetryShared9XPCObjectO
- _symbolic _____Sg s13OpaquePointerV
- _symbolic _____XDXMT 20CloudTelemetryShared11XPCActivityC
- _symbolic ______p So13OS_xpc_objectP
- _symbolic ______pSg So13OS_xpc_objectP
- _symbolic ______pSgXw 20CloudTelemetryShared21XPCConnectionDelegateP
- _symbolic ______pXp 20CloudTelemetryShared18XPCActivityHandlerP
- _symbolic _____ySPy_____G_____G s18_DictionaryStorageC s4Int8V 20CloudTelemetryShared9XPCObjectO
- _symbolic _____ySPy_____G______tG s23_ContiguousArrayStorageC s4Int8V 20CloudTelemetryShared9XPCObjectO
- _symbolic _____ySS_____G s18_DictionaryStorageC 20CloudTelemetryShared9XPCObjectO
- _symbolic x
- _type_layout_string 20CloudTelemetryShared10XPCMessageV
- _type_layout_string 20CloudTelemetryShared13XPCDictionaryV
- _type_layout_string 20CloudTelemetryShared8XPCErrorV
- _xpc_activity_add_eligibility_changed_handler
- _xpc_activity_copy_criteria
- _xpc_activity_get_state
- _xpc_activity_register
- _xpc_activity_remove_eligibility_changed_handler
- _xpc_activity_set_criteria
- _xpc_activity_set_state
- _xpc_activity_should_defer
- _xpc_bool_create
- _xpc_bool_get_value
- _xpc_connection_activate
- _xpc_connection_cancel
- _xpc_connection_copy_entitlement_value
- _xpc_connection_create
- _xpc_connection_create_from_endpoint
- _xpc_connection_create_mach_service
- _xpc_connection_get_audit_token
- _xpc_connection_get_euid
- _xpc_connection_send_message
- _xpc_connection_send_message_with_reply
- _xpc_connection_set_event_handler
- _xpc_connection_set_target_queue
- _xpc_data_create
- _xpc_data_get_bytes_ptr
- _xpc_data_get_length
- _xpc_date_create
- _xpc_date_get_value
- _xpc_dictionary_apply
- _xpc_dictionary_create_empty
- _xpc_dictionary_get_count
- _xpc_dictionary_get_string
- _xpc_dictionary_get_value
- _xpc_dictionary_set_value
- _xpc_double_create
- _xpc_double_get_value
- _xpc_endpoint_create
- _xpc_equal
- _xpc_get_type
- _xpc_int64_create
- _xpc_int64_get_value
- _xpc_null_create
- _xpc_string_create
- _xpc_string_get_string_ptr
- _xpc_uint64_create
- _xpc_uint64_get_value
- _xpc_uuid_create
- _xpc_uuid_get_bytes
CStrings:
+ "CloudTelemetry"
- "A."
- "B."
- "B24@?0r*8@\"<OS_xpc_object>\"16"
- "C."
- "D."
- "E."
- "XPCErrorDescription"
- "_TtC20CloudTelemetryShared11XPCActivity"
- "_TtC20CloudTelemetryShared13XPCConnection"
- "_TtC20CloudTelemetryShared17XPCActivityHandle"
- "activity: %s, encountered unrecognized XPC activity state: %ld"
- "checkin: %s"
- "com.apple.CloudTelemetry.Shared"
- "com.apple.CloudTelemetryService"
- "com.apple.CloudTelemetryService.group"
- "conn"
- "connection released"
- "currentTask"
- "delegate"
- "disabled"
- "disabled: skipping %s"
- "done: %s"
- "handle"
- "handlerType"
- "registered: %s"
- "run: %s"
- "sendWithReply(_:)"
- "targetQ"
- "unable to register: %s, nil bundleIdentifier"
- "v16@?0@\"<OS_xpc_object>\"8"

```
