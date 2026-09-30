## appleidsetupd

> `/usr/libexec/appleidsetupd`

```diff

-45.1.0.0.0
-  __TEXT.__text: 0xe18
+47.0.0.0.0
+  __TEXT.__text: 0xda4
   __TEXT.__auth_stubs: 0x260
   __TEXT.__const: 0x4a
-  __TEXT.__swift5_typeref: 0x29
+  __TEXT.__swift5_typeref: 0x27
   __TEXT.__swift5_capture: 0x20
   __TEXT.__objc_methname: 0x13
   __TEXT.__swift5_entry: 0x8

   __DATA_CONST.__auth_got: 0x130
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__linkguard: 0xe
   __DATA.__objc_selrefs: 0x10

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftWebKit.dylib
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
   Functions: 17
-  Symbols:   71
+  Symbols:   79
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
