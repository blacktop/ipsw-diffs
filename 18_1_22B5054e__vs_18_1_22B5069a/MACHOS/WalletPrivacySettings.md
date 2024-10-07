## WalletPrivacySettings

> `/System/Library/PreferenceBundles/Privacy/WalletPrivacySettings.bundle/WalletPrivacySettings`

```diff

-224.1.4.0.0
+224.1.6.0.0
   __TEXT.__text: 0x20e20
   __TEXT.__auth_stubs: 0x1080
   __TEXT.__objc_methlist: 0x218

   __DATA_CONST.__auth_got: 0x840
   __DATA_CONST.__got: 0x328
   __DATA_CONST.__auth_ptr: 0x288
-  __DATA_CONST.__const: 0x5a0
+  __DATA_CONST.__const: 0x5a8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
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
   Functions: 375
-  Symbols:   181
+  Symbols:   182
   CStrings:  224
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
