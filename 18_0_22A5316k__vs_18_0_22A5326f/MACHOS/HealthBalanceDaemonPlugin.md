## HealthBalanceDaemonPlugin

> `/System/Library/Health/Plugins/HealthBalanceDaemonPlugin.bundle/HealthBalanceDaemonPlugin`

```diff

-5132.0.0.0.0
+5138.0.1.1.0
   __TEXT.__text: 0x178
   __TEXT.__auth_stubs: 0x60
   __TEXT.__const: 0x8e

   __TEXT.__unwind_info: 0x68
   __DATA_CONST.__auth_got: 0x30
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x88
+  __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x48
   __DATA.__objc_selrefs: 0x10

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
   Functions: 7
-  Symbols:   29
+  Symbols:   37
   CStrings:  3
 
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