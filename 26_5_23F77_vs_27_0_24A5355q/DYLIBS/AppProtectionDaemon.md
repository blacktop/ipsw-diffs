## AppProtectionDaemon

> `/System/Library/PrivateFrameworks/AppProtectionDaemon.framework/AppProtectionDaemon`

```diff

-46.4.3.0.0
-  __TEXT.__text: 0x9dd4
-  __TEXT.__auth_stubs: 0x8f0
+54.0.0.0.0
+  __TEXT.__text: 0x99a8
   __TEXT.__objc_methlist: 0x134
-  __TEXT.__const: 0x28e
+  __TEXT.__const: 0x27e
   __TEXT.__constg_swiftt: 0x140
-  __TEXT.__swift5_typeref: 0x1ea
+  __TEXT.__swift5_typeref: 0x1cc
   __TEXT.__swift5_reflstr: 0x141
   __TEXT.__swift5_fieldmd: 0xe0
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__oslogstring: 0x29e
-  __TEXT.__swift5_capture: 0xb4
+  __TEXT.__swift5_capture: 0xa4
   __TEXT.__cstring: 0x98
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x210
-  __TEXT.__eh_frame: 0x348
-  __TEXT.__objc_classname: 0x74
-  __TEXT.__objc_methname: 0x2cd
-  __TEXT.__objc_methtype: 0xc7
-  __TEXT.__objc_stubs: 0x120
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x70
+  __TEXT.__swift_as_cont: 0x10
+  __TEXT.__unwind_info: 0x1f8
+  __TEXT.__eh_frame: 0x2c0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x78
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xf8
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x480
-  __AUTH_CONST.__const: 0x370
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x348
   __AUTH_CONST.__objc_const: 0x288
+  __AUTH_CONST.__auth_got: 0x4d0
   __AUTH.__objc_data: 0x48
   __DATA.__data: 0x110
   __DATA_DIRTY.__objc_data: 0x80

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E176CD92-44AE-3C1B-A11E-C0605B55D852
-  Functions: 134
-  Symbols:   241
-  CStrings:  79
+  UUID: D590152D-4E8F-3BC0-8EF8-C402A6F644A4
+  Functions: 126
+  Symbols:   268
+  CStrings:  18
 
Symbols:
+ ___swift__destructor
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.13
+ ___swift_closure_destructor.16
+ ___swift_closure_destructor.20
+ ___swift_closure_destructor.26
+ ___swift_closure_destructor.9
+ ___swift_closure_destructorTm
+ ___swift_exist.box.addr_destructor
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_AppProtectionDaemon
+ _block_copy_helper.28
+ _block_descriptor.30
+ _block_destroy_helper.29
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x28
+ _objc_retain_x22
+ _objc_retain_x25
+ _objc_retain_x26
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x3
+ _swift_release_x8
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
- _block_copy_helper.33
- _block_descriptor.35
- _block_destroy_helper.34
- _objc_release_x26
- _objc_retain
- _objc_retain_x21
- _objc_retain_x23
- _objc_retain_x24
- _objectdestroyTm
- _swift_bridgeObjectRetain_n
- _swift_stdlib_isStackAllocationSafe
- _swift_willThrowTypedImpl
- _symbolic SS3key______5valuetSg 13AppProtection07ManagedA14ProtectabilityV
- _symbolic ______p s5ErrorP
CStrings:
- "#16@0:8"
- ".cxx_destruct"
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
- "OS_os_transaction"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC19AppProtectionDaemon19iOSManagementExpert"
- "_TtC19AppProtectionDaemon9APDServer"
- "addObject:"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "description"
- "eventEmissionQueue"
- "events"
- "hash"
- "init"
- "initWithCapacity:"
- "isEqual:"
- "isHidingAppsAllowed"
- "isKindOfClass:"
- "isLockingAppsAllowed"
- "isMemberOfClass:"
- "isProxy"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "platformExpert"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "runWithArguments:"
- "self"
- "serviceQueue"
- "sharedConnection"
- "state"
- "stringWithUTF8String:"
- "superclass"
- "v16@0:8"
- "v24@0:8@16"
- "v8@?0"
- "zone"

```
