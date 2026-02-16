## CloudTelemetryService

> `/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService`

```diff

-2320.10.0.0.0
-  __TEXT.__text: 0x77f48
-  __TEXT.__auth_stubs: 0x2130
+2350.100.1.0.0
+  __TEXT.__text: 0x75858
+  __TEXT.__auth_stubs: 0x1fc0
+  __TEXT.__objc_stubs: 0x660
   __TEXT.__objc_methlist: 0x14c
-  __TEXT.__const: 0x5088
-  __TEXT.__oslogstring: 0x1ac0
-  __TEXT.__cstring: 0x2a40
-  __TEXT.__objc_methname: 0x67d
-  __TEXT.__swift5_typeref: 0x12e3
-  __TEXT.__constg_swiftt: 0x1790
-  __TEXT.__swift5_reflstr: 0xfe4
-  __TEXT.__swift5_fieldmd: 0x1a50
-  __TEXT.__swift5_capture: 0x320
+  __TEXT.__const: 0x4a08
+  __TEXT.__oslogstring: 0x19c7
+  __TEXT.__cstring: 0x1ff7
+  __TEXT.__swift5_typeref: 0x110f
+  __TEXT.__objc_classname: 0x523
+  __TEXT.__objc_methname: 0xad7
+  __TEXT.__objc_methtype: 0x2d9
+  __TEXT.__constg_swiftt: 0x1494
+  __TEXT.__swift5_reflstr: 0xe8a
+  __TEXT.__swift5_fieldmd: 0x17d0
+  __TEXT.__swift5_capture: 0x284
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_assocty: 0x140
-  __TEXT.__swift5_proto: 0x3f0
-  __TEXT.__swift5_types: 0x204
-  __TEXT.__objc_classname: 0x6a
-  __TEXT.__objc_methtype: 0x1fe
-  __TEXT.__swift_as_entry: 0x160
-  __TEXT.__swift_as_ret: 0x19c
-  __TEXT.__swift5_protos: 0x30
+  __TEXT.__swift5_assocty: 0x108
+  __TEXT.__swift5_proto: 0x3c8
+  __TEXT.__swift5_types: 0x1d0
+  __TEXT.__swift_as_entry: 0x14c
+  __TEXT.__swift_as_ret: 0x18c
+  __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_mpenum: 0x20
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x1e78
-  __TEXT.__eh_frame: 0x5264
-  __DATA_CONST.__auth_got: 0x1098
-  __DATA_CONST.__got: 0x4d8
-  __DATA_CONST.__auth_ptr: 0x5a8
-  __DATA_CONST.__const: 0x3b38
-  __DATA_CONST.__objc_classlist: 0xc8
+  __TEXT.__unwind_info: 0x1bb0
+  __TEXT.__eh_frame: 0x500c
+  __DATA_CONST.__auth_got: 0xfe8
+  __DATA_CONST.__got: 0x3a8
+  __DATA_CONST.__auth_ptr: 0x558
+  __DATA_CONST.__const: 0x3658
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA.__objc_const: 0x19d0
+  __DATA.__objc_const: 0x1708
   __DATA.__objc_selrefs: 0x258
   __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x25d0
-  __DATA.__bss: 0x67d0
-  __DATA.__common: 0x268
+  __DATA.__data: 0x2258
+  __DATA.__common: 0x240
+  __DATA.__bss: 0x63e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/C2.framework/C2
+  - /System/Library/PrivateFrameworks/CloudTelemetryShared.dylib
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 76E1790A-71AC-3CAE-809E-98B2C11983F3
-  Functions: 2082
-  Symbols:   320
-  CStrings:  502
+  UUID: 984B388D-FBC1-357A-9C50-B219869A647E
+  Functions: 1814
+  Symbols:   241
+  CStrings:  478
 
Symbols:
+ _objc_retain_x28
+ _swift_bridgeObjectRelease_n
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
- _malloc
- _swift_unknownObjectWeakAssign
- _swift_unknownObjectWeakDestroy
- _swift_unknownObjectWeakInit
- _swift_unknownObjectWeakLoadStrong
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
- _xpc_connection_copy_entitlement_value
- _xpc_connection_create
- _xpc_connection_create_from_endpoint
- _xpc_connection_create_mach_service
- _xpc_connection_get_euid
- _xpc_connection_send_message_with_reply
- _xpc_connection_set_event_handler
- _xpc_connection_set_target_queue
- _xpc_data_create
- _xpc_data_get_bytes_ptr
- _xpc_data_get_length
- _xpc_date_create
- _xpc_date_get_value
- _xpc_dictionary_create_empty
- _xpc_dictionary_get_string
- _xpc_dictionary_get_value
- _xpc_dictionary_set_value
- _xpc_double_create
- _xpc_double_get_value
- _xpc_endpoint_create
- _xpc_equal
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
- "A."
- "B."
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
- "com.apple.CloudTelemetryService.group"
- "connection released"
- "currentTask"
- "delegate"
- "disabled"
- "disabled: skipping %s"
- "done: %s"
- "handlerType"
- "registered: %s"
- "run: %s"
- "sendWithReply(_:)"
- "targetQ"
- "unable to register: %s, nil bundleIdentifier"
- "v16@?0@\"<OS_xpc_object>\"8"

```
