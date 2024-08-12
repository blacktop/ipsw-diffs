## webinspectord

> `/usr/libexec/webinspectord`

```diff

-7619.1.22.4.0
+7619.1.26.20.1
   __TEXT.__text: 0x994
   __TEXT.__auth_stubs: 0x270
   __TEXT.__objc_stubs: 0xa0

   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__info_plist: 0x52b
+  __TEXT.__info_plist: 0x52e
   __TEXT.__unwind_info: 0xb0
   __DATA_CONST.__auth_got: 0x140
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0xe8
+  __DATA_CONST.__const: 0x128
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

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
   Functions: 19
-  Symbols:   68
+  Symbols:   76
   CStrings:  21
 
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
