## swtransparency-sysdiagnose

> `/usr/libexec/swtransparency-sysdiagnose`

```diff

-1218.120.15.0.0
-  __TEXT.__text: 0x1d48
-  __TEXT.__auth_stubs: 0x470
+1547.0.6.0.0
+  __TEXT.__text: 0x1d5c
+  __TEXT.__auth_stubs: 0x480
   __TEXT.__const: 0x21e
   __TEXT.__cstring: 0xa4
   __TEXT.__swift5_typeref: 0x89

   __TEXT.__swift5_types: 0x8
   __TEXT.__unwind_info: 0x140
   __TEXT.__eh_frame: 0x70
-  __DATA_CONST.__auth_got: 0x238
-  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__auth_got: 0x240
+  __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x118
-  __DATA_CONST.__const: 0x180
+  __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x10
   __DATA.__data: 0xd0

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
-  UUID: 9ED2C518-AEED-3B41-A0C6-4EC19B75360D
+  UUID: 5097CCBE-3A6D-3513-A073-71048241980D
   Functions: 70
-  Symbols:   137
+  Symbols:   134
   CStrings:  7
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _swift_coroFrameAlloc
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
Functions:
~ sub_100001de4 -> sub_100001d04 : 108 -> 132
~ sub_100002570 -> sub_1000024a8 : 80 -> 76

```
