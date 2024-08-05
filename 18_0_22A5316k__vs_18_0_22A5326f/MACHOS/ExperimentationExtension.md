## ExperimentationExtension

> `/System/Library/ExtensionKit/Extensions/ExperimentationExtension.appex/ExperimentationExtension`

```diff

-3400.46.4.0.0
-  __TEXT.__text: 0x3da8
-  __TEXT.__auth_stubs: 0x5f0
+3400.51.1.0.0
+  __TEXT.__text: 0x3d34
+  __TEXT.__auth_stubs: 0x5e0
   __TEXT.__const: 0x39e
   __TEXT.__cstring: 0x2f2
   __TEXT.__swift5_typeref: 0x119

   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x90
   __TEXT.__swift5_fieldmd: 0x94
-  __TEXT.__oslogstring: 0x141
+  __TEXT.__oslogstring: 0xe1
   __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x10
   __TEXT.__unwind_info: 0x1e8
   __TEXT.__eh_frame: 0x238
-  __DATA_CONST.__auth_got: 0x2f8
+  __DATA_CONST.__auth_got: 0x2f0
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x1a8
-  __DATA_CONST.__const: 0x2d8
+  __DATA_CONST.__const: 0x320
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x148
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
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 119
-  Symbols:   72
-  CStrings:  25
+  Symbols:   81
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
