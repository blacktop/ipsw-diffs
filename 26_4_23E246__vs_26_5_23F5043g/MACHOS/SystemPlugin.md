## SystemPlugin

> `/System/Library/Snippets/UIPlugins/SystemPlugin.bundle/SystemPlugin`

```diff

-3520.81.1.0.0
+3525.4.2.1.1
   __TEXT.__text: 0x27fe0
   __TEXT.__auth_stubs: 0x1d10
   __TEXT.__objc_stubs: 0x720

   __DATA_CONST.__auth_got: 0xe90
   __DATA_CONST.__got: 0x5d8
   __DATA_CONST.__auth_ptr: 0x640
-  __DATA_CONST.__const: 0x10d8
+  __DATA_CONST.__const: 0x10f0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreAudio_Private.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 221F32D3-F9F5-30A6-A1A4-3EAC51FBF8A5
+  UUID: 07A9FF9D-980E-3CA2-80DA-694A38BBEC9B
   Functions: 1021
-  Symbols:   205
+  Symbols:   208
   CStrings:  252
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ __swift_FORCE_LOAD_$_swiftCallKit
+ __swift_FORCE_LOAD_$_swiftCompression

```
