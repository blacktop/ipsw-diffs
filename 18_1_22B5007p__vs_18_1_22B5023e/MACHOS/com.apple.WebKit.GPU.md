## com.apple.WebKit.GPU

> `/System/Library/ExtensionKit/Extensions/GPUExtension.appex/com.apple.WebKit.GPU`

```diff

-7619.1.22.4.0
+7619.1.26.20.1
   __TEXT.__text: 0x500
   __TEXT.__auth_stubs: 0x110
   __TEXT.__objc_methlist: 0x20

   __DATA_CONST.__auth_got: 0x88
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA_CONST.__const: 0xa8
+  __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x48

   - /usr/lib/swift/libswiftQuartzCore.dylib
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
   Functions: 14
-  Symbols:   40
+  Symbols:   48
   CStrings:  7
 
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
