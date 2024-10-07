## videosubscriptionsd

> `/usr/libexec/videosubscriptionsd`

```diff

-561.10.3.0.0
+561.10.5.0.0
   __TEXT.__text: 0xd094
   __TEXT.__auth_stubs: 0x6e0
   __TEXT.__objc_stubs: 0x23c0

   __TEXT.__unwind_info: 0x370
   __DATA_CONST.__auth_got: 0x380
   __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__const: 0x878
+  __DATA_CONST.__const: 0x880
   __DATA_CONST.__cfstring: 0x420
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x40

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 298
-  Symbols:   230
+  Symbols:   231
   CStrings:  713
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
