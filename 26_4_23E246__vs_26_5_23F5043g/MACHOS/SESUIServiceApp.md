## SESUIServiceApp

> `/Applications/SESUIServiceApp.app/SESUIServiceApp`

```diff

-64.24.0.0.0
+65.2.1.0.0
   __TEXT.__text: 0xf7cc
   __TEXT.__auth_stubs: 0xb60
   __TEXT.__objc_stubs: 0x920

   __DATA_CONST.__auth_got: 0x5c0
   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x100
-  __DATA_CONST.__const: 0x9e0
+  __DATA_CONST.__const: 0x9e8
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0xa0

   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9B493E38-2408-32DD-80EC-48B91B773593
+  UUID: B6058FC3-7D7C-3C32-A6F4-14382C02B06E
   Functions: 299
-  Symbols:   308
+  Symbols:   309
   CStrings:  394
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCallKit

```
