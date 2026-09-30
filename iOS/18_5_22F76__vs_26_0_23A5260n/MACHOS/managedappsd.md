## managedappsd

> `/usr/libexec/managedappsd`

```diff

-20.5.1.2.0
-  __TEXT.__text: 0x848
-  __TEXT.__auth_stubs: 0x220
+43.0.0.0.0
+  __TEXT.__text: 0x6d8
+  __TEXT.__auth_stubs: 0x200
   __TEXT.__const: 0x42
   __TEXT.__objc_methname: 0x13
   __TEXT.__oslogstring: 0x8c
   __TEXT.__swift5_entry: 0x8
   __TEXT.__cstring: 0x66
   __TEXT.__unwind_info: 0x78
-  __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x110
+  __TEXT.__eh_frame: 0x40
+  __DATA_CONST.__auth_got: 0x100
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x78
+  __DATA_CONST.__const: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x10
   __DATA.__data: 0x8

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
-  UUID: AA567AA1-23A2-311E-9D02-68694004CA19
+  UUID: E33F9C3A-D6D1-3B04-A110-60BE96864CAA
   Functions: 6
-  Symbols:   53
+  Symbols:   47
   CStrings:  10
 
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
- _objc_release_x22
- _objc_release_x24
Functions:
~ sub_10000113c -> sub_10000105c : 576 -> 388
~ sub_10000137c -> sub_1000011e0 : 548 -> 368

```
