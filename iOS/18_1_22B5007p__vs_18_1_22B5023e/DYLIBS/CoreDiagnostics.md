## CoreDiagnostics

> `/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics`

```diff

 6.0.0.0.0
-  __TEXT.__text: 0x12664
+  __TEXT.__text: 0x12680
   __TEXT.__auth_stubs: 0xd30
   __TEXT.__objc_methlist: 0x1e8
   __TEXT.__const: 0x9e0

   __TEXT.__objc_methtype: 0xcb
   __TEXT.__objc_stubs: 0x120
   __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x40
+  __DATA_CONST.__const: 0x80
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__auth_got: 0x6a0
-  __AUTH_CONST.__auth_ptr: 0x278
+  __AUTH_CONST.__auth_ptr: 0x270
   __AUTH_CONST.__const: 0x838
   __AUTH_CONST.__objc_const: 0x550
   __AUTH.__objc_data: 0x4a0

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 384
-  Symbols:   173
+  Symbols:   181
   CStrings:  158
 
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
