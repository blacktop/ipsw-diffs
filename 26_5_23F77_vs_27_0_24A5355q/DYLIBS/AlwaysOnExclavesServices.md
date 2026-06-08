## AlwaysOnExclavesServices

> `/System/Library/PrivateFrameworks/AlwaysOnExclavesServices.framework/AlwaysOnExclavesServices`

```diff

-40.100.10.0.0
-  __TEXT.__text: 0xeec
-  __TEXT.__auth_stubs: 0x300
+60.0.0.0.1
+  __TEXT.__text: 0x294c
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x268
-  __TEXT.__swift5_typeref: 0x50
-  __TEXT.__swift5_capture: 0x10
-  __TEXT.__cstring: 0x58
-  __TEXT.__constg_swiftt: 0x80
-  __TEXT.__swift5_reflstr: 0xbe
-  __TEXT.__swift5_fieldmd: 0xb4
-  __TEXT.__swift5_types: 0xc
+  __TEXT.__const: 0x340
+  __TEXT.__cstring: 0x165
+  __TEXT.__oslogstring: 0x96
+  __TEXT.__constg_swiftt: 0xd0
+  __TEXT.__swift5_typeref: 0xca
+  __TEXT.__swift5_reflstr: 0x165
+  __TEXT.__swift5_fieldmd: 0x13c
+  __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_proto: 0x14
-  __TEXT.__unwind_info: 0xd0
+  __TEXT.__unwind_info: 0x128
   __TEXT.__eh_frame: 0x80
-  __TEXT.__objc_classname: 0x42
-  __TEXT.__objc_methname: 0x1f7
-  __TEXT.__objc_methtype: 0xc8
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0x38
-  __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x20
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x40
+  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa0
-  __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x180
-  __AUTH_CONST.__const: 0x170
-  __AUTH_CONST.__objc_const: 0x1d8
-  __DATA.__data: 0xe0
-  __DATA.__bss: 0x280
-  __DATA_DIRTY.__data: 0xb0
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x1c0
+  __AUTH_CONST.__objc_const: 0x318
+  __AUTH_CONST.__auth_got: 0x368
+  __AUTH.__objc_data: 0x50
+  __AUTH.__data: 0xb8
+  __DATA.__data: 0x200
+  __DATA.__bss: 0x200
+  __DATA_DIRTY.__data: 0xc8
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: F757BF20-6BB0-326F-A8C2-249CDBD21C45
-  Functions: 57
-  Symbols:   86
-  CStrings:  51
+  UUID: 1A0405FA-BB03-39FC-8A8B-B789AF77947B
+  Functions: 88
+  Symbols:   167
+  CStrings:  15
 
Symbols:
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$_OS_dispatch_source
+ __DATA__TtC24AlwaysOnExclavesServicesP33_6748D3F1EAC6BFB59926E695A6DCD28F18ClientErrorHandler
+ __IVARS__TtC24AlwaysOnExclavesServicesP33_6748D3F1EAC6BFB59926E695A6DCD28F18ClientErrorHandler
+ __METACLASS_DATA__TtC24AlwaysOnExclavesServicesP33_6748D3F1EAC6BFB59926E695A6DCD28F18ClientErrorHandler
+ __OBJC_$_PROTOCOL_REFS_OS_dispatch_source
+ __OBJC_$_PROTOCOL_REFS_OS_dispatch_source_mach_send
+ __OBJC_LABEL_PROTOCOL_$_OS_dispatch_source
+ __OBJC_LABEL_PROTOCOL_$_OS_dispatch_source_mach_send
+ __OBJC_PROTOCOL_$_OS_dispatch_source
+ __OBJC_PROTOCOL_$_OS_dispatch_source_mach_send
+ ___stack_chk_fail
+ ___stack_chk_guard
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ __os_log_impl
+ __swiftEmptyArrayStorage
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_AlwaysOnExclavesServices
+ __swift_stdlib_malloc_size
+ _block_copy_helper.11
+ _block_copy_helper.8
+ _block_descriptor.10
+ _block_descriptor.13
+ _block_destroy_helper.12
+ _block_destroy_helper.9
+ _bootstrap_look_up
+ _bootstrap_port
+ _bzero
+ _exclaves_lookup_service
+ _flat unique So28OS_dispatch_source_mach_send_p
+ _get_type_metadata 15Synchronization19AtomicLazyReferenceVySo28OS_dispatch_source_mach_send_pG noncopyable.2
+ _mach_port_deallocate
+ _mach_task_self_
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_release_x20
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x8
+ _objc_retain_x24
+ _os_log_type_enabled
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_deletedMethodError
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x8
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x25
+ _swift_runtimeSupportsNoncopyableTypes
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_updateClassMetadata2
+ _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
+ _symbolic So17OS_dispatch_queueC
+ _symbolic _____ 24AlwaysOnExclavesServices18ClientErrorHandler33_6748D3F1EAC6BFB59926E695A6DCD28FLLC
+ _symbolic _____ 2os6LoggerV
+ _symbolic _____Sg 24AlwaysOnExclavesServices18ClientErrorHandler33_6748D3F1EAC6BFB59926E695A6DCD28FLLC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y______pG 15Synchronization19AtomicLazyReferenceV So28OS_dispatch_source_mach_sendP
+ _symbolic y_____c 24AlwaysOnExclavesServices16ConnectionStatusO
+ _sysctlbyname
+ _xpc_connection_cancel
- _objc_release_x19
- _objc_release_x25
- _objc_release_x27
- _swift_deallocObject
- _symbolic _____Iegn_ 24AlwaysOnExclavesServices16ConnectionStatusO
- _xpc_connection_set_target_queue
CStrings:
+ "AlwaysOnExclavesServices/AlwaysOnExclavesServices.swift"
+ "Fatal error"
+ "[AlwaysOnExclavesServices] unexpected message received on xpc mach service listener."
+ "com.apple.AlwaysOnExclavesServices"
+ "com.apple.alwaysonexclaves"
+ "hasConclave"
+ "mach service %s has no conclave, falling back to com.apple.alwaysonexclaves"
+ "mach service %s not found, falling back to com.apple.alwaysonexclaves"
- "#16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "OS_xpc_object"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC24AlwaysOnExclavesServices10Connection"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "connection"
- "debugDescription"
- "description"
- "entitlementPresent"
- "hash"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "superclass"
- "v16@?0@\"<OS_xpc_object>\"8"
- "zone"

```
