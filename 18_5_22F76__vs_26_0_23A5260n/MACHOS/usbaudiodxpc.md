## usbaudiodxpc

> `/System/Library/Audio/Plug-Ins/HAL/usbaudiodxpc.driver/usbaudiodxpc`

```diff

-750.4.0.0.0
-  __TEXT.__text: 0x2d54
-  __TEXT.__auth_stubs: 0x630
+802.17.0.0.0
+  __TEXT.__text: 0x2ac0
+  __TEXT.__auth_stubs: 0x5f0
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x34
   __TEXT.__objc_methname: 0x172

   __TEXT.__swift5_capture: 0x40
   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0xf8
-  __DATA_CONST.__auth_got: 0x318
+  __DATA_CONST.__auth_got: 0x2f8
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x198
+  __DATA_CONST.__const: 0x178
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x130

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: DF219C64-9E97-3134-A9D1-C28871DC44B6
+  UUID: FE27A7C8-DE3E-38A0-99FA-83DAA5242905
   Functions: 47
-  Symbols:   94
+  Symbols:   88
   CStrings:  32
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_retain_x9
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_retain_x24
- _objc_retain_x26
- _swift_release_n
CStrings:
+ "Starting new session."
- "Restarting session after error."

```
