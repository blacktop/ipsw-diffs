## init_exclavekit

> `/usr/libexec/init_exclavekit`

```diff

   __DATA_CONST.__auth_got: 0x28
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x30
+  __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x8
   __DATA.__common: 0x8

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 2
-  Symbols:   16
+  Symbols:   24
   CStrings:  1
 
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
