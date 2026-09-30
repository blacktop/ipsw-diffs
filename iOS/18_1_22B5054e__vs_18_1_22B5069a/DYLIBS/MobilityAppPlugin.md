## MobilityAppPlugin

> `/System/Library/Health/FeedItemPlugins/MobilityAppPlugin.healthplugin/MobilityAppPlugin`

```diff

-5200.1.9.1.2
+5200.1.15.1.2
   __TEXT.__text: 0x3d740
   __TEXT.__auth_stubs: 0x2340
   __TEXT.__objc_methlist: 0x124

   __TEXT.__objc_methname: 0x1ccc
   __TEXT.__objc_methtype: 0xdf5
   __DATA_CONST.__got: 0x800
-  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__const: 0x128
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 1131
-  Symbols:   241
+  Symbols:   242
   CStrings:  687
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
