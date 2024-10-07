## ResearchApp

> `/System/Library/Health/FeedItemPlugins/ResearchApp.healthplugin/ResearchApp`

```diff

-5200.1.9.1.2
+5200.1.15.1.2
   __TEXT.__text: 0x12544
   __TEXT.__auth_stubs: 0xfb0
   __TEXT.__objc_methlist: 0x68

   __TEXT.__objc_methname: 0x4dc
   __TEXT.__objc_methtype: 0xe1
   __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__const: 0x128
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 360
-  Symbols:   145
+  Symbols:   146
   CStrings:  194
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
