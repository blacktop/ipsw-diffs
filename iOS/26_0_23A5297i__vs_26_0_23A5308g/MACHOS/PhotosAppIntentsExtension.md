## PhotosAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/PhotosAppIntentsExtension.appex/PhotosAppIntentsExtension`

```diff

-800.32.101.0.0
+800.38.103.0.0
   __TEXT.__text: 0x697c
   __TEXT.__auth_stubs: 0x4a0
   __TEXT.__const: 0x60a

   __DATA_CONST.__auth_got: 0x250
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x378
-  __DATA_CONST.__const: 0x380
+  __DATA_CONST.__const: 0x388
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x160
   __DATA.__bss: 0xbb0

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
-  UUID: B42FD6E2-26B3-396E-AEDD-20F8F7D0C673
+  UUID: 41F2DF33-EB2E-309A-87BF-37CB5C4FC281
   Functions: 157
-  Symbols:   58
+  Symbols:   59
   CStrings:  74
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private

```
