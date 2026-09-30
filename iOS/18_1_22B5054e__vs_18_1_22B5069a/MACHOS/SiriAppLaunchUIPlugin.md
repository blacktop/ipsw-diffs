## SiriAppLaunchUIPlugin

> `/System/Library/Snippets/UIPlugins/SiriAppLaunchUIPlugin.bundle/SiriAppLaunchUIPlugin`

```diff

-3401.3.1.0.0
+3401.4.1.0.0
   __TEXT.__text: 0xf0
   __TEXT.__auth_stubs: 0x60
   __TEXT.__cstring: 0x33

   __DATA_CONST.__auth_got: 0x30
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x150
+  __DATA_CONST.__const: 0x158
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
   Functions: 8
-  Symbols:   50
+  Symbols:   51
   CStrings:  1
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
