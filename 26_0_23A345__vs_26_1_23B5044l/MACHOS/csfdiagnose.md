## csfdiagnose

> `/usr/bin/csfdiagnose`

```diff

-301.23.0.23.0
+301.23.1.1.0
   __TEXT.__text: 0x14544
   __TEXT.__auth_stubs: 0xc50
   __TEXT.__const: 0x13d2

   __DATA_CONST.__auth_got: 0x628
   __DATA_CONST.__got: 0x210
   __DATA_CONST.__auth_ptr: 0x1e0
-  __DATA_CONST.__const: 0xcb0
+  __DATA_CONST.__const: 0xca8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x60
   __DATA.__data: 0x848

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2A6A0208-9498-358C-B66A-B06694FF62E3
+  UUID: 9221CA9E-F035-3264-B302-65973816C84D
   Functions: 449
-  Symbols:   337
+  Symbols:   336
   CStrings:  84
 
Symbols:
- __swift_FORCE_LOAD_$_swiftCoreImage

```
