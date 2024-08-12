## PFLCSLAppStore

> `/System/Library/ExtensionKit/Extensions/PFLCSLAppStore.appex/PFLCSLAppStore`

```diff

-1.3.19.0.0
+1.3.22.0.0
   __TEXT.__text: 0x22d8c
   __TEXT.__auth_stubs: 0x830
   __TEXT.__objc_stubs: 0x1a60

   __DATA_CONST.__auth_got: 0x428
   __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__auth_ptr: 0xc0
-  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__const: 0x140
   __DATA_CONST.__cfstring: 0x1860
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x10

   - /usr/lib/swift/libswiftQuartzCore.dylib
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
   Functions: 202
-  Symbols:   518
+  Symbols:   526
   CStrings:  606
 
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
