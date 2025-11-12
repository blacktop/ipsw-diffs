## VPNAppIntentWidgetExtension

> `/System/Library/ExtensionKit/Extensions/VPNAppIntentWidgetExtension.appex/VPNAppIntentWidgetExtension`

```diff

-2205.60.3.0.0
+2205.60.8.0.1
   __TEXT.__text: 0x88cc
   __TEXT.__auth_stubs: 0x6c0
   __TEXT.__const: 0xf04

   __DATA_CONST.__auth_got: 0x360
   __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x4c0
-  __DATA_CONST.__const: 0x3a0
+  __DATA_CONST.__const: 0x3b0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   - /System/Library/Frameworks/WidgetKit.framework/WidgetKit
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
-  UUID: 375C4318-D046-3D18-8DD5-D65C680EFBD4
+  UUID: 2819E90F-21C2-3A86-A994-13B0E39AB497
   Functions: 327
-  Symbols:   85
+  Symbols:   87
   CStrings:  31
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCompression

```
