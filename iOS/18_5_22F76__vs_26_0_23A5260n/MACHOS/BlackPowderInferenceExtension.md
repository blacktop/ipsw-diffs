## BlackPowderInferenceExtension

> `/System/Library/ExtensionKit/Extensions/BlackPowderInferenceExtension.appex/BlackPowderInferenceExtension`

```diff

-43.730.0.0.0
+70.0.0.0.0
   __TEXT.__text: 0x1b0
   __TEXT.__auth_stubs: 0xa0
   __TEXT.__const: 0xaa

   __DATA_CONST.__auth_got: 0x50
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x88
+  __DATA_CONST.__const: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x48
   __DATA.__objc_data: 0x48

   - /System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 36B0F55C-8609-3DA5-9B28-546576D413E3
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: B7E0B11B-AC87-3071-B47C-7BF8CD89624F
   Functions: 7
-  Symbols:   31
+  Symbols:   32
   CStrings:  1
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swiftsimd
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd

```
