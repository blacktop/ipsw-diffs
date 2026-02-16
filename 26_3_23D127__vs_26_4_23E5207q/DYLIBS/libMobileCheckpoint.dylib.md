## libMobileCheckpoint.dylib

> `/usr/lib/libMobileCheckpoint.dylib`

```diff

 40.0.0.0.0
-  __TEXT.__text: 0x81c
-  __TEXT.__auth_stubs: 0x1d0
-  __TEXT.__cstring: 0x19e
+  __TEXT.__text: 0x874
+  __TEXT.__auth_stubs: 0x1e0
+  __TEXT.__cstring: 0x1dd
   __TEXT.__unwind_info: 0x78
   __TEXT.__objc_methname: 0x109
   __TEXT.__objc_stubs: 0x160
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x58
-  __AUTH_CONST.__auth_got: 0xf0
+  __AUTH_CONST.__auth_got: 0xf8
   __AUTH_CONST.__cfstring: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 13566CE0-8C77-3408-A651-56183D813DEB
+  UUID: F53BED4B-264B-3B81-8261-47063BC1B5E1
   Functions: 5
-  Symbols:   56
+  Symbols:   57
   CStrings:  31
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
+ _objc_retain_x23
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x8
Functions:
~ _MCCopyCheckpoint : 560 -> 592
~ __cacheValid : 324 -> 336
~ _MCCopyCheckpointData : 340 -> 352
~ _MCCopyCheckpointValue : 620 -> 644
~ _getResponseForCommand : 232 -> 240
CStrings:
+ "/Library/Caches/com.apple.xbs/0F6C8B0A-8CE6-49C2-A5FB-D181B630AE7E/TemporaryDirectory.F0hSdr/Sources/MobileCheckpoint/MobileCheckpoint.m"
- "/Library/Caches/com.apple.xbs/Sources/MobileCheckpoint/MobileCheckpoint.m"

```
