## com.apple.mlhost.TelemetryWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.TelemetryWorker.appex/com.apple.mlhost.TelemetryWorker`

```diff

-3.2.14.0.0
+3.2.17.0.0
   __TEXT.__text: 0x7b9c
   __TEXT.__auth_stubs: 0x990
   __TEXT.__const: 0x3e8

   __DATA_CONST.__auth_got: 0x4c8
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x178
-  __DATA_CONST.__const: 0x4c0
+  __DATA_CONST.__const: 0x500
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x60
   __DATA.__data: 0xc8

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
   Functions: 167
-  Symbols:   82
+  Symbols:   90
   CStrings:  51
 
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
