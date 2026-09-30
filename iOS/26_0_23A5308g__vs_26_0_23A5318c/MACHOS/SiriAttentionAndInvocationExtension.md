## SiriAttentionAndInvocationExtension

> `/System/Library/ExtensionKit/Extensions/SiriAttentionAndInvocationExtension.appex/SiriAttentionAndInvocationExtension`

```diff

-3500.71.1.0.0
+3500.71.1.11.1
   __TEXT.__text: 0x3910
   __TEXT.__auth_stubs: 0x560
   __TEXT.__const: 0x3ee

   __DATA_CONST.__auth_got: 0x2b0
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x1a8
-  __DATA_CONST.__const: 0x300
+  __DATA_CONST.__const: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x128
   __DATA.__bss: 0x7c0

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
-  UUID: E640F4E8-AE93-3D2E-908D-F0E8AD58B453
+  UUID: AFC9F7DE-EA80-3152-9F40-A6EC2025B8D5
   Functions: 106
-  Symbols:   76
+  Symbols:   77
   CStrings:  13
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private

```
