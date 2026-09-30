## IdentityFlowPlugin

> `/System/Library/Assistant/FlowDelegatePlugins/IdentityFlowPlugin.bundle/IdentityFlowPlugin`

```diff

-3400.14.1.0.0
-  __TEXT.__text: 0x1334
+3400.16.1.0.0
+  __TEXT.__text: 0x1338
   __TEXT.__auth_stubs: 0x300
   __TEXT.__const: 0xb6
   __TEXT.__cstring: 0x378

   __DATA_CONST.__auth_got: 0x180
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x78
-  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xd8

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
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
   Functions: 32
-  Symbols:   58
+  Symbols:   66
   CStrings:  22
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_release_x21
- _objc_release_x20

```
