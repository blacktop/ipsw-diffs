## ControlCenterAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/ControlCenterAppIntentsExtension.appex/ControlCenterAppIntentsExtension`

```diff

-587.100.0.0.0
+592.100.0.0.0
   __TEXT.__text: 0x29f8
   __TEXT.__auth_stubs: 0x4a0
   __TEXT.__const: 0x6c8

   __DATA_CONST.__auth_got: 0x250
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x3b8
-  __DATA_CONST.__const: 0x1f8
+  __DATA_CONST.__const: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x190
   __DATA.__common: 0x50

   - /usr/lib/swift/libswiftQuartzCore.dylib
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
   Functions: 117
-  Symbols:   42
+  Symbols:   50
   CStrings:  11
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd

```
