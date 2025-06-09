## AppProtectionDaemon

> `/System/Library/PrivateFrameworks/AppProtectionDaemon.framework/AppProtectionDaemon`

```diff

-35.2.8.0.0
-  __TEXT.__text: 0xa600
-  __TEXT.__auth_stubs: 0x940
+38.0.0.0.0
+  __TEXT.__text: 0x8e60
+  __TEXT.__auth_stubs: 0x8b0
   __TEXT.__objc_methlist: 0x134
-  __TEXT.__const: 0x1ee
+  __TEXT.__const: 0x20e
   __TEXT.__cstring: 0x148
   __TEXT.__constg_swiftt: 0x140
   __TEXT.__swift5_typeref: 0x1e2

   __TEXT.__swift5_types: 0x14
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x1e8
-  __TEXT.__eh_frame: 0x2f0
+  __TEXT.__unwind_info: 0x228
+  __TEXT.__eh_frame: 0x3b8
   __TEXT.__objc_classname: 0x1b
   __TEXT.__objc_methname: 0x1e7
   __TEXT.__objc_methtype: 0xad

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xf8
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x4a8
-  __AUTH_CONST.__const: 0x2c8
+  __AUTH_CONST.__auth_got: 0x460
+  __AUTH_CONST.__const: 0x2f0
   __AUTH_CONST.__objc_const: 0x288
   __AUTH.__objc_data: 0x48
-  __DATA.__data: 0x120
+  __DATA.__data: 0x110
   __DATA_DIRTY.__objc_data: 0x80
-  __DATA_DIRTY.__data: 0x228
+  __DATA_DIRTY.__data: 0x218
   __DATA_DIRTY.__common: 0x20
   __DATA_DIRTY.__bss: 0x180
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 0F5FA0F5-178A-3E86-A9AF-F009109D7336
-  Functions: 124
-  Symbols:   244
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: ED906121-8465-301F-BAD5-98B9265401C5
+  Functions: 131
+  Symbols:   236
   CStrings:  80
 
Symbols:
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_AppProtectionDaemon
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_AppProtectionDaemon
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_AppProtectionDaemon
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AppProtectionDaemon
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AppProtectionDaemon
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AppProtectionDaemon
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_AppProtectionDaemon
+ _objc_retain_x23
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_AppProtectionDaemon
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_AppProtectionDaemon
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_AppProtectionDaemon
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_AppProtectionDaemon
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_AppProtectionDaemon
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_AppProtectionDaemon
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_AppProtectionDaemon
- _objc_release_x24
- _objc_release_x25
- _objc_release_x27
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x8
- _swift_bridgeObjectRetain_n
- _swift_retain_n
- _swift_willThrow

```
