## com.apple.mlhost.SampleWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.SampleWorker.appex/com.apple.mlhost.SampleWorker`

```diff

-3.2.14.0.0
-  __TEXT.__text: 0x8e74
+3.2.17.0.0
+  __TEXT.__text: 0x8f40
   __TEXT.__auth_stubs: 0xb00
   __TEXT.__const: 0x598
   __TEXT.__cstring: 0x3c4

   __DATA_CONST.__auth_got: 0x580
   __DATA_CONST.__got: 0x128
   __DATA_CONST.__auth_ptr: 0x218
-  __DATA_CONST.__const: 0x3c0
+  __DATA_CONST.__const: 0x400
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x40
   __DATA.__data: 0x200

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
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
   Functions: 187
-  Symbols:   88
+  Symbols:   96
   CStrings:  49
 
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
