## merchantd

> `/usr/libexec/merchantd`

```diff

-130.35.0.0.0
+130.39.0.0.0
   __TEXT.__text: 0x3ac
   __TEXT.__auth_stubs: 0x130
   __TEXT.__const: 0x4a

   __DATA_CONST.__auth_got: 0x98
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x28
   __DATA.__common: 0x8

   - /usr/lib/swift/libswiftSpatial.dylib
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
   Functions: 9
-  Symbols:   44
+  Symbols:   52
   CStrings:  7
 
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
