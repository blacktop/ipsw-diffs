## AudioUIPlugin

> `/System/Library/Snippets/UIPlugins/AudioUIPlugin.bundle/AudioUIPlugin`

```diff

-3500.94.2.0.0
+3500.100.1.0.0
   __TEXT.__text: 0xf464
   __TEXT.__auth_stubs: 0xe30
   __TEXT.__objc_methlist: 0x16c

   __DATA_CONST.__auth_got: 0x718
   __DATA_CONST.__got: 0x350
   __DATA_CONST.__auth_ptr: 0x3c8
-  __DATA_CONST.__const: 0x6b8
+  __DATA_CONST.__const: 0x6c0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 663EC73B-2B00-30A3-8DFA-D4BCD2C33051
+  UUID: 1434B861-262A-3172-84E4-466F74EF902F
   Functions: 351
-  Symbols:   115
+  Symbols:   116
   CStrings:  98
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private

```
