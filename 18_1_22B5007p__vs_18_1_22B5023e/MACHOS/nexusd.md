## nexusd

> `/usr/libexec/nexusd`

```diff

-750.53.0.0.0
+750.58.0.0.0
   __TEXT.__text: 0x858
   __TEXT.__auth_stubs: 0x2f0
   __TEXT.__cstring: 0x54

   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__oslogstring: 0x60
-  __TEXT.__info_plist: 0x52f
+  __TEXT.__info_plist: 0x525
   __TEXT.__unwind_info: 0x90
   __TEXT.__eh_frame: 0x44
   __DATA_CONST.__auth_got: 0x178
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xa8
+  __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x20
   __DATA.__bss: 0x10

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 13
-  Symbols:   70
+  Symbols:   78
   CStrings:  7
 
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
