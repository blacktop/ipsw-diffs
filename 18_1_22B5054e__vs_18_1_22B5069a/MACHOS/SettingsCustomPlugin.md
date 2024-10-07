## SettingsCustomPlugin

> `/System/Library/Snippets/UIPlugins/SettingsCustomPlugin.bundle/SettingsCustomPlugin`

```diff

-3401.18.1.0.0
+3401.19.1.0.0
   __TEXT.__text: 0x7dc4
   __TEXT.__auth_stubs: 0x900
   __TEXT.__const: 0x48e

   __DATA_CONST.__auth_got: 0x480
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x258
-  __DATA_CONST.__const: 0x300
+  __DATA_CONST.__const: 0x308
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
   Functions: 290
-  Symbols:   113
+  Symbols:   114
   CStrings:  32
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
