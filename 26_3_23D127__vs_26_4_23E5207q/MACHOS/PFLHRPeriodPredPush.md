## PFLHRPeriodPredPush

> `/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredPush.appex/PFLHRPeriodPredPush`

```diff

 71.0.0.0.0
-  __TEXT.__text: 0xd90
+  __TEXT.__text: 0xd44
   __TEXT.__auth_stubs: 0x1e0
   __TEXT.__const: 0x10a
   __TEXT.__swift5_entry: 0x8

   __DATA_CONST.__auth_got: 0xf0
   __DATA_CONST.__got: 0x58
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
-  UUID: 165D4734-C2B8-3F3C-9785-FEBFBCDF7F2C
+  UUID: D6B623D8-37F3-3511-82E8-63B27C164016
   Functions: 24
-  Symbols:   30
+  Symbols:   31
   CStrings:  1
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio
Functions:
~ sub_1000012a8 -> sub_1000012f0 : 252 -> 228
~ sub_100001488 -> sub_1000014b8 : 244 -> 220
~ sub_100001b94 -> sub_100001bac : 264 -> 244
~ sub_100001e90 -> sub_100001e94 : 76 -> 68

```
