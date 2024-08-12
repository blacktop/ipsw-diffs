## DevicePropertiesExtension

> `/System/Library/ExtensionKit/Extensions/DevicePropertiesExtension.appex/DevicePropertiesExtension`

```diff

-3400.46.4.0.0
-  __TEXT.__text: 0x46c8
-  __TEXT.__auth_stubs: 0x660
+3401.5.1.0.0
+  __TEXT.__text: 0x46b8
+  __TEXT.__auth_stubs: 0x640
   __TEXT.__const: 0x39e
   __TEXT.__cstring: 0x2f2
   __TEXT.__swift5_typeref: 0x11f

   __TEXT.__constg_swiftt: 0x90
   __TEXT.__swift5_fieldmd: 0xa0
   __TEXT.__objc_methname: 0x38
-  __TEXT.__oslogstring: 0x19b
+  __TEXT.__oslogstring: 0x131
   __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x1f0
-  __TEXT.__eh_frame: 0x238
-  __DATA_CONST.__auth_got: 0x330
+  __TEXT.__unwind_info: 0x1f8
+  __TEXT.__eh_frame: 0x230
+  __DATA_CONST.__auth_got: 0x320
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x1b0
-  __DATA_CONST.__const: 0x2d8
+  __DATA_CONST.__const: 0x320
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x18
   __DATA.__data: 0x150

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
-  Functions: 120
-  Symbols:   78
-  CStrings:  30
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 122
+  Symbols:   87
+  CStrings:  29
 
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
