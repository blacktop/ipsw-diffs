## migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

-829.40.175.0.0
+829.40.191.0.0
   __TEXT.__text: 0x14358
   __TEXT.__auth_stubs: 0xce0
   __TEXT.__objc_methlist: 0x34c

   __DATA_CONST.__auth_got: 0x670
   __DATA_CONST.__got: 0x290
   __DATA_CONST.__auth_ptr: 0x1f8
-  __DATA_CONST.__const: 0x9e8
+  __DATA_CONST.__const: 0x9f0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F1E9BDDC-E8D8-3BD8-991E-4B53A4EEF5A8
+  UUID: F33FD9FD-2EFA-3F36-B2FB-DB132F433794
   Functions: 430
-  Symbols:   374
+  Symbols:   375
   CStrings:  172
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression

```
