## FitnessSiriSession

> `/System/Library/PrivateFrameworks/FitnessSiriSession.framework/FitnessSiriSession`

```diff

-980.0.0.0.0
+989.0.0.0.0
   __TEXT.__text: 0x8044
   __TEXT.__auth_stubs: 0x3b0
   __TEXT.__const: 0x1118

   __TEXT.__unwind_info: 0x440
   __TEXT.__eh_frame: 0x560
   __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x90
+  __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x1d8
   __AUTH_CONST.__auth_ptr: 0x208

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
   Functions: 350
-  Symbols:   60
-  CStrings:  5
+  Symbols:   68
+  CStrings:  0
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
- "_$s11ActivityKit0A15ProtectionClassON"
- "_$s11ActivityKit0A3QoSON"
- "_$s11ActivityKit16DeviceIdentifierON"
- "_$s16AdAttributionKit13AppImpressionV24compactJWSRepresentationSSvg"
- "peON"

```