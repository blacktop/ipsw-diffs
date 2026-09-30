## com.apple.weather.appremoval

> `/System/Library/AppRemovalServices/com.apple.weather.appremoval.xpc/com.apple.weather.appremoval`

```diff

-881.0.0.0.0
-  __TEXT.__text: 0x1a70
-  __TEXT.__auth_stubs: 0x3a0
+927.0.0.0.0
+  __TEXT.__text: 0x2784
+  __TEXT.__auth_stubs: 0x410
   __TEXT.__objc_stubs: 0x4c0
   __TEXT.__objc_methlist: 0x1dc
   __TEXT.__objc_classname: 0x67
-  __TEXT.__objc_methname: 0x4f6
+  __TEXT.__objc_methname: 0x4f7
   __TEXT.__objc_methtype: 0x13a
-  __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x1a7
+  __TEXT.__const: 0xaa
+  __TEXT.__cstring: 0x1b7
   __TEXT.__oslogstring: 0x2ca
-  __TEXT.__swift5_typeref: 0x26
-  __TEXT.__swift5_capture: 0x20
   __TEXT.__constg_swiftt: 0x38
+  __TEXT.__swift5_typeref: 0x48
   __TEXT.__swift5_reflstr: 0x17
   __TEXT.__swift5_fieldmd: 0x1c
+  __TEXT.__swift5_capture: 0x4c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xd8
-  __DATA_CONST.__auth_got: 0x1d8
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1e8
+  __TEXT.__swift_as_entry: 0x14
+  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__unwind_info: 0x138
+  __TEXT.__eh_frame: 0x138
+  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x220
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18

   __DATA.__objc_const: 0x378
   __DATA.__objc_selrefs: 0x1f8
   __DATA.__objc_data: 0x158
-  __DATA.__data: 0x150
+  __DATA.__data: 0x158
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: F6354A36-1220-37F0-9BD1-3964AB3C6C32
-  Functions: 37
-  Symbols:   113
+  UUID: C4E5BA4D-4BB1-3487-B9B9-30F74E901735
+  Functions: 62
+  Symbols:   118
   CStrings:  141
 
Symbols:
+ ___chkstk_darwin
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _swift_errorRelease
+ _swift_getTypeByMangledNameInContext2
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _swift_retain
CStrings:
+ "decommissionDaemonWithCompletion:"
+ "v24@0:8@?<v@?>16"
- "decomissionDaemonWithCompletion:"

```
