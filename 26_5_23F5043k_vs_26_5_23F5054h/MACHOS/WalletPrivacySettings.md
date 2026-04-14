## WalletPrivacySettings

> `filesystem/System/Library/Settings/WalletPrivacySettings.settings/WalletPrivacySettings`

```diff

-1642.6.1.0.0
+1642.6.3.0.0
   __TEXT.__text: 0x22f8
   __TEXT.__auth_stubs: 0x4f0
   __TEXT.__objc_stubs: 0x1c0

   __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x80
-  __DATA_CONST.__const: 0x128
+  __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7E4963AA-B587-3A86-9806-2979C2F892D4
+  UUID: B59EB74F-C2C5-38FA-97ED-7653A88B34BF
   Functions: 55
-  Symbols:   99
+  Symbols:   100
   CStrings:  95
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCallKit

```
