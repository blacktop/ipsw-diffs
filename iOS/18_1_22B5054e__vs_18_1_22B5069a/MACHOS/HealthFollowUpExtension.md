## HealthFollowUpExtension

> `/System/Library/PrivateFrameworks/HealthAppSupport.framework/PlugIns/HealthFollowUpExtension.appex/HealthFollowUpExtension`

```diff

-5200.1.9.1.2
+5200.1.15.1.2
   __TEXT.__text: 0x17d0
   __TEXT.__auth_stubs: 0x470
   __TEXT.__objc_stubs: 0x200

   __DATA_CONST.__auth_got: 0x240
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x148
+  __DATA_CONST.__const: 0x150
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
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
   Functions: 30
-  Symbols:   111
+  Symbols:   112
   CStrings:  57
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
