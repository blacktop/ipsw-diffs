## ContactThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/ContactThumbnailExtension.appex/ContactThumbnailExtension`

```diff

-197.0.0.0.0
+199.0.0.0.0
   __TEXT.__text: 0x1c00
   __TEXT.__auth_stubs: 0x430
   __TEXT.__const: 0x39a

   __DATA_CONST.__auth_got: 0x218
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x190
-  __DATA_CONST.__const: 0xb8
+  __DATA_CONST.__const: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x18
   __DATA.__data: 0x118

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
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 65
-  Symbols:   56
+  Symbols:   64
   CStrings:  4
 
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
