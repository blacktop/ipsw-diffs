## ManagedApp

> `/System/Library/Frameworks/ManagedApp.framework/ManagedApp`

```diff

-20.4.18.0.0
-  __TEXT.__text: 0x1144c
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__swift5_typeref: 0x2bc
-  __TEXT.__const: 0x758
-  __TEXT.__swift5_reflstr: 0x102
+20.5.1.0.0
+  __TEXT.__text: 0x15be0
+  __TEXT.__auth_stubs: 0xa10
+  __TEXT.__swift5_typeref: 0x328
+  __TEXT.__const: 0x808
+  __TEXT.__swift5_reflstr: 0x12e
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__constg_swiftt: 0x6a0
-  __TEXT.__swift5_fieldmd: 0x1f8
-  __TEXT.__cstring: 0x300
+  __TEXT.__constg_swiftt: 0x78c
+  __TEXT.__swift5_fieldmd: 0x274
+  __TEXT.__cstring: 0x3c0
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__swift5_proto: 0x5c
-  __TEXT.__swift5_types: 0x34
-  __TEXT.__swift_as_entry: 0x88
-  __TEXT.__swift_as_ret: 0xa8
-  __TEXT.__oslogstring: 0xe14
-  __TEXT.__swift5_capture: 0xa8
-  __TEXT.__unwind_info: 0x648
-  __TEXT.__eh_frame: 0x13b8
+  __TEXT.__swift5_proto: 0x60
+  __TEXT.__swift5_types: 0x44
+  __TEXT.__swift_as_entry: 0xb0
+  __TEXT.__swift_as_ret: 0xd4
+  __TEXT.__oslogstring: 0xe04
+  __TEXT.__swift5_capture: 0x114
+  __TEXT.__unwind_info: 0x820
+  __TEXT.__eh_frame: 0x1a18
   __TEXT.__objc_methname: 0x62
-  __DATA_CONST.__got: 0xe0
+  __DATA_CONST.__got: 0x148
   __DATA_CONST.__const: 0x78
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x418
-  __AUTH_CONST.__auth_ptr: 0x1d8
-  __AUTH_CONST.__const: 0x4b0
-  __AUTH_CONST.__objc_const: 0x640
-  __AUTH.__data: 0x718
-  __DATA.__data: 0x368
-  __DATA.__bss: 0xb00
+  __AUTH_CONST.__auth_got: 0x508
+  __AUTH_CONST.__auth_ptr: 0x1f0
+  __AUTH_CONST.__const: 0x698
+  __AUTH_CONST.__objc_const: 0x6f8
+  __AUTH.__data: 0x7b0
+  __DATA.__data: 0x500
+  __DATA.__bss: 0xb80
   __DATA.__common: 0x80
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ManagedAppsCore.framework/ManagedAppsCore

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 370
-  Symbols:   119
-  CStrings:  61
+  Functions: 453
+  Symbols:   131
+  CStrings:  67
 
Symbols:
+ _bzero
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_allocError
+ _swift_allocateGenericClassMetadata
+ _swift_arrayDestroy
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
+ _swift_initClassMetadata2
+ _swift_runtimeSupportsNoncopyableTypes
+ _swift_willThrow
CStrings:
+ "Decoding configuration took longer than the maximum "
+ "Fatal error"
+ "Managed app configuration decoded successfully."
+ "Managed app configuration decoding failed with error code 0x%s, message \"%s\""
+ "ManagedApp/ConcurrencyUtils.swift"
+ "_TtC10ManagedApp16ConcurrencyUtils"
+ "makeCancellable(untrustedWork:)"
+ "mutex"
- "New managed app configuration decoded successfully."
- "New managed app configuration decoding failed with error code %ld, message %s."

```
