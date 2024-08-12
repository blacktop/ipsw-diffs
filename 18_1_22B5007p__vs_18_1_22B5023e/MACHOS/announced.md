## announced

> `/usr/libexec/announced`

```diff

-234.0.5.0.0
+234.10.2.0.0
   __TEXT.__text: 0x1188
   __TEXT.__auth_stubs: 0x380
   __TEXT.__const: 0x52

   __TEXT.__swift5_typeref: 0x3a
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__info_plist: 0x55b
+  __TEXT.__info_plist: 0x567
   __TEXT.__unwind_info: 0xa8
   __DATA_CONST.__auth_got: 0x1c0
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x38
   __DATA.__data: 0x18

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
   Functions: 20
-  Symbols:   97
+  Symbols:   105
   CStrings:  31
 
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
