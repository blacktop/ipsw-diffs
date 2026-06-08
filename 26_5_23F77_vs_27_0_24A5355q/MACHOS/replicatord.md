## replicatord

> `/System/Library/PrivateFrameworks/ReplicatorCore.framework/Support/replicatord`

```diff

-126.5.4.0.0
-  __TEXT.__text: 0x658
-  __TEXT.__auth_stubs: 0x2b0
+164.0.0.0.0
+  __TEXT.__text: 0x698
+  __TEXT.__auth_stubs: 0x2e0
   __TEXT.__objc_stubs: 0xc0
   __TEXT.__objc_methlist: 0x38
   __TEXT.__const: 0xa

   __TEXT.__objc_methtype: 0x21
   __TEXT.__swift5_entry: 0x8
   __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0x160
-  __DATA_CONST.__got: 0x28
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x90
+  __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0xa8
   __DATA.__objc_selrefs: 0x48
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x8
+  __DATA.__data: 0x10
   __DATA.__bss: 0x10
   __DATA.__common: 0x8
+  - /AppleInternal/Library/Frameworks/ReplicatorTesting.framework/ReplicatorTesting
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ReplicatorCore.framework/ReplicatorCore

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4BED6EF4-05D5-39C8-A194-04A1F02B1B14
-  Functions: 11
-  Symbols:   66
+  UUID: FE248B58-05FF-3059-BB4D-589E959570C2
+  Functions: 12
+  Symbols:   71
   CStrings:  20
 
Symbols:
+ _$s14ReplicatorCore6DaemonC8workloop13testingServerACSo17OS_dispatch_queueC_0A8Services07TestingF0_pSgtcfC
+ _$s17ReplicatorTesting10TestServerC0A8Services0bD0AAMc
+ _$s17ReplicatorTesting10TestServerCACycfC
+ _$s17ReplicatorTesting10TestServerCACycfc
+ _$s17ReplicatorTesting10TestServerCMa
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x8
+ _swift_getWitnessTable
+ _swift_release_x20
+ _swift_retain_x20
- _$s14ReplicatorCore6DaemonC8workloopACSo17OS_dispatch_queueC_tcfc
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retain_x19
- _objc_retain_x20
- _swift_allocObject
- _swift_release

```
