## ScreenSharingAccessibilityServer

> `/System/Library/AccessibilityBundles/ScreenSharingAccessibilityServer.axuiservice/ScreenSharingAccessibilityServer`

```diff

-74.0.0.0.0
+75.0.0.0.0
   __TEXT.__text: 0x3f24
   __TEXT.__auth_stubs: 0x640
   __TEXT.__objc_methlist: 0x21c

   __DATA_CONST.__auth_got: 0x320
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0x148
+  __DATA_CONST.__const: 0x150
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F15D8764-4271-3DD8-ABE2-F43FC1C2B8C3
+  UUID: F629218C-E7E9-3E33-B566-4E9672C10279
   Functions: 66
-  Symbols:   86
+  Symbols:   87
   CStrings:  87
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private

```
