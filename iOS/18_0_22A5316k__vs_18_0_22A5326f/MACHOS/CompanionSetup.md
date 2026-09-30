## CompanionSetup

> `/Applications/CompanionSetup.app/CompanionSetup`

```diff

-98.0.24.0.0
-  __TEXT.__text: 0x1388
+98.0.27.0.0
+  __TEXT.__text: 0x12a8
   __TEXT.__auth_stubs: 0x2f0
   __TEXT.__objc_methlist: 0x98
   __TEXT.__cstring: 0x22e

   __DATA_CONST.__auth_got: 0x178
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0xb0
-  __DATA_CONST.__const: 0xb0
+  __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

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
   Functions: 39
-  Symbols:   106
+  Symbols:   114
   CStrings:  209
 
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
