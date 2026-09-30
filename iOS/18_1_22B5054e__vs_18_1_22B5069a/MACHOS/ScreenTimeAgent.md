## ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent`

```diff

-537.1.5.0.0
+537.1.8.0.0
   __TEXT.__text: 0x25e690
   __TEXT.__auth_stubs: 0x2810
   __TEXT.__objc_stubs: 0x10fc0

   __TEXT.__eh_frame: 0xe7a0
   __DATA_CONST.__auth_got: 0x1418
   __DATA_CONST.__got: 0x1470
-  __DATA_CONST.__auth_ptr: 0x6b8
-  __DATA_CONST.__const: 0xf788
+  __DATA_CONST.__auth_ptr: 0x690
+  __DATA_CONST.__const: 0xf790
   __DATA_CONST.__cfstring: 0x4820
   __DATA_CONST.__objc_classlist: 0x618
   __DATA_CONST.__objc_catlist: 0x20

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 7803
-  Symbols:   1427
+  Symbols:   1428
   CStrings:  7807
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
