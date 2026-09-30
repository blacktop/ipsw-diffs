## modelmanagerdump

> `/usr/bin/modelmanagerdump`

```diff

-121.0.0.0.0
+122.0.0.0.0
   __TEXT.__text: 0x1504
   __TEXT.__auth_stubs: 0x220
   __TEXT.__const: 0x23c

   __DATA_CONST.__auth_got: 0x110
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__auth_ptr: 0x98
-  __DATA_CONST.__const: 0x88
+  __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x88
   __DATA.__common: 0x30

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 56
-  Symbols:   70
+  Symbols:   78
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
