## SiriMASPFLPush

> `/System/Library/ExtensionKit/Extensions/SiriMASPFLPush.appex/SiriMASPFLPush`

```diff

-85.0.0.0.0
-  __TEXT.__text: 0xcf0
+92.0.0.0.0
+  __TEXT.__text: 0xca4
   __TEXT.__auth_stubs: 0x1b0
   __TEXT.__const: 0x132
   __TEXT.__swift5_entry: 0x8

   __DATA_CONST.__auth_got: 0xd8
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x98
+  __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x38
   __DATA.__bss: 0x100

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D28E426C-99AA-3124-B835-B4057AABAEE4
+  UUID: 80107A43-B913-33C1-9FC1-20489A42A450
   Functions: 24
-  Symbols:   32
+  Symbols:   33
   CStrings:  1
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio
Functions:
~ sub_100001250 -> sub_100001298 : 252 -> 228
~ sub_100001430 -> sub_100001460 : 244 -> 220
~ sub_100001aa8 -> sub_100001ac0 : 264 -> 244
~ sub_100001d98 -> sub_100001d9c : 76 -> 68

```
