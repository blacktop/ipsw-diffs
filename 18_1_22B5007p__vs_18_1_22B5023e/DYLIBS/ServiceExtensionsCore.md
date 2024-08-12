## ServiceExtensionsCore

> `/System/Library/PrivateFrameworks/ServiceExtensionsCore.framework/ServiceExtensionsCore`

```diff

-188.0.0.0.0
+193.0.0.0.0
   __TEXT.__text: 0x1318
   __TEXT.__auth_stubs: 0x190
   __TEXT.__objc_methlist: 0x4c

   __TEXT.__objc_methtype: 0x11
   __TEXT.__objc_stubs: 0x40
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x78
+  __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x28

   __AUTH_CONST.__const: 0x1b0
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0xd8
-  __AUTH.__objc_data: 0x100
-  __AUTH.__data: 0x28
   __DATA.__data: 0x38
   __DATA.__bss: 0x230
+  __DATA_DIRTY.__objc_data: 0x100
+  __DATA_DIRTY.__data: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 63
-  Symbols:   48
+  Symbols:   56
   CStrings:  0
 
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
