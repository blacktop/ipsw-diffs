## photoanalysisd

> `/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd`

```diff

-710.22.200.0.0
+712.0.160.0.0
   __TEXT.__text: 0x2178
   __TEXT.__auth_stubs: 0x490
   __TEXT.__objc_stubs: 0xc0

   __DATA_CONST.__auth_got: 0x250
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x238
+  __DATA_CONST.__const: 0x240
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 66
-  Symbols:   134
+  Symbols:   135
   CStrings:  75
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
