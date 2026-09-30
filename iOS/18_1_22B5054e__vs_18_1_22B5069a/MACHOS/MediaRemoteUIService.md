## MediaRemoteUIService

> `/Applications/MediaRemoteUIService.app/MediaRemoteUIService`

```diff

-4024.200.18.0.0
+4024.210.4.0.0
   __TEXT.__text: 0x693c
   __TEXT.__auth_stubs: 0xb70
   __TEXT.__objc_stubs: 0xe0

   __DATA_CONST.__auth_got: 0x5c0
   __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__auth_ptr: 0x258
-  __DATA_CONST.__const: 0x258
+  __DATA_CONST.__const: 0x260
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x30
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
   Functions: 167
-  Symbols:   359
+  Symbols:   360
   CStrings:  298
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
