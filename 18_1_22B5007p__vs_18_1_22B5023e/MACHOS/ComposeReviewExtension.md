## ComposeReviewExtension

> `/System/Library/ExtensionKit/Extensions/ComposeReviewExtension.appex/ComposeReviewExtension`

```diff

-6.0.60.0.0
+6.1.1.2.1
   __TEXT.__text: 0x277c
   __TEXT.__auth_stubs: 0x5c0
   __TEXT.__const: 0x262

   __DATA_CONST.__auth_got: 0x2e0
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x1b0
-  __DATA_CONST.__const: 0x160
+  __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8
   __DATA.__data: 0x108

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftWebKit.dylib
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
   Functions: 93
-  Symbols:   74
+  Symbols:   82
   CStrings:  3
 
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
