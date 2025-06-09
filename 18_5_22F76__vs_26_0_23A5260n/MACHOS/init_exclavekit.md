## init_exclavekit

> `/usr/libexec/init_exclavekit`

```diff

-87.100.1.0.0
+96.0.2.0.0
   __TEXT.__text: 0x11c
   __TEXT.__auth_stubs: 0x50
   __TEXT.__const: 0x12

   __DATA_CONST.__auth_got: 0x28
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x70
+  __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x8
   __DATA.__common: 0x8

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: D3C4D20B-726A-3E0C-AED5-AD421F369890
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  UUID: 0D8BD871-7EC4-3B26-A06A-9C54672D7C32
   Functions: 2
-  Symbols:   24
+  Symbols:   20
   CStrings:  1
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd

```
