## PrivacyAppIntents

> `/System/Library/ExtensionKit/Extensions/PrivacyAppIntents.appex/PrivacyAppIntents`

```diff

-1199.0.0.0.0
+1201.0.0.0.0
   __TEXT.__text: 0x5a70
   __TEXT.__auth_stubs: 0x450
   __TEXT.__const: 0x83e

   __DATA_CONST.__auth_got: 0x228
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__auth_ptr: 0x428
-  __DATA_CONST.__const: 0x638
+  __DATA_CONST.__const: 0x678
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x38
   __DATA.__data: 0x1d8

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
   Functions: 152
-  Symbols:   65
+  Symbols:   73
   CStrings:  106
 
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