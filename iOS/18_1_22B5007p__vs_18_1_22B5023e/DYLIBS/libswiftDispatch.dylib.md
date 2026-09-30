## libswiftDispatch.dylib

> `/usr/lib/swift/libswiftDispatch.dylib`

```diff

-46.0.0.0.0
+49.0.0.0.0
   __TEXT.__text: 0xfe1c
   __TEXT.__auth_stubs: 0xaa0
   __TEXT.__const: 0x2440

   __TEXT.__objc_methname: 0x13f
   __TEXT.__objc_methtype: 0xad
   __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x98
+  __DATA_CONST.__const: 0xd8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 1084
-  Symbols:   2044
+  Symbols:   2052
   CStrings:  59
 
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
