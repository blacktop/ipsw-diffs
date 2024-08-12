## DriverManagement

> `/System/Library/PrivateFrameworks/DriverManagement.framework/DriverManagement`

```diff

 463.0.0.0.0
-  __TEXT.__text: 0x20f90
+  __TEXT.__text: 0x20f80
   __TEXT.__auth_stubs: 0xe00
   __TEXT.__objc_methlist: 0x21c
   __TEXT.__const: 0x16d8

   __TEXT.__objc_methtype: 0xbb
   __TEXT.__objc_stubs: 0x300
   __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x60
+  __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftOSLog.dylib
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
   Functions: 818
-  Symbols:   208
+  Symbols:   216
   CStrings:  187
 
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
