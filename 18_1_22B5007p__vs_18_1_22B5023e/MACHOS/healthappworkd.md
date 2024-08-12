## healthappworkd

> `/System/Library/PrivateFrameworks/HealthPluginHost.framework/XPCServices/healthappworkd.xpc/healthappworkd`

```diff

-5132.0.0.0.0
+5200.1.3.0.0
   __TEXT.__text: 0x4c8
   __TEXT.__auth_stubs: 0x280
   __TEXT.__cstring: 0x53

   __DATA_CONST.__auth_got: 0x140
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x10
   __DATA.__data: 0x20

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 4
-  Symbols:   44
+  Symbols:   52
   CStrings:  5
 
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
