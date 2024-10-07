## SleepLockScreen

> `/Applications/SleepLockScreen.app/SleepLockScreen`

```diff

-5200.1.9.1.2
+5200.1.15.1.2
   __TEXT.__text: 0xda24
   __TEXT.__auth_stubs: 0xc10
   __TEXT.__objc_stubs: 0x20

   __DATA_CONST.__auth_got: 0x610
   __DATA_CONST.__got: 0x250
   __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0x6b8
+  __DATA_CONST.__const: 0x6c0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x70
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
   Functions: 205
-  Symbols:   321
+  Symbols:   322
   CStrings:  254
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
