## VoiceMemosSettings

> `/System/Library/PreferenceBundles/VoiceMemosSettings.bundle/VoiceMemosSettings`

```diff

-1355.0.0.0.0
+1356.0.0.0.0
   __TEXT.__text: 0x1f48
   __TEXT.__auth_stubs: 0x4a0
   __TEXT.__objc_stubs: 0x3c0

   __DATA_CONST.__auth_got: 0x260
   __DATA_CONST.__got: 0x110
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA_CONST.__const: 0x1c8
+  __DATA_CONST.__const: 0x1d8
   __DATA_CONST.__cfstring: 0x5a0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8F8D6019-2B84-320F-BDB0-1669594C0ACB
+  UUID: CB978735-F231-3AF2-A875-5CBE8B48236D
   Functions: 42
-  Symbols:   121
+  Symbols:   123
   CStrings:  149
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCompression

```
