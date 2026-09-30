## homeenergyd

> `/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/Support/homeenergyd`

```diff

-213.0.0.0.0
+222.0.0.0.0
   __TEXT.__text: 0x41d4
   __TEXT.__auth_stubs: 0x5c0
   __TEXT.__const: 0x7a

   __DATA_CONST.__auth_got: 0x2e0
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x110
+  __DATA_CONST.__const: 0x150
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 49
-  Symbols:   143
+  Symbols:   151
   CStrings:  37
 
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
