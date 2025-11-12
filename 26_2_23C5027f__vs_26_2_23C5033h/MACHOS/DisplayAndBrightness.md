## DisplayAndBrightness

> `/System/Library/PreferenceBundles/DisplayAndBrightness.bundle/DisplayAndBrightness`

```diff

-1184.103.0.0.0
+1185.2.1.0.0
   __TEXT.__text: 0x22c4
   __TEXT.__auth_stubs: 0x4b0
   __TEXT.__objc_stubs: 0x140

   __DATA_CONST.__auth_got: 0x260
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x80
-  __DATA_CONST.__const: 0x270
+  __DATA_CONST.__const: 0x280
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 48B72F61-2723-3298-91F7-E5B701219DDF
+  UUID: BE4E2BB0-CF01-366A-869C-F4ECA84D84CB
   Functions: 46
-  Symbols:   108
+  Symbols:   110
   CStrings:  55
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCompression

```
