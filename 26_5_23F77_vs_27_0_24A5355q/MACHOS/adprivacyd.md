## adprivacyd

> `/usr/libexec/adprivacyd`

```diff

-637.5.1.0.0
-  __TEXT.__text: 0x48c
-  __TEXT.__auth_stubs: 0x140
-  __TEXT.__objc_stubs: 0x160
+638.0.7.0.0
+  __TEXT.__text: 0x3e8
+  __TEXT.__auth_stubs: 0x130
+  __TEXT.__objc_stubs: 0x120
   __TEXT.__const: 0x38
   __TEXT.__cstring: 0x117
-  __TEXT.__objc_methname: 0xb3
+  __TEXT.__objc_methname: 0x91
   __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0xa8
-  __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__linkguard: 0x1e
-  __DATA.__objc_selrefs: 0x58
+  __DATA_CONST.__auth_got: 0xa0
+  __DATA_CONST.__got: 0x38
+  __DATA.__objc_selrefs: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AdCore.framework/AdCore

   - /System/Library/PrivateFrameworks/AdPlatformsInternal.framework/AdPlatformsInternal
   - /System/Library/PrivateFrameworks/LimitAdTracking.framework/LimitAdTracking
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
-  - /System/Library/PrivateFrameworks/PromotedContentPrediction.framework/PromotedContentPrediction
   - /usr/appleinternal/lib/liblinkguard.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9CC2F977-E307-3DEF-9202-B2C0CEDD30C8
+  UUID: AB20618D-A04F-32F0-B8E8-95D2AEE3ED23
   Functions: 3
-  Symbols:   35
-  CStrings:  37
+  Symbols:   32
+  CStrings:  35
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
- _MKBDeviceUnlockedSinceBoot
- _OBJC_CLASS_$_APOdmlDatabaseConfiguration
- _OBJC_CLASS_$_APOdmlStoreServerContainer
- _objc_retainAutoreleasedReturnValue
Functions:
~ sub_100000ba0 -> sub_100000b20 : 740 -> 616
~ sub_100000e98 -> sub_100000d9c : 404 -> 364
CStrings:
- "setProcessToDaemon"
- "startListening"

```
