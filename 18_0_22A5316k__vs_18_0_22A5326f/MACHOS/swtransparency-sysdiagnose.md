## swtransparency-sysdiagnose

> `/usr/libexec/swtransparency-sysdiagnose`

```diff

-1218.0.87.0.0
-  __TEXT.__text: 0x22b0
+1218.0.96.0.0
+  __TEXT.__text: 0x21f0
   __TEXT.__auth_stubs: 0x470
   __TEXT.__const: 0x21e
   __TEXT.__cstring: 0xd4

   __DATA_CONST.__auth_got: 0x238
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x120
-  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x10
   __DATA.__data: 0xd8

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
   Functions: 79
-  Symbols:   124
+  Symbols:   132
   CStrings:  8
 
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
