## PhotosPFLPlugin

> `/System/Library/ExtensionKit/Extensions/PhotosPFLPlugin.appex/PhotosPFLPlugin`

```diff

-710.22.200.0.0
+712.0.160.0.0
   __TEXT.__text: 0x29f0
   __TEXT.__auth_stubs: 0x550
   __TEXT.__const: 0x230

   __DATA_CONST.__auth_got: 0x2a8
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__auth_ptr: 0x120
-  __DATA_CONST.__const: 0x2b0
+  __DATA_CONST.__const: 0x2b8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 76
-  Symbols:   94
+  Symbols:   95
   CStrings:  11
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
