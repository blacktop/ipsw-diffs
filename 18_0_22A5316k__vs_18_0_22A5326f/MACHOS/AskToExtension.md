## AskToExtension

> `/Applications/AskToMessagesHost.app/Extensions/AskToExtension.appex/AskToExtension`

```diff

-37.1.0.0.0
+39.0.0.0.0
   __TEXT.__text: 0x1610
   __TEXT.__auth_stubs: 0x410
   __TEXT.__const: 0x1ae

   __DATA_CONST.__auth_got: 0x208
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0xc8
-  __DATA_CONST.__const: 0x178
+  __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x60
   __DATA.__data: 0x40

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftVideoToolbox.dylib
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
   Functions: 44
-  Symbols:   69
+  Symbols:   77
   CStrings:  29
 
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