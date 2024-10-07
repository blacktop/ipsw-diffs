## healthappd

> `/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd`

```diff

-5200.1.9.1.2
+5200.1.15.1.2
   __TEXT.__text: 0x32104
   __TEXT.__auth_stubs: 0x1eb0
   __TEXT.__objc_methlist: 0x1bc

   __DATA_CONST.__auth_got: 0xf58
   __DATA_CONST.__got: 0x5d8
   __DATA_CONST.__auth_ptr: 0x388
-  __DATA_CONST.__const: 0x1188
+  __DATA_CONST.__const: 0x1190
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x58
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
   Functions: 683
-  Symbols:   785
+  Symbols:   786
   CStrings:  395
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
