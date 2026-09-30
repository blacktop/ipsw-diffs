## HealthSettings

> `/System/Library/PreferenceBundles/HealthSettings.bundle/HealthSettings`

```diff

-5200.1.9.1.2
+5200.1.15.1.2
   __TEXT.__text: 0x5f68
   __TEXT.__auth_stubs: 0x400
   __TEXT.__objc_stubs: 0x1980

   __TEXT.__unwind_info: 0x2a8
   __DATA_CONST.__auth_got: 0x210
   __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__const: 0x400
+  __DATA_CONST.__const: 0x408
   __DATA_CONST.__cfstring: 0x440
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x10

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 198
-  Symbols:   190
+  Symbols:   191
   CStrings:  482
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
