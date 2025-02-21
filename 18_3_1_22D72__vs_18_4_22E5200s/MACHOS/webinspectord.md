## webinspectord

> `/usr/libexec/webinspectord`

```diff

-7620.2.4.10.7
-  __TEXT.__text: 0x994
+7621.1.10.20.6
+  __TEXT.__text: 0x998
   __TEXT.__auth_stubs: 0x270
   __TEXT.__objc_stubs: 0xa0
   __TEXT.__objc_methlist: 0x44

   __DATA_CONST.__auth_got: 0x140
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x128
+  __DATA_CONST.__const: 0x138
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_errno.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 19
-  Symbols:   76
+  Functions: 20
+  Symbols:   78
   CStrings:  21
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftQuartzCore

```
