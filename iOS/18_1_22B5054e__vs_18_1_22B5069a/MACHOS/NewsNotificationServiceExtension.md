## NewsNotificationServiceExtension

> `/private/var/staged_system_apps/News.app/PlugIns/NewsNotificationServiceExtension.appex/NewsNotificationServiceExtension`

```diff

-5588.0.0.0.0
+5593.0.0.0.0
   __TEXT.__text: 0x1b3bc
   __TEXT.__auth_stubs: 0xdf0
   __TEXT.__objc_stubs: 0x11a0

   __DATA_CONST.__auth_got: 0x708
   __DATA_CONST.__got: 0x330
   __DATA_CONST.__auth_ptr: 0x1d0
-  __DATA_CONST.__const: 0xca0
+  __DATA_CONST.__const: 0xca8
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x40

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 500
-  Symbols:   282
+  Symbols:   283
   CStrings:  451
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
