## Camera

> `/Applications/Camera.app/Camera`

```diff

-4015.94.1.0.0
+4015.98.3.0.0
   __TEXT.__text: 0x335c
   __TEXT.__auth_stubs: 0x4e0
   __TEXT.__objc_stubs: 0xa0

   __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__auth_ptr: 0x358
-  __DATA_CONST.__const: 0x2b0
+  __DATA_CONST.__const: 0x2f0
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftVideoToolbox.dylib
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
   Functions: 110
-  Symbols:   251
+  Symbols:   259
   CStrings:  28
 
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