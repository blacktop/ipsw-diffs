## AVCPlugin

> `/System/Library/ExtensionKit/Extensions/AVCPlugin.appex/AVCPlugin`

```diff

-76.0.0.0.0
+78.0.0.0.0
   __TEXT.__text: 0x110f4
   __TEXT.__auth_stubs: 0xd20
   __TEXT.__const: 0xd90

   __DATA_CONST.__auth_got: 0x690
   __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__auth_ptr: 0x280
-  __DATA_CONST.__const: 0x9c8
+  __DATA_CONST.__const: 0x9d0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xd8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0C679151-C255-39CE-AC84-37C7E84BAE97
+  UUID: 0D57FE37-7F5F-3B94-8E2A-4B79161D3C5C
   Functions: 346
-  Symbols:   119
+  Symbols:   120
   CStrings:  45
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression

```
