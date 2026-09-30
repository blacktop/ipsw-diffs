## PrivateEvolutionPlugin

> `/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/PrivateEvolutionPlugin`

```diff

-76.0.0.0.0
+78.0.0.0.0
   __TEXT.__text: 0x1b1a8
   __TEXT.__auth_stubs: 0x1120
   __TEXT.__objc_methlist: 0x20

   __DATA_CONST.__auth_got: 0x890
   __DATA_CONST.__got: 0x248
   __DATA_CONST.__auth_ptr: 0x2d0
-  __DATA_CONST.__const: 0xae0
+  __DATA_CONST.__const: 0xae8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 135FCC2E-0E8C-3900-9B56-0AC4C7C8E76C
+  UUID: 94205C18-D77E-305E-9371-542591603F0F
   Functions: 420
-  Symbols:   145
+  Symbols:   146
   CStrings:  134
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression

```
