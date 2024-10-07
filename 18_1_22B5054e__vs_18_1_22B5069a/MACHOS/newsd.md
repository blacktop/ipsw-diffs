## newsd

> `/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd`

```diff

-5588.0.0.0.0
+5593.0.0.0.0
   __TEXT.__text: 0x1f414
   __TEXT.__auth_stubs: 0xe80
   __TEXT.__objc_stubs: 0x2d20

   __DATA_CONST.__auth_got: 0x750
   __DATA_CONST.__got: 0x358
   __DATA_CONST.__auth_ptr: 0xd8
-  __DATA_CONST.__const: 0xde0
+  __DATA_CONST.__const: 0xde8
   __DATA_CONST.__cfstring: 0x460
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xd0

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 591
-  Symbols:   405
+  Symbols:   406
   CStrings:  1095
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
