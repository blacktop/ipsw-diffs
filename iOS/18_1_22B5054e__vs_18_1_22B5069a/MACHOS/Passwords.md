## Passwords

> `/private/var/staged_system_apps/Passwords.app/Passwords`

```diff

-619.2.5.10.3
+619.2.8.10.3
   __TEXT.__text: 0x6cc0
   __TEXT.__auth_stubs: 0x6d0
   __TEXT.__const: 0x204

   __DATA_CONST.__auth_got: 0x368
   __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__auth_ptr: 0x1e8
-  __DATA_CONST.__const: 0x238
+  __DATA_CONST.__const: 0x240
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x120

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 107
-  Symbols:   260
+  Symbols:   261
   CStrings:  28
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
