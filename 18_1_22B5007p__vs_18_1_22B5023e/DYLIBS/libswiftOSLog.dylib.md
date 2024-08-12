## libswiftOSLog.dylib

> `/usr/lib/swift/libswiftOSLog.dylib`

```diff

   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_methname: 0xb4
   __DATA_CONST.__got: 0x18
-  __DATA_CONST.__const: 0x38
+  __DATA_CONST.__const: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
   __AUTH_CONST.__auth_got: 0xc0

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 29
-  Symbols:   81
-  CStrings:  0
+  Symbols:   89
+  CStrings:  2
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "__ZN4TSWP16ShapeInfoArchive14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE"
+ "__ZN4TSWP16ShapeInfoArchive5ClearEv"

```
