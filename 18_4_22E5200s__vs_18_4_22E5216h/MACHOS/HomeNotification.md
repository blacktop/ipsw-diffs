## HomeNotification

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeNotification.appex/HomeNotification`

```diff

-1025.0.0.1.1
+1026.5.8.0.0
   __TEXT.__text: 0xafec
   __TEXT.__auth_stubs: 0x4e0
   __TEXT.__objc_stubs: 0x2aa0

   __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0x240
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xa38
+  __DATA_CONST.__const: 0xa40
   __DATA_CONST.__cfstring: 0x6e0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x48

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 267
-  Symbols:   223
+  Symbols:   224
   CStrings:  845
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
