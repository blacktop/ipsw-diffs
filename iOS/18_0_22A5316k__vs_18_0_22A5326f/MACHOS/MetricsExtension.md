## MetricsExtension

> `/System/Library/ExtensionKit/Extensions/MetricsExtension.appex/MetricsExtension`

```diff

-3400.46.4.0.0
-  __TEXT.__text: 0x4218
-  __TEXT.__auth_stubs: 0x650
+3400.51.1.0.0
+  __TEXT.__text: 0x4214
+  __TEXT.__auth_stubs: 0x640
   __TEXT.__const: 0x396
   __TEXT.__cstring: 0x302
   __TEXT.__swift5_typeref: 0x141

   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x90
   __TEXT.__swift5_fieldmd: 0x94
-  __TEXT.__oslogstring: 0x141
+  __TEXT.__oslogstring: 0xe1
   __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x10
   __TEXT.__unwind_info: 0x1f0
   __TEXT.__eh_frame: 0x270
-  __DATA_CONST.__auth_got: 0x328
+  __DATA_CONST.__auth_got: 0x320
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x1a8
-  __DATA_CONST.__const: 0x2d8
+  __DATA_CONST.__const: 0x320
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x168
   __DATA.__bss: 0x7c0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 122
-  Symbols:   73
-  CStrings:  25
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 124
+  Symbols:   82
+  CStrings:  24
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
- "Device running on battery and device type is not permitted to run extension in this state."

```
