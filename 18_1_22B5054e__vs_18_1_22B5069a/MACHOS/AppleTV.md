## AppleTV

> `/private/var/staged_system_apps/AppleTV.app/AppleTV`

```diff

-973.10.18.0.1
+973.11.1.0.0
   __TEXT.__text: 0xc17c
   __TEXT.__auth_stubs: 0x9e0
   __TEXT.__objc_stubs: 0x1120

   __DATA_CONST.__auth_got: 0x500
   __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__auth_ptr: 0x100
-  __DATA_CONST.__const: 0x8f0
+  __DATA_CONST.__const: 0x8f8
   __DATA_CONST.__cfstring: 0x2e0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 425
-  Symbols:   292
+  Symbols:   293
   CStrings:  480
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
