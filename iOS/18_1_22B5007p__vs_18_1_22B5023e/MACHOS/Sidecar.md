## Sidecar

> `/Applications/Sidecar.app/Sidecar`

```diff

-340.0.0.0.0
-  __TEXT.__text: 0x157d8
+342.1.2.0.0
+  __TEXT.__text: 0x15754
   __TEXT.__auth_stubs: 0xb90
   __TEXT.__objc_methlist: 0x334
   __TEXT.__const: 0x5d0

   __DATA_CONST.__auth_got: 0x5c8
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__auth_ptr: 0x170
-  __DATA_CONST.__const: 0x8d0
+  __DATA_CONST.__const: 0x950
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8

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
-  Functions: 552
-  Symbols:   315
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 549
+  Symbols:   323
   CStrings:  466
 
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
