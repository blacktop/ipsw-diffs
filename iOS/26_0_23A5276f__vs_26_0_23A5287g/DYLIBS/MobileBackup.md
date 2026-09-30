## MobileBackup

> `/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup`

```diff

-2891.0.0.0.0
+2899.0.2.0.0
   __TEXT.__text: 0x3046c
   __TEXT.__auth_stubs: 0xde0
   __TEXT.__objc_methlist: 0x3ff4
-  __TEXT.__const: 0x590
-  __TEXT.__cstring: 0x7d2b
+  __TEXT.__const: 0x598
+  __TEXT.__cstring: 0x7db7
   __TEXT.__gcc_except_tab: 0x1408
   __TEXT.__oslogstring: 0x26f9
-  __TEXT.__unwind_info: 0x1128
+  __TEXT.__unwind_info: 0x1138
   __TEXT.__objc_classname: 0x397
-  __TEXT.__objc_methname: 0x9cff
+  __TEXT.__objc_methname: 0x9d1a
   __TEXT.__objc_methtype: 0x11d1
   __TEXT.__objc_stubs: 0x4b20
   __DATA_CONST.__got: 0x3b0
-  __DATA_CONST.__const: 0x640
+  __DATA_CONST.__const: 0x650
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0x700
   __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0x5bc0
+  __AUTH_CONST.__cfstring: 0x5c00
   __AUTH_CONST.__objc_const: 0x5338
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 64ECFC6A-1908-3B7E-99C0-24C979039B27
+  UUID: 0D986123-A698-3709-A881-ABB14B0C7447
   Functions: 1587
-  Symbols:   4927
-  CStrings:  3891
+  Symbols:   4929
+  CStrings:  3895
 
Symbols:
+ +[MBDomain isLegacyPerAppPlaceholderName:]
+ -[MBDomain isLegacyPerAppPlaceholderDomain]
+ _kMBTargetDeviceTransferMinutesRemainingNotification
+ _kMBTargetDeviceTransferProgressNotification
+ _objc_msgSend$isLegacyPerAppPlaceholderName:
- +[MBDomain isAppPlaceholderName:]
- -[MBDomain isPlaceholderAppDomain]
- _objc_msgSend$isAppPlaceholderName:
CStrings:
+ "TB,R,N,GisLegacyPerAppPlaceholderDomain"
+ "com.apple.private.restrict-post.MobileBackup.d2d.transferMinutesRemaining"
+ "com.apple.private.restrict-post.MobileBackup.d2d.transferProgress"
+ "isLegacyPerAppPlaceholderDomain"
+ "isLegacyPerAppPlaceholderName:"
- "TB,R,N,GisPlaceholderAppDomain"
- "isAppPlaceholderName:"
- "isPlaceholderAppDomain"

```
