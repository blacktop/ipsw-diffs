## ParsingInternal

> `/System/Library/PrivateFrameworks/ParsingInternal.framework/ParsingInternal`

```diff

-40.0.0.0.0
+42.0.0.0.0
   __TEXT.__text: 0x1add48
   __TEXT.__auth_stubs: 0x5f0
   __TEXT.__swift5_typeref: 0x4797

   __TEXT.__unwind_info: 0x1578
   __TEXT.__eh_frame: 0x2c30
   __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x8
+  __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x2f8
   __AUTH_CONST.__auth_ptr: 0x4c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 1937
-  Symbols:   63
+  Symbols:   71
   CStrings:  26
 
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
