## Diagnostic-6004

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004`

```diff

-795.0.0.0.0
+815.0.0.0.0
   __TEXT.__text: 0x1365c
   __TEXT.__auth_stubs: 0xc60
   __TEXT.__objc_stubs: 0x160

   __TEXT.__eh_frame: 0x108
   __DATA_CONST.__auth_got: 0x638
   __DATA_CONST.__got: 0x260
-  __DATA_CONST.__auth_ptr: 0x2d8
-  __DATA_CONST.__const: 0xd38
+  __DATA_CONST.__auth_ptr: 0x2e0
+  __DATA_CONST.__const: 0xd78
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x28

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 478
-  Symbols:   152
+  Symbols:   160
   CStrings:  264
 
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
