## liveactivitiesd

> `/System/Library/PrivateFrameworks/SessionCore.framework/Support/liveactivitiesd`

```diff

-198.100.0.0.0
+200.100.0.0.0
   __TEXT.__text: 0x630
   __TEXT.__auth_stubs: 0x2d0
   __TEXT.__objc_stubs: 0x80

   __DATA_CONST.__auth_got: 0x170
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xc0
+  __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xa8

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
   Functions: 9
-  Symbols:   73
+  Symbols:   81
   CStrings:  20
 
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
