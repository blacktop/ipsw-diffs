## Transfer to Android

> `/Applications/Transfer to Android.app/Transfer to Android`

```diff

-829.40.175.0.0
+829.40.191.0.0
   __TEXT.__text: 0xcec
   __TEXT.__auth_stubs: 0x2c0
   __TEXT.__objc_methlist: 0x574

   __TEXT.__unwind_info: 0xb0
   __DATA_CONST.__auth_got: 0x160
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x90
+  __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A69CA304-91E8-3C7F-A897-F18D3A74851F
+  UUID: 780732E0-6F06-3CEB-A37B-2262FE649B12
   Functions: 28
-  Symbols:   78
+  Symbols:   79
   CStrings:  207
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression

```
