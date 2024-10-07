## HealthBalanceAppPluginBundle

> `/System/Library/Health/FeedItemPlugins/HealthBalanceAppPluginBundle.healthplugin/HealthBalanceAppPluginBundle`

```diff

-5200.1.9.1.2
+5200.1.15.1.2
   __TEXT.__text: 0x2f64
   __TEXT.__auth_stubs: 0x540
   __TEXT.__const: 0x31c

   __DATA_CONST.__auth_got: 0x2a0
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x120
-  __DATA_CONST.__const: 0x200
+  __DATA_CONST.__const: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x1b0
   __DATA.__objc_selrefs: 0x40

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 91
-  Symbols:   104
+  Symbols:   105
   CStrings:  33
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
