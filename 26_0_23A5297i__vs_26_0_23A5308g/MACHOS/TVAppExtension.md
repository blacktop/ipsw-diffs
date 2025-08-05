## TVAppExtension

> `/System/Library/ExtensionKit/Extensions/TVAppExtension.appex/TVAppExtension`

```diff

-1060.0.0.0.1
+1061.0.3.0.1
   __TEXT.__text: 0x72cc
   __TEXT.__auth_stubs: 0x950
   __TEXT.__objc_methlist: 0xd8

   __DATA_CONST.__auth_got: 0x4a8
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x1c0
-  __DATA_CONST.__const: 0x298
+  __DATA_CONST.__const: 0x2a0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F6C44CF3-E917-3A5E-9540-989CD079AEAD
+  UUID: 18039185-E2BD-36D6-89BA-EC8E2735342F
   Functions: 187
-  Symbols:   128
+  Symbols:   129
   CStrings:  85
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private

```
